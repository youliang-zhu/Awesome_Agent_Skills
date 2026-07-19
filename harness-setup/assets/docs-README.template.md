# {{HARNESS_NAME}} docs

This is a scoped docs harness for **{{HARNESS_TOPIC}}**.

## Before asking an agent to maintain this harness

Tell the agent:

- Harness directory: `{{HARNESS_DIR}}`
- Mode: `init` or `adopt`
- Topic/responsibility: {{HARNESS_TOPIC}}
- Outside-read permission: {{OUTSIDE_READ_POLICY}}

The root `AGENTS.md` and root `harness_management.md` remain the only global
agent rules/runbook. This docs harness owns only the documentation below.

## Buckets

| Bucket | Holds | Read/write pattern |
|---|---|---|
| [`idea/`](idea/) | Direction, boundaries, success criteria | Stable "why & what" |
| [`architecture/`](architecture/) | Current architecture, plans, ADRs | Present state; history via git + ADRs |
| [`testing/`](testing/) | Test method, findings, per-round log | Lessons graduate from `log/` to `findings.md` |

## Scope notes

- Owned scope: {{OWNED_SCOPE}}
- Important artifact/data boundaries: {{ARTIFACT_BOUNDARIES}}
- Sensitive or local-only paths: {{SENSITIVE_PATHS}}

Do not borrow or migrate content from another docs harness unless the user
explicitly permits it.
