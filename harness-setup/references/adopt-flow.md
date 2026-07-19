# Adopt flow — retrofit a docs harness

Use when the user wants to clean up or reshape existing docs for a specified
`HARNESS_DIR`. The goal is to organize that area's docs into the idea /
architecture / testing buckets without silently changing ownership boundaries.

## Phase 0 — scope interview

Confirm:

- `HARNESS_DIR`
- topic/responsibility of this docs harness
- whether Codex may read outside `HARNESS_DIR`
- whether existing docs should be moved, distilled, or only indexed

If the user has not answered, ask before editing.

`✓ FINISH — adopt phase 0: scope`

## Phase 1 — audit

Run:

```bash
bash scripts/audit.sh <repo-root> <harness-dir>
```

Read flagged docs enough to classify them. Also inspect real scope content:
README/docs, scripts, source entrypoints, tests, and data/output directories.

Present an audit summary: what exists, what is stale, what duplicates, what is a
graveyard, and what appears outside the selected harness.

`✓ FINISH — adopt phase 1: audit`

## Phase 2 — mapping

For each relevant existing doc, propose one action:

- **Keep/index** in place.
- **Move** into `docs/idea`, `docs/architecture`, or `docs/testing`.
- **Distill** durable current content into the new bucket.
- **Delete** redundant/dead content; git retains history.
- **Leave outside scope** when the content belongs to another harness.

Do not migrate content across docs harnesses unless the user explicitly approves.

`✓ FINISH — adopt phase 2: mapping`

## Phase 3 — migrate

Execute the approved mapping. Prefer `git mv` for moves inside a git repo. Fix
links affected by moves. Seed `findings.md` only with confirmed durable lessons.

Do not create scoped `AGENTS.md` or scoped `harness_management.md`.

`✓ FINISH — adopt phase 3: migration`

## Phase 4 — verify

- Re-run the scoped audit.
- Verify no `{{PLACEHOLDER}}` remains.
- Confirm the docs harness covers only the user-approved scope.
- Summarize remaining user-owned cleanup.

`✓ FINISH — adopt complete`
