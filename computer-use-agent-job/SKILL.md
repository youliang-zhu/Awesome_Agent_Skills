---
name: computer-use-agent-job
description: Automate and maintain Chinese job application form filling workflows with Chrome/computer-use for campus recruitment, internships, and full-time applications. Use when Codex needs to fill, audit, resume, or improve online application forms in ATS systems such as Mokahr, Beisen, or company-hosted portals; map a resume/profile document to web form fields; handle dropdowns, autocomplete, required-field validation, multi-screen user coordination, and self-updating ATS-specific filling rules.
---

# Computer Use Agent Job

## Core Rule

Use this skill to make live job-application filling faster, more accurate, and easier to improve after every run. Treat the application page as a fragile UI automation task: read source data, identify the ATS, fill conservatively, verify visually and structurally, and update this skill with new lessons before finishing.

Do not submit, preview-submit, withdraw, delete, or upload a resume unless the user explicitly authorizes that exact action in the current conversation.

## Source Data

Prefer user-maintained source documents over memory. For this workspace, read `D:\zGraduateStudy\实习与求职\网申个人信息.md` before filling or auditing application data. Use the current resume PDF only as a resume-content baseline when the user explicitly asks to refresh profile/project wording.

Do not copy sensitive personal data into this skill unless the user explicitly requests it. Store reusable mapping rules here; keep personal facts in the profile document.

## Workflow

1. Confirm the target company, job title, ATS/page type, and whether the task is fill, audit, resume, or maintain.
2. Read the profile source and the relevant role strategy.
3. Identify the ATS. For Mokahr, read `references/mokahr.md`; for Beisen, read `references/beisen.md`; for HotJob-style pages such as CGN, read `references/hotjob.md`; otherwise use `references/ats-common.md`.
4. Build a short fill plan by page section: personal information, education, internships, projects, awards, skills, language, open questions.
5. Fill stable text fields first, then dates/spinners, then dropdowns/cascading selectors/autocomplete fields.
6. Add repeated entries one at a time. After each add, verify the current visual state before continuing because ATS pages may reorder or insert blank cards near the viewport.
7. Before using computer-use, tell the user not to move the mouse or use the keyboard until the filling run pauses or finishes. Shared input devices can make Codex and the user fight for mouse/keyboard focus and cause form-filling failure. See `references/ats-common.md`.
8. Scan for required-field errors and mismatches. Resolve fields that can be filled from source data; report fields needing user choice.
9. Before finishing, update this skill with new ATS observations, failures, and successful tactics. See `references/self-evolution.md`.

## Reference Routing

- Read `references/ats-common.md` for cross-ATS filling rules, user-coordination rules, and validation discipline.
- Read `references/mokahr.md` for Mokahr-specific selectors, dropdown/autocomplete behavior, and known failure modes from ZTE/Sohu applications.
- Read `references/beisen.md` when the page is Beisen or resembles Beisen.
- Read `references/hotjob.md` when the page URL or UI resembles `*.hotjob.cn` old-style resume forms.
- Read `references/role-strategies.md` before choosing which internships/projects/awards to prioritize for a job family.
- Read `references/self-evolution.md` before editing this skill after a real application run.
- Read `references/validation-and-failure-log.md` when a visible value still fails validation or a previous run has similar symptoms.

## Automation Helpers

Optional PowerShell helpers live in `scripts/`. Use them only when they fit the current UI-control approach:

- `scripts/inspect_chrome_uia.ps1`: inspect visible Chrome UI Automation controls.
- `scripts/scan_required_errors.ps1`: list visible required-field validation texts.

These scripts are diagnostic aids, not a substitute for visual verification.
