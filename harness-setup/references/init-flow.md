# Init flow — create a docs harness

Use when the user wants a new docs harness under a specified `HARNESS_DIR`.
Work in propose → approve → write phases unless the user explicitly asks for
autonomous execution.

Templates are in `assets/*.template.md`. Fill every `{{PLACEHOLDER}}`.

## Phase 0 — scope interview

Confirm:

- `HARNESS_DIR`
- topic/responsibility of this docs harness
- whether Codex may read outside `HARNESS_DIR`
- any known artifact/data/privacy boundaries

Then inspect real files in the allowed scope: README/docs, scripts, source
entrypoints, tests, data/output directories, and git status.

`✓ FINISH — init phase 0: scope` · Locked: harness directory and allowed context.

## Phase 1 — docs/README.md + idea

Create:

- `<HARNESS_DIR>/docs/README.md`
- `<HARNESS_DIR>/docs/idea/idea.md`

`docs/README.md` must tell future users to specify the harness directory, mode,
topic, and outside-read permission before asking an agent to maintain this docs
harness.

`idea.md` states the goal, users, boundaries, constraints, and success criteria.
Keep it directional, not a detailed spec.

`✓ FINISH — init phase 1: idea + index`

## Phase 2 — architecture

Create:

- `<HARNESS_DIR>/docs/architecture/ARCHITECTURE.md`
- `<HARNESS_DIR>/docs/architecture/decisions/.gitkeep`

Describe the current state of the selected scope. Do not enumerate raw file
trees; describe roles, flows, and status.

`✓ FINISH — init phase 2: architecture`

## Phase 3 — testing

Create:

- `<HARNESS_DIR>/docs/testing/METHOD.md`
- `<HARNESS_DIR>/docs/testing/findings.md`
- `<HARNESS_DIR>/docs/testing/log/.gitkeep`

Record how to run/reproduce checks, where artifacts live, and which generated
outputs should stay out of git. Keep specific artifact rules here or in
architecture docs, not root runbooks.

`✓ FINISH — init phase 3: testing`

## Phase 4 — verify

- Confirm the tree.
- Verify no `{{PLACEHOLDER}}` remains.
- Check local markdown links.
- Summarize what the docs harness covers and what remains TBD.

Do not create scoped `AGENTS.md` or scoped `harness_management.md`.

`✓ FINISH — init complete`
