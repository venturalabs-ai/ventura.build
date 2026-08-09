from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
SHA = re.compile(r"^[0-9a-fA-F]{40}$")
USES = re.compile(r"^\s*-?\s*uses:\s*([^\s#]+)")


def test_reusable_autonomy_gate_exists():
    text = (WORKFLOWS / "autonomy-gate.yml").read_text(encoding="utf-8")
    assert "workflow_call:" in text
    assert "Reject decorative test scaffolds" in text
    assert "Require immutable GitHub Action refs" in text


def test_external_actions_are_immutable():
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
    assert not failures, "mutable action refs: " + ", ".join(failures)


def test_failure_issue_template_is_deduplicated_and_least_privilege():
    text = (ROOT / "templates" / "ci-failure-issue.yml").read_text(encoding="utf-8")
    assert "issues: write" in text
    assert "workflow_run:" in text
    assert "state=open" in text
    assert "Created failure issue" in text
