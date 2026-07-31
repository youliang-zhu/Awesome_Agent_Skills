---
name: computer-use-agent-job
description: Automate and maintain Chinese job application form filling workflows with Chrome/computer-use for campus recruitment, internships, and full-time applications. Use when Codex needs to fill, audit, resume, or improve online application forms in ATS systems such as Mokahr, Beisen, Feishu, HotJob, or company-hosted portals; map a resume/profile document to web form fields; handle dropdowns, autocomplete, required-field validation, multi-screen user coordination; and learn, correct, version, commit, and push reusable ATS-specific filling rules after every live run.
---

# Computer Use Agent Job

## Core Rule

Use this skill to make live job-application filling faster, more accurate, and easier to improve after every run. Treat the application page as a fragile UI automation task: read source data, identify the ATS, reuse applicable lessons, fill conservatively, verify visually and structurally, and update this skill with new evidence before finishing.

Do not submit, preview-submit, withdraw, delete, or upload a resume unless the user explicitly authorizes that exact action in the current conversation.

For every live application-form run, learning and Git synchronization are required deliverables. Record the run even when it produces no new reusable rule. If a reusable lesson changes, update the relevant reference, validate the skill, commit only this skill's changes, and push the current branch. Never force-push or include unrelated worktree changes.

## Source Data

Prefer user-maintained source documents over memory. For this workspace, read `D:\zGraduateStudy\实习与求职\resume_info.md` before filling or auditing application data. Use the current resume PDF only as a resume-content baseline when the user explicitly asks to refresh profile/project wording.

Do not copy sensitive personal data into this skill unless the user explicitly requests it. Store reusable mapping rules here; keep personal facts in the profile document.

## Workflow

1. Confirm the target company, job title, ATS/page type, and whether the task is fill, audit, resume, or maintain.
2. Read the profile source and the relevant role strategy.
3. Identify the ATS from the host, visible branding, page assets, and UI behavior. Read `references/ats-common.md`, the matching ATS reference, and applicable recent entries in `references/validation-and-failure-log.md`. Use `references/mokahr.md` for Mokahr, `references/beisen.md` for Beisen/Phoenix, `references/feishu.md` for Feishu Recruitment, `references/hotjob.md` for HotJob-style pages, and `references/oppo.md` for OPPO's company-hosted university resume editor. Treat each company's schema as a possible variant of the vendor platform.
4. Build a short fill plan by page section: personal information, education, internships, projects, awards, skills, language, open questions.
5. Fill stable text fields first, then dates/spinners, then dropdowns/cascading selectors/autocomplete fields.
6. Add repeated entries one at a time. After each add, verify the current visual state before continuing because ATS pages may reorder or insert blank cards near the viewport.
7. Before using computer-use, tell the user not to move the mouse or use the keyboard until the filling run pauses or finishes. Shared input devices can make Codex and the user fight for mouse/keyboard focus and cause form-filling failure. See `references/ats-common.md`.
8. Scan for required-field errors and mismatches. Resolve fields that can be filled from source data; report fields needing user choice.
9. Before finishing, run the mandatory post-run learning workflow in `references/self-evolution.md`: append one sanitized run record, reconcile reusable rules with new evidence, mark corrections or superseded rules, and avoid duplicating existing guidance.
10. Validate the skill. If the skill changed, stage only `computer-use-agent-job/`, inspect the staged diff, commit, and push the current branch according to `references/self-evolution.md`. If validation, commit, or push fails, preserve the local work and report the unsynchronized state; do not claim the run is fully closed.

## Completion Gate

A live fill, audit, or resume run is not complete until all of the following are true:

- The form state and unresolved user decisions are reported accurately.
- A run record is appended without personal values, credentials, or page transcripts.
- New evidence is merged into the correct common or ATS-specific rule, or the run record explicitly says no reusable rule changed.
- Conflicting guidance is narrowed, corrected, or marked superseded instead of being silently duplicated.
- Skill validation passes.
- Any skill changes are committed and pushed. A failed push is an explicit incomplete synchronization state, not a reason to force-push.

## Reference Routing

- Read `references/ats-common.md` for cross-ATS filling rules, user-coordination rules, and validation discipline.
- Read `references/mokahr.md` for Mokahr-specific selectors, dropdown/autocomplete behavior, and known failure modes from ZTE/Sohu applications.
- Read `references/beisen.md` when the page is Beisen or resembles Beisen.
- Read `references/feishu.md` when the page is Feishu Recruitment or its branding/assets identify a Feishu recruiting form.
- Read `references/hotjob.md` when the page URL or UI resembles `*.hotjob.cn` old-style resume forms.
- Read `references/oppo.md` for `careers.oppo.com` university resume pages and their section-save, education, date, portfolio, and publication-field behavior.
- Read `references/cmbnt.md` for the company-hosted CMBNT resume editor on `cmbnt.cmbchina.com`, including parser gaps, special-character validation, award dates, and draft behavior.
- Read `references/role-strategies.md` before choosing which internships/projects/awards to prioritize for a job family.
- Read `references/self-evolution.md` before the first live action and again before editing this skill after a real application run.
- Read `references/validation-and-failure-log.md` before a live run for similar prior symptoms and append exactly one run record afterward.

## Automation Helpers

Optional PowerShell helpers live in `scripts/`. Use them only when they fit the current UI-control approach:

- `scripts/inspect_chrome_uia.ps1`: inspect visible Chrome UI Automation controls.
- `scripts/scan_required_errors.ps1`: list visible required-field validation texts.
- `scripts/record_run.py`: append the required sanitized post-run record; use `--dry-run` to review it before writing.

These scripts are diagnostic aids, not a substitute for visual verification.
