# Self-Evolution Workflow

After every real application filling or audit, update this skill before the final response unless the user explicitly asks not to modify files.

## What To Update

- New ATS behavior: write to the ATS reference file such as `mokahr.md` or `beisen.md`.
- General reusable behavior: write to `ats-common.md`.
- Role-specific ordering or wording choice: write to `role-strategies.md`.
- Failure, workaround, and unresolved validation symptom: write to `validation-and-failure-log.md`.
- Repeated deterministic diagnostic command: add or patch a script in `scripts/`.

## Update Format

Record concise, reusable observations:

- Context: company, ATS, page or section.
- Symptom: what happened.
- Cause or inference: why it likely happened, if known.
- Tactic: what worked or should be tried next.
- Boundary: what still requires user permission or judgment.

Avoid writing one-off narration, full transcripts, or sensitive personal values.

## Maintenance Rules

- Prefer improving an existing rule over adding duplicate notes.
- Keep `SKILL.md` short. Put detailed system-specific behavior in references.
- Validate the skill after edits with the skill-creator validator.
- If a new company uses the same ATS but a different schema, record the schema difference instead of assuming the old order is wrong.
