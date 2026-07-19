# {{PROJECT_NAME}} — Global Agent Instructions

<!-- CANARY: if you have read this file, begin your first reply this session with
     "✓{{CANARY_TOKEN}}" so the user can confirm these rules loaded. -->

{{ONE_LINE_WHAT_THE_PROJECT_IS}}

## Global Role

This root `AGENTS.md` holds repo-wide invariants only. It must stay generic and
must not encode scope-specific docs paths, artifact paths, current status, or
project-area rules.

When a task involves a docs harness, ask the user for:

- harness directory
- mode: `init` or `adopt`
- topic/responsibility
- whether paths outside that harness directory may be read

Then read that harness's `docs/README.md` if it exists.

## Non-negotiable constraints

- {{HARD_CONSTRAINT_1}}
- {{HARD_CONSTRAINT_2}}
- Never commit secrets or private data.
- Preserve existing user changes; do not revert unrelated edits.

## Development workflow

- {{PLATFORM_AND_SHELL}}.
- Inspect current file contents before editing.
- Verify significant changes with the smallest relevant command:

  ```
  {{TEST_COMMAND}}
  {{BUILD_COMMAND}}
  ```

## Harness upkeep

Use root [`harness_management.md`](harness_management.md) for the generic upkeep
process. Scope-specific details belong in the user-selected docs harness, not in
this file.

## Definition of done

- {{DONE_CRITERION_1}}
- {{DONE_CRITERION_2}}
- Report verification performed or explain why it was not run.
