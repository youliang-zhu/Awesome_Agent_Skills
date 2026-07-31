# CMBNT Resume Center Reference

Use this reference for the company-hosted resume editor on `cmbnt.cmbchina.com`. The observed implementation is a React and Ant Design style form with one whole-page draft action and a separate final submit action. Keep all rules `provisional` until independently reproduced.

## Run Strategy

- Audit parser-created repeated cards before adding new ones; project descriptions can be present while their required project-name fields remain blank.
- Prefer the `暂存` action for progress preservation. Never use `提交` without explicit current-turn authorization.
- Keep source-missing required fields blank and record them; this variant can preserve a draft without completing every required section.

## Verified Rules

### RULE-CMBNT-parser-blank-project-names

- Status: provisional
- Applies when: the CMBNT resume parser has populated project cards from an attachment
- Does not apply when: project cards were entered manually or already audited
- Symptom: project organizations, dates, and descriptions are populated while project-name fields remain empty
- Tactic: inventory every parsed project card, map each description to its source-backed project, and fill the project name before editing or adding other cards
- Verification: every retained project card has a name consistent with its organization, dates, and description
- Evidence: RUN-20260731-223111-custom-cmbnt
- Last reviewed: 2026-07-31
- Supersedes: none

### RULE-CMBNT-special-character-draft-validation

- Status: provisional
- Applies when: CMBNT draft save reports that company name, organization, or project description contains special characters
- Does not apply when: draft save succeeds or the page identifies a different invalid field
- Symptom: `暂存` is rejected with a combined special-character message; values may contain punctuation such as ampersands, slashes, or plus signs
- Tactic: replace nonessential symbolic separators with equivalent Chinese words or punctuation, preserve technical meaning, then retry `暂存`
- Verification: the page displays the authoritative `暂存成功` message
- Evidence: RUN-20260731-223111-custom-cmbnt
- Last reviewed: 2026-07-31
- Supersedes: none

### RULE-CMBNT-draft-allows-incomplete-required-sections

- Status: provisional
- Applies when: CMBNT shows separate `暂存` and `提交` actions and required sections still contain source-missing values
- Does not apply when: the user explicitly authorizes final submission or the page has no draft action
- Symptom: required basic, language, job-intention, or family fields remain incomplete, but known resume sections are ready to preserve
- Tactic: use `暂存`, never `提交`, and report the remaining source-data gaps after the success signal
- Verification: the page displays `暂存成功` while the final-submit control remains untouched
- Evidence: RUN-20260731-223111-custom-cmbnt
- Last reviewed: 2026-07-31
- Supersedes: none

### RULE-CMBNT-readonly-award-date-picker

- Status: provisional
- Applies when: an award date input is read-only and opens the Ant Design calendar
- Does not apply when: the date field accepts direct text input
- Symptom: direct fill fails even though the input is enabled
- Tactic: open the date picker, select the year, select the month, then select the day; verify the resulting full date in the same award card
- Verification: the award card displays the intended `YYYY-MM-DD` value and the draft later succeeds
- Evidence: RUN-20260731-223111-custom-cmbnt
- Last reviewed: 2026-07-31
- Supersedes: none
