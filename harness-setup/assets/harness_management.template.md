# Harness Management

The generic runbook for maintaining docs harnesses in this repository.
`AGENTS.md` holds always-on global rules; this file holds process only. It must
not contain scope-specific paths or artifact rules.

## Start of docs-harness work

Before creating or maintaining harness docs, confirm with the user:

1. harness directory
2. mode: `init` or `adopt`
3. topic/responsibility
4. whether paths outside the harness directory may be read

If any answer is missing or ambiguous, ask before editing.

## After every task

For the user-selected docs harness, decide by what changed:

| You changed... | Update |
|---|---|
| Direction, boundaries, success criteria | `docs/idea/idea.md` |
| Current architecture or behavior | `docs/architecture/ARCHITECTURE.md` |
| Major direction decision | `docs/architecture/decisions/NNNN-title.md` |
| Test/debug method or artifact policy | `docs/testing/METHOD.md` |
| Ran a debug/test round | `docs/testing/log/` |
| Found a durable reusable lesson | `docs/testing/findings.md` |

Scope-specific artifact locations, generated-data rules, and sensitive paths
belong inside that docs harness, usually in `docs/testing/METHOD.md` or a
specific architecture doc.

## Anti-patterns

- Do not create scoped `AGENTS.md` or scoped `harness_management.md` by default.
- Do not put scope-specific paths in root `AGENTS.md` or this file.
- Do not migrate content across docs harnesses without user permission.
- Do not create version-numbered living docs; update the current doc and let git
  hold history.

## Verification

After docs-harness work, verify:

- no `{{PLACEHOLDER}}` remains
- local markdown links still resolve
- generated/local-only artifacts are not staged for commit

_This doc is maintained by hand. Keep it generic._
