---
name: harness-setup
description: >-
  Set up or clean up a user-specified docs harness for a project area, while
  keeping AGENTS.md and harness_management.md unique at the repository root. Use
  when Codex needs to create or adopt scoped documentation under a directory such
  as evals/, training/datapipe/, or training/grpo/: docs/idea, docs/architecture,
  and docs/testing. Also use when an existing area's docs are messy, stale,
  duplicated, or need a clean agent-facing documentation structure.
---

# Harness Setup

Establish or repair a **docs harness** for a user-specified project area. This
skill is intentionally scoped: it creates or adopts docs under a chosen
`HARNESS_DIR`, while `AGENTS.md` and `harness_management.md` remain unique at the
repository root and stay generic.

## Shape

Global, at repo root:

1. `AGENTS.md` — always-loaded global invariants only.
2. `harness_management.md` — generic upkeep process only.

Per docs harness, under the user-selected `HARNESS_DIR`:

```text
<HARNESS_DIR>/docs/README.md
<HARNESS_DIR>/docs/idea/idea.md
<HARNESS_DIR>/docs/architecture/ARCHITECTURE.md
<HARNESS_DIR>/docs/architecture/decisions/
<HARNESS_DIR>/docs/testing/METHOD.md
<HARNESS_DIR>/docs/testing/findings.md
<HARNESS_DIR>/docs/testing/log/
```

Do **not** create scoped `AGENTS.md` or scoped `harness_management.md` unless the
user explicitly asks for that different design.

Read [`references/conventions.md`](references/conventions.md) before writing docs.

## Step 1 — Ask first

For both `init` and `adopt`, start by asking the user enough to pin down the work:

- Which `HARNESS_DIR` should own these docs?
- Is this `init` or `adopt`?
- What is this docs harness about?
- May Codex read paths outside `HARNESS_DIR` as supporting context, or should it
  stay inside the harness directory?

Do not infer these silently. If the user already answered them in the request,
state the assumptions and proceed.

## Step 2 — Detect the mode inside HARNESS_DIR

After the user specifies `HARNESS_DIR`:

- **`init`**: create a new docs harness under `<HARNESS_DIR>/docs/`.
  Follow [`references/init-flow.md`](references/init-flow.md).
- **`adopt`**: audit and reshape existing docs in that harness directory.
  Follow [`references/adopt-flow.md`](references/adopt-flow.md).

The mode is still only `init` or `adopt`. The scoped behavior comes from
`HARNESS_DIR`, not from additional mode names.

## Step 3 — Read real scope content before drafting

Before proposing docs, inspect the actual harness area: existing README/docs,
source entrypoints, scripts, test commands, data/output directories, and relevant
git status. If the user disallowed outside reads, stay inside `HARNESS_DIR`.
Templates are starting points only; do not produce generic filler.

## Step 4 — Propose → approve → write

This skill does not mass-write files silently. For each phase:

1. Propose the draft or mapping.
2. Get approval, unless the user explicitly asked you to proceed autonomously.
3. Write files with all `{{PLACEHOLDER}}` values filled.
4. Emit a FINISH signal:

```text
✓ FINISH — <mode> phase <N>: <name>
  Produced: <files written or changed>
  Locked:   <decisions settled>
  Next:     <next phase or user action>
```

## Assets and script

- Templates live in [`assets/`](assets/).
- `scripts/audit.sh <repo-root> <harness-dir>` audits one docs harness area.

`AGENTS.template.md` and `harness_management.template.md` are for explicitly
requested root-level setup only. Normal scoped harness work uses the docs
templates and does not touch root agent files.

## Rules

- Keep root `AGENTS.md` and root `harness_management.md` generic.
- Put scope-specific knowledge in the selected harness docs.
- Do not migrate or borrow content from another harness unless the user permits it.
- Do not create version-numbered living docs. Current docs describe the present;
  git holds history, and major direction changes go in ADRs.
- Keep generated artifacts and secrets out of committed docs.

## What this skill will not do

- Write product code.
- Decide architecture for the user.
- Build domain-specific test/eval machinery.
- Automatically rewrite root `AGENTS.md` or `harness_management.md` for scoped
  harness work.
