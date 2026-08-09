#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROLES = {
    "orchestrator",
    "engineering_platform",
    "security",
    "agent_catalog",
    "provider_catalog",
    "shared_sdk",
    "optimizer",
    "roadmap",
    "knowledge",
    "discovery",
    "curation",
    "domain_product",
    "experimental_domain",
}
BUDGETS = {"simple", "normal", "critical"}
CONTEXT_STRATEGIES = {"semantic_ast", "semantic", "diff_first"}
AUTONOMY = {"high", "guarded", "curation"}


def validate(payload: dict) -> list[str]:
    errors: list[str] = []
    if payload.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if payload.get("repository_role") not in ROLES:
        errors.append(f"repository_role must be one of {sorted(ROLES)}")
    if payload.get("autonomy") not in AUTONOMY:
        errors.append(f"autonomy must be one of {sorted(AUTONOMY)}")
    if payload.get("budget_profile") not in BUDGETS:
        errors.append(f"budget_profile must be one of {sorted(BUDGETS)}")

    context = payload.get("context") or {}
    if context.get("strategy") not in CONTEXT_STRATEGIES:
        errors.append(f"context.strategy must be one of {sorted(CONTEXT_STRATEGIES)}")
    max_files = context.get("max_files")
    max_chars = context.get("max_chars")
    if not isinstance(max_files, int) or not 1 <= max_files <= 50:
        errors.append("context.max_files must be an integer from 1 to 50")
    if not isinstance(max_chars, int) or not 1000 <= max_chars <= 100000:
        errors.append("context.max_chars must be an integer from 1000 to 100000")

    routing = payload.get("routing") or {}
    for key in ("enabled", "champion_challenger"):
        if not isinstance(routing.get(key), bool):
            errors.append(f"routing.{key} must be boolean")

    validation = payload.get("validation") or {}
    required = validation.get("required")
    if not isinstance(required, list) or not required or not all(isinstance(v, str) and v for v in required):
        errors.append("validation.required must be a non-empty string list")

    security = payload.get("security") or {}
    hard_gates = security.get("hard_gates")
    if not isinstance(hard_gates, list) or not hard_gates or not all(isinstance(v, str) and v for v in hard_gates):
        errors.append("security.hard_gates must be a non-empty string list")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=".ventura/repo-profile.json")
    args = parser.parse_args()
    path = Path(args.path)
    if not path.is_file():
        print(f"missing repository profile: {path}")
        return 2
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"invalid repository profile: {exc}")
        return 2
    errors = validate(payload)
    if errors:
        for error in errors:
            print(f"PROFILE ERROR: {error}")
        return 1
    print(
        "PROFILE OK: "
        f"role={payload['repository_role']} autonomy={payload['autonomy']} "
        f"budget={payload['budget_profile']} context={payload['context']['strategy']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
