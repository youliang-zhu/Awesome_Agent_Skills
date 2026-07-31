# Feishu Recruitment Reference

Use this reference only when visible branding, host metadata, or page assets identify Feishu Recruitment. A company-hosted page can customize its schema, so record the host and observable variant in every run.

## Current Evidence Status

Feishu-specific behavior has been observed on a Xiaomi-hosted `jobs.f.mioffice.cn` resume editor. The rules below remain `provisional` until independently reproduced under matching preconditions.

## Run Strategy

- Inventory the visible sections, save/draft controls, required markers, and final-submit control before filling.
- Fill and verify one repeated education, internship, project, award, or language card at a time.
- Distinguish plain text fields from candidate-backed, cascading, date, upload, and rich-text controls.
- Use the page's validation state, persisted draft state, or reopened saved value as the success signal; visible text alone is insufficient.
- Record company-only field order or wording in the run log. Promote it here only when the observable preconditions are reusable.

## Verified Rules

### RULE-FEISHU-parser-section-bleed

- Status: provisional
- Applies when: a Feishu/Mioffice resume editor has created repeated cards from an uploaded resume and the parsed content is visible for review
- Does not apply when: the form was entered manually or the parser output has already been independently audited
- Symptom: adjacent resume sections can be concatenated into one description, and a project or competition can appear under internship experience
- Tactic: inventory every repeated education, internship, and project card before editing; remove misclassified cards and split concatenated content into the correct sections before adding new entries
- Verification: each card contains only the source-backed organization, role, dates, and description for that section
- Evidence: RUN-20260731-220944-feishu-xiaomi
- Last reviewed: 2026-07-31
- Supersedes: none

### RULE-FEISHU-active-month-dropdown

- Status: provisional
- Applies when: a Feishu/Mioffice month-period picker renders multiple date dropdowns in the DOM and only one lacks the hidden-dropdown class
- Does not apply when: the form uses a native date input, a day-level calendar, or only one date panel exists
- Symptom: unscoped year or month locators match several hidden historical panels and cannot identify the active option reliably
- Tactic: open the exact card's begin or end control, then scope year, month, or present-time option clicks to the non-hidden date dropdown; re-read the card's displayed period after each endpoint
- Verification: the same repeated card displays the intended start and end months or the explicit present-time label
- Evidence: RUN-20260731-220944-feishu-xiaomi
- Last reviewed: 2026-07-31
- Supersedes: none

### RULE-FEISHU-company-required-schema

- Status: provisional
- Applies when: a Feishu/Mioffice customer form marks company-configured education fields required and exposes one whole-form Save control
- Does not apply when: the page provides per-section saves or the fields are optional in the visible schema
- Symptom: Save keeps the editor open and reveals inline errors for blank company-specific fields even when the source profile intentionally leaves them empty
- Tactic: trigger Save once after filling all source-backed values, treat the resulting inline errors as authoritative, and leave source-missing or explicitly blank fields unresolved instead of inventing placeholders
- Verification: either the editor reports no inline errors and persists, or every remaining inline error is mapped to a documented source-data gap
- Evidence: RUN-20260731-220944-feishu-xiaomi
- Last reviewed: 2026-07-31
- Supersedes: none
