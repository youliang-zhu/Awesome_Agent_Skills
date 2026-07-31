# OPPO University Resume Editor

Use for the company-hosted resume editor on `careers.oppo.com`. Verify the host and visible OPPO university-recruiting resume structure before applying these rules.

### RULE-OPPO-module-edit-save

- Status: provisional
- Applies when: a collapsed resume section exposes the module edit control and becomes a multi-entry form.
- Does not apply when: the section is already in edit mode or uses a separate navigation page.
- Symptom: summary sections do not expose per-entry edit buttons; saving may complete asynchronously.
- Tactic: open the section, invoke its module edit control, edit all repeated entries in one form, click `保存`, and wait for the visible Save button to disappear before treating the section as saved.
- Verification: the section returns to summary mode and displays the updated entries.
- Evidence: RUN-20260731-215741-custom-oppo
- Last reviewed: 2026-07-31
- Supersedes: none

### RULE-OPPO-exchange-education-confirmations

- Status: provisional
- Applies when: an education entry is marked as exchange study and a non-exchange entry represents the degree-granting program.
- Does not apply when: no exchange entry is present.
- Symptom: saving education can show an exchange-study information prompt followed by a separate final save confirmation.
- Tactic: use the same study level for the exchange and degree-granting entries, distinguish them with `该学历是否为交流学习`, accept the exchange-study information prompt, then confirm the final `保存前请确认以上经历` dialog. If the form remains open after the first prompt, invoke Save again before the final confirmation.
- Verification: the Save button disappears and the summary identifies the exchange entry as `是` and the degree-granting entry as `否`.
- Evidence: RUN-20260731-215741-custom-oppo
- Last reviewed: 2026-07-31
- Supersedes: none

### RULE-OPPO-date-range-update-order

- Status: provisional
- Applies when: changing a start month would temporarily place it after the entry's current end month.
- Does not apply when: the new start month is not later than the current end month.
- Symptom: selecting the new start month appears to succeed but the input keeps its previous value.
- Tactic: extend or correct the end month first, verify it, then change the start month and verify the complete range before saving.
- Verification: both date inputs show the intended range before Save and the same range appears in summary mode.
- Evidence: RUN-20260731-215741-custom-oppo
- Last reviewed: 2026-07-31
- Supersedes: none

### RULE-OPPO-hidden-lab-field

- Status: provisional
- Applies when: `是否国家重点实验室` is set to `否`.
- Does not apply when: the page visibly keeps the laboratory input enabled after selecting `否`.
- Symptom: an `所在实验室` input remains in the DOM but is hidden and cannot be filled.
- Tactic: keep the truthful `否` selection; do not switch to `是` merely to expose the laboratory field. Report the laboratory name as unfillable under this schema.
- Verification: summary mode shows `是否国家重点实验室：否` and leaves `所在实验室` blank.
- Evidence: RUN-20260731-215741-custom-oppo
- Last reviewed: 2026-07-31
- Supersedes: none

### RULE-OPPO-required-portfolio-attachment

- Status: provisional
- Applies when: the `作品` section displays both a required link field and a required attachment uploader.
- Does not apply when: the attachment control is optional or an authorized attachment is already present.
- Symptom: link-only Save keeps the form open and reports that a portfolio attachment is required.
- Tactic: do not upload an arbitrary file. Keep the section unresolved until the user authorizes a specific portfolio attachment.
- Verification: the form's visible validation explicitly identifies the attachment requirement.
- Evidence: RUN-20260731-215741-custom-oppo
- Last reviewed: 2026-07-31
- Supersedes: none

### RULE-OPPO-patent-publication-date

- Status: provisional
- Applies when: the patent section requires `发布时间` but the source only proves application or acceptance.
- Does not apply when: an authoritative publication date is available.
- Symptom: the form cannot represent an accepted-but-not-published patent without supplying a publication date.
- Tactic: do not substitute the application or acceptance date for publication. Leave the patent section unresolved and request an authoritative publication date.
- Verification: no unsupported patent publication claim is saved.
- Evidence: RUN-20260731-215741-custom-oppo
- Last reviewed: 2026-07-31
- Supersedes: none
