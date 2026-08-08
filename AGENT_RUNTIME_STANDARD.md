# Ventura Agent Runtime Standard

This document defines the shared runtime model for Ventura Labs AI repositories that contain Agent Skills.

## Execution architecture

```text
USER / EVENT
    -> ORCHESTRATOR
    -> INTENT + ROUTER
    -> PLANNER
    -> SKILLS + TOOLS/MCP + RAG + MEMORY + APIs/DATABASES
    -> EXECUTION ENGINE
    -> VERIFIER / CRITIC
    -> GUARDRAILS
    -> RESULT
    -> MEMORY + TELEMETRY + EVALS
```

## Twelve required pillars

1. **Agent Skills** — reusable task procedures stored as `.github/skills/<name>/SKILL.md`.
2. **Tools / MCP** — external capabilities selected on demand, never all exposed at once.
3. **RAG** — retrieve authoritative repository, documentation, API, or database context before generation when facts can drift.
4. **Memory** — separate working, short-term, semantic, and persistent memory; persist only what the product needs.
5. **Planner** — decompose goals into bounded steps with explicit success criteria.
6. **Orchestrator** — route intent to the smallest capable skill, model, and connector set.
7. **Model routing** — use the smallest adequate model for simple work and escalate only for harder reasoning.
8. **Evals** — test skills, connector selection, expected outputs, refusals, and regressions.
9. **Guardrails** — default deny for dangerous actions; approval gates for write, delete, deploy, payments, secrets, or privileged operations.
10. **Observability** — structured logs, traces, latency, error rate, tool calls, token/cost signals, and correlation IDs.
11. **Cache** — cache stable retrieval and deterministic transforms with explicit TTL/invalidation rules.
12. **CI/CD** — validate skill format, connector manifests, security scans, tests, builds, SBOM, and release provenance.

## Connector policy

- Maintain a broad repository connector catalog, but activate **no more than 6 connectors for one skill invocation** unless a documented exception exists.
- Prefer first-party/official provider integrations and MCP servers.
- Default to read-only access; grant write access only for the exact skill that needs it.
- Require human approval for destructive, external-publishing, payment, deployment, credential, or security-control changes.
- Keep secrets in environment variables, a secret manager, or platform Agent Secrets; never commit credentials.
- Use per-skill routing in `.github/agent/connectors.json`.
- A connector listed in the manifest is **supported/configurable**, not proof that credentials are installed in every runtime.
- Fail closed when a required connector is unavailable for a high-impact action; do not silently substitute an untrusted service.

## Connector trust levels

- `official`: first-party MCP server or provider-maintained integration.
- `native`: direct SDK/API/database integration maintained as application code.
- `local`: local runtime tool such as filesystem, Docker, or a test runner.

## Routing contract

For every skill invocation:

1. identify the skill and requested effect;
2. load its connector route from `.github/agent/connectors.json`;
3. enable the smallest connector subset that can satisfy the task;
4. prefer read-only tools during discovery;
5. plan before write actions;
6. execute with timeouts, retries, idempotency where applicable;
7. verify the result using an independent check when possible;
8. emit telemetry without secrets or unnecessary personal data;
9. record eval evidence for reusable production workflows.

## Performance rules

- Prefer CLI/SDK calls over MCP when they are more token-efficient and equally auditable.
- Use MCP when standardized discovery, remote access, persistent tool state, or cross-client portability is valuable.
- Cache documentation and retrieval results when freshness permits.
- Parallelize independent read operations; serialize conflicting writes.
- Bound retries with exponential backoff and a circuit breaker.
- Keep connector schemas out of model context until the router selects them.

## Security baseline

- least privilege;
- explicit allowlists;
- read-only by default;
- human-in-the-loop for high-impact writes;
- prompt-injection-aware retrieval boundaries;
- secret redaction;
- connector provenance and version tracking;
- timeout, retry, and rate-limit handling;
- audit log for tool decisions;
- regular connector revalidation because endpoints and tool schemas can drift.
