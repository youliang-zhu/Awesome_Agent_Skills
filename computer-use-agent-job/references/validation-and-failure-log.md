# Validation And Failure Log

Use this file as the append-only, sanitized history of live application-form runs, validation failures, successful recoveries, and rule corrections. Read applicable recent entries before a run and append exactly one structured run record afterward. Keep durable active rules in `ats-common.md` or the matching ATS reference.

## Run Record Contract

Use the `RUN-YYYYMMDD-HHMMSS-<ats>-<company>` template in `self-evolution.md`.

- Always record outcome, difficulties, successful and failed tactics, rule changes, unresolved items, and a privacy check.
- Never record personal field values, credentials, authentication state, private URLs, uploaded files, or full page transcripts.
- Reference stable rule IDs when a run adds, confirms, narrows, corrects, or supersedes guidance.
- If a run yields no reusable lesson, write `Rule changes: none`; the run record is still required.
- Do not rewrite old run records except to correct accidental sensitive data. Record later contradictions in a new run and update the owning rule lifecycle.

## Common Failure Classes

### Visual Value But Required Error Remains

Likely cause: the page requires an internal option id, not text. Try opening the dropdown/autocomplete and clicking the real candidate.

### Candidate List Open But Selection Fails

Likely cause: the page requires a true option click, the menu is not under the expected cursor location, or the user moved the mouse/used the keyboard during computer-use. Pause, obtain a clean input-device handoff, then re-open the field and select the candidate.

### Repeated Section Values Shift

Likely cause: adding an entry inserted a blank item near the viewport or rerendered the section. Re-identify entries by section heading and labels; do not continue with old indices.

### User Uses Mouse Or Keyboard During Computer-Use

Expected behavior: pause safely and wait for exclusive input-device control. Do not continue racing for focus because shared mouse/keyboard use can corrupt dropdown, autocomplete, and text-entry state.

### Required Resume Upload

Boundary: do not upload unless the user explicitly authorizes upload in the current conversation. If upload is mandatory, report it as unresolved.

## Legacy Run Notes

The entries below predate the structured run-record contract. Preserve them as evidence and migrate reusable observations into stable vendor rules when those files are next updated.

### ZTE Mokahr

- Many textareas and spinners accepted UI Automation values.
- Select-like education fields still required true option confirmation.
- GPA score/total fields appeared as spinner controls.
- Some required dropdowns remained red even when values were visible.

### Sohu Mokahr

- Personal-information schema differed from ZTE despite both being Mokahr.
- School and major autocomplete fields required candidate clicks.
- Adding education entries shifted visible cards and caused fixed indices to become unsafe.
- Dropdowns such as gender, highest degree, and intended city could remain invalid after direct value setting.

### 360 Beisen / Phoenix

- Area selector values can appear selected inside the popup but remain `请选择` in the form until the popup-local `确定` button is invoked.
- Full date fields can look like select controls, but the reliable path is to use the calendar popup's `phoenix-calendar-input` with a full `YYYY-MM-DD` value and Enter.
- A successful `暂存` may still leave visible `请选择` placeholders for optional fields such as current residence or internship location; distinguish optional placeholders from required errors before treating them as blockers.

### CGN HotJob

- Context: CGN `cgn.hotjob.cn` old-style resume page.
- Symptom: education `学校` and `专业` can appear as read-only `Edit` controls. Direct `ValuePattern.SetValue`, focus plus paste, clicking, double-clicking, and Enter may not open a picker or update the value.
- Tactic: verify read-only fields before assuming text entry works. If the school/catalog picker does not open, pause and ask the user to manually select the school or provide a page-specific instruction.
- Symptom: English ability may offer only CET-4/CET-6 dropdown options while the source profile only has IELTS.
- Boundary: do not fabricate CET certificate names or scores. Ask the user for a confirmed CET value or permission to leave unresolved.
- Symptom: personal basic information may remain red because the form requires a photo and emergency contact number.
- Boundary: do not upload a photo without explicit current-run authorization; ask for the emergency contact number when absent from the profile source.

### Baidu Campus Recruitment

- Context: Baidu `talent.baidu.com/jobs/resume/edit` resume editor, education and project sections.
- Symptom: school fields are searchable `ComboBox` controls, but offscreen values can be lost when the page virtualizes or rerenders during scrolling. A value may appear in `ValuePattern` briefly yet return to `请选择` after another dropdown action.
- Tactic: handle one visible education card at a time. Bring the card into view, expand the school `ComboBox`, set/search the school name, select the visible candidate from the suggestion list, then verify the same visible card before touching other dropdowns.
- Symptom: repeated education cards may be inserted or left half-filled; adding another card can produce duplicate or blank required records.
- Tactic: before adding education, scan existing cards and fill or delete incomplete duplicates. Avoid broad offscreen batch edits for Baidu education cards.

### TAL / Haoweilai Mokahr

- Context: TAL / 好未来 campus application page on `app.mokahr.com`, role example `算法工程师（27 届校招）`.
- Symptom: the resume parser may prefill education cards, but select fields can show a visible value while the page still displays `必填项未填写`. Direct `ValuePattern.SetValue` or focus-plus-text can change the visual text without committing the internal option id.
- Reliable tactic: for a stale dropdown, focus the `Edit`, press `Ctrl+A`, type the exact visible option text, wait for the candidate layer, then invoke the candidate `Group` whose child `Text` equals the option. Afterward scan for `Edit` controls whose `Name` still contains `必填项未填写` and repeat until the count is zero.
- Coordinate note: on dual-screen/high-DPI setups, mouse coordinates can shift depending on scroll position. Prefer `ScrollItemPattern.ScrollIntoView`, `SetFocus`, keyboard entry, and UIA candidate invocation. If mouse is required, first move the target field to the middle/lower-middle of the viewport and verify by reading the opened candidate list.
- TAL education option mapping observed: `学习形式` -> `全国普通高等院校全日制`; `培养方式` -> `非定向（统招、并轨）`; overseas graduate schools -> `是否为海外院校=是`; domestic undergraduate school -> `否`; English certificate type can be selected as `雅思` for overseas entries and `六级` for SYSU.
- TAL birth date picker accepted only year-month in this run; selecting year `2002` and month `十一月` produced `2002-11 (23岁)` and cleared the date requirement.

### RUN-20260731-215741-custom-oppo

- Date: 2026-07-31
- Company / host: OPPO / careers.oppo.com
- ATS / variant: custom / OPPO university resume editor
- Scope: basic information, education, internships, projects, student leadership, skills, awards, publications, portfolio, patent, and emergency-contact audit
- Outcome: partial
- Difficulties: Education used two confirmation modals; changing a start month beyond the current end was reverted; false national-lab selection hid the lab field; portfolio required an attachment; patent required a publication date.
- Successful tactics: Edited sections through the module edit control; corrected date ranges end-first; matched exchange and degree-granting entries at the same study level; verified saves by waiting for Save to disappear; kept source-missing fields unresolved.
- Failed tactics: Link-only portfolio save; direct hidden lab-field fill; setting project start dates before extending end dates.
- Rule changes: RULE-OPPO-module-edit-save, RULE-OPPO-exchange-education-confirmations, RULE-OPPO-date-range-update-order, RULE-OPPO-hidden-lab-field, RULE-OPPO-required-portfolio-attachment, RULE-OPPO-patent-publication-date
- Unresolved: Existing unsourced identity and language values need user confirmation; internship current-status month, school ranks and one department need confirmation; portfolio attachment, patent publication date, and emergency-contact data are missing.
- Privacy check: no personal values, credentials, attachments, or page transcript
