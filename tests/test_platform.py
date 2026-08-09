from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
SHA = re.compile(r"^[0-9a-fA-F]{40}$")
USES = re.compile(r"^\s*-?\s*uses:\s*([^\s#]+)")


class PlatformTests(unittest.TestCase):
    def test_reusable_autonomy_gate_exists(self):
        text = (WORKFLOWS / "autonomy-gate.yml").read_text(encoding="utf-8")
        self.assertIn("workflow_call:", text)
        self.assertIn("Reject decorative test scaffolds", text)
        self.assertIn("Require immutable GitHub Action refs", text)
        self.assertIn("Validate repository control profile", text)

    def test_external_actions_are_immutable(self):
        failures = []
        for path in WORKFLOWS.glob("*.yml"):
            for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                match = USES.match(line)
                if not match:
                    continue
                target = match.group(1)
                if target.startswith("./") or target.startswith("docker://"):
                    continue
                if "@" not in target or not SHA.fullmatch(target.rsplit("@", 1)[1]):
                    failures.append(f"{path.name}:{line_no}:{target}")
        self.assertFalse(failures, "mutable action refs: " + ", ".join(failures))

    def test_failure_issue_template_is_deduplicated_and_least_privilege(self):
        text = (ROOT / "templates" / "ci-failure-issue.yml").read_text(encoding="utf-8")
        self.assertIn("issues: write", text)
        self.assertIn("workflow_run:", text)
        self.assertIn("state=open", text)
        self.assertIn("Created failure issue", text)

    def test_retry_template_has_single_retry_guard(self):
        text = (ROOT / "templates" / "ci-auto-retry.yml").read_text(encoding="utf-8")
        self.assertIn("actions: write", text)
        self.assertIn("run_attempt < 2", text)
        self.assertIn("rerun-failed-jobs", text)

    def test_repository_profile_is_valid(self):
        result = subprocess.run(
            [sys.executable, "scripts/validate_repo_profile.py", ".ventura/repo-profile.json"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
