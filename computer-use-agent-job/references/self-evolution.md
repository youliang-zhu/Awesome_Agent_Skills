# Self-Evolution Workflow

Use this workflow before and after every live application-form fill, audit, or resume run. The objective is to reuse verified ATS behavior, preserve contradictory evidence, correct obsolete guidance, and synchronize the learned skill to Git.

## Before The Run: Retrieve Applicable Experience

1. Identify the platform from the host, visible branding, page assets, and UI behavior. Do not classify from visual similarity alone when stronger evidence exists.
2. Read `ats-common.md`, the matching ATS reference, and recent relevant entries in `validation-and-failure-log.md`.
3. Separate vendor behavior from company schema:
   - Vendor behavior belongs in `mokahr.md`, `beisen.md`, `feishu.md`, `hotjob.md`, or a new vendor reference.
   - Cross-platform behavior belongs in `ats-common.md`.
   - Company-only differences stay scoped to a run record until they recur.
4. Apply only rules whose `Applies when` conditions match the current page. Treat `provisional` rules as hypotheses that require verification.

## After The Run: Always Record It

Append exactly one sanitized record to `validation-and-failure-log.md`, even when no reusable rule changed. Prefer `scripts/record_run.py`; it normalizes the record and rejects common sensitive-value patterns. Use this template when the script cannot represent the run:

```markdown
### RUN-YYYYMMDD-HHMMSS-<ats>-<company>

- Date:
- Company / host:
- ATS / variant:
- Scope: sections attempted; fill, audit, or resume
- Outcome: completed, partial, or blocked
- Difficulties: concise symptoms only
- Successful tactics: actions and verification signals
- Failed tactics: what failed and how it was detected
- Rule changes: rule IDs added, updated, superseded, or `none`
- Unresolved: missing source data, UI blocker, user permission, or `none`
- Privacy check: no personal values, credentials, attachments, or page transcript
```

Do not record resume field values, phone numbers, email addresses, IDs, addresses, credentials, auth state, private URLs, or full page text. Generalize company-specific observations to the smallest reusable condition.

## Promote Reusable Lessons

Store each reusable rule in the appropriate common or vendor reference with a stable ID:

```markdown
### RULE-<ATS>-<short-slug>

- Status: provisional | confirmed | superseded
- Applies when: observable preconditions
- Does not apply when: known counterconditions
- Symptom: what the page shows or rejects
- Tactic: the shortest reliable action sequence
- Verification: authoritative success signal
- Evidence: run IDs
- Last reviewed: YYYY-MM-DD
- Supersedes: rule ID or `none`
```

Use these evidence rules:

- Mark a rule `provisional` after one successful run or one well-supported failure diagnosis.
- Mark it `confirmed` after independent reproduction under the same preconditions, or when the page exposes an authoritative success signal that directly proves the behavior.
- Keep company schema differences scoped by host, form version, or visible precondition. Do not generalize one customer's Mokahr/Beisen/Feishu schema to the whole vendor.
- Prefer updating an existing rule over adding a near-duplicate.

## Correct Or Retire A Rule

When new evidence conflicts with an existing rule:

1. Recheck the current page state and verification signal before editing the rule.
2. Compare preconditions. If both observations can be true, narrow `Applies when` and add `Does not apply when` instead of calling either rule wrong.
3. If the old tactic is wrong, unsafe, or obsolete, mark it `superseded`; add the replacement rule and cross-link both rule IDs.
4. Update `Last reviewed` and evidence run IDs.
5. Record the correction in the current run entry. Never silently delete contradictory history.

## What To Update

- New vendor behavior: update the matching ATS reference.
- General reusable behavior: update `ats-common.md`.
- Role-specific ordering or wording choice: update `role-strategies.md`.
- Failure, workaround, correction, or unresolved symptom: update `validation-and-failure-log.md` and the owning rule.
- Repeated deterministic diagnostic command: add or patch a script in `scripts/` and test it.
- Newly identified ATS: add one reference file and route to it from `SKILL.md`; do not copy common rules into it.

## Validate, Commit, And Push

Run this sequence after the run record and rule updates:

1. Locate the Git root with `git rev-parse --show-toplevel` and confirm it is the intended skills repository.
2. Inspect `git status --short`. Preserve unrelated user changes.
3. Run the skill-creator validator against `computer-use-agent-job/` and fix every error.
4. Review the skill diff for personal data, duplicate rules, accidental transcripts, and overly broad claims.
5. Stage only paths under `computer-use-agent-job/`. Never stage unrelated changes.
6. Inspect the staged diff.
7. Commit with a message such as `skill(computer-use-agent-job): learn <ats> <company> <date>`.
8. Push the current branch with `git push origin HEAD`.

Never force-push, rewrite unrelated history, discard user changes, or hide a failed push. If Git authentication, network access, conflicts, or repository state blocks synchronization, keep the local commit when possible and report the exact unpushed state to the user.

## Maintenance Rules

- Keep `SKILL.md` concise; store detailed behavior in references.
- Keep rule IDs stable when wording changes.
- Prefer observable verification signals over inferred success.
- Do not turn a one-off coordinate, control index, or DOM position into a reusable rule.
- Do not edit personal facts into this skill; keep them in the profile source.
