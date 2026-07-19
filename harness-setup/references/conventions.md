# Conventions — docs harness design

These conventions keep a repository with many project areas from accumulating one
overloaded root documentation system.

## Global files stay unique

The repo root owns exactly one always-loaded rules file and one upkeep runbook:

| Layer | File | Holds |
|---|---|---|
| Global rules | `AGENTS.md` | repo-wide invariants only |
| Global process | `harness_management.md` | generic upkeep process only |

Neither file should contain project-area-specific paths, artifact rules, or
current status. Those belong in the selected docs harness.

## Docs harnesses are scoped

A docs harness lives under a user-selected `HARNESS_DIR` and owns only docs:

```text
<HARNESS_DIR>/docs/idea/
<HARNESS_DIR>/docs/architecture/
<HARNESS_DIR>/docs/testing/
```

The user must identify the current harness before work starts. When ambiguous,
ask. Do not guess the docs root from path names alone.

## Split by volatility

- **Stable global invariant**: root `AGENTS.md`.
- **Generic maintenance process**: root `harness_management.md`.
- **Scope-specific direction, architecture, test method, artifacts, findings**:
  `<HARNESS_DIR>/docs/`.

This keeps root files small while allowing each area to be specific.

## Current state, not history

Living docs describe the present. Do not create version-numbered plan files.
Update the current doc; git preserves history. Record major direction changes as
short ADRs in `docs/architecture/decisions/`.

## Graduation mechanism

The testing bucket uses a lifecycle:

```text
docs/testing/log/  ->  docs/testing/findings.md  ->  regression fixture when useful
```

Raw logs are pruned after durable lessons graduate.

## User-owned scope

The user owns harness boundaries. The skill asks for `HARNESS_DIR`, mode, topic,
and whether outside paths may be read. Generated docs must be based on real scope
content, not generic template language.

## Anti-patterns

- Creating scoped `AGENTS.md` or `harness_management.md` by default.
- Putting scope-specific artifact rules in root files.
- Migrating content across docs harnesses without user permission.
- Freezing file trees or volatile status into root `AGENTS.md`.
- Producing empty template docs without reading the target scope.
