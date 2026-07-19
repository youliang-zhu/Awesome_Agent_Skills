# ATS Common Rules

## Operating Boundaries

- Never click final submit, preview-submit, withdraw, delete, or upload resume without explicit current-turn authorization.
- Keep the user's profile document as the source of truth. If the page asks for a fact missing from the document and no safe inference exists, ask the user or leave a clear note.
- Prefer semantic labels and nearby section headings over fixed UI Automation indices. Repeated sections and add buttons can shift after every insertion.
- Use visual screenshots plus UI Automation reads for verification. Either one alone can lie.

## User Coordination While Filling

Computer-use requires exclusive control of the shared mouse and keyboard. Before starting live form filling, tell the user not to move the mouse, click, scroll, type, or use keyboard shortcuts until Codex pauses or finishes.

If the user uses the mouse or keyboard during a computer-use run:

1. Pause the live action as soon as it is safe.
2. Wait until the user stops using the input devices and the target Chrome page is active again.
3. Re-check the current field and page state before continuing.
4. Do not attempt to race the user for focus, dropdowns, or cursor position.
5. Stop and ask for a clean handoff if repeated interference makes the page state uncertain.

## Filling Order

1. Text inputs and textareas.
2. Numeric spinners such as GPA score and GPA total.
3. Dates.
4. Dropdowns, cascades, and autocomplete fields.
5. Repeated sections such as education, internship, project, awards.
6. Final required-field scan.

This order reduces the chance that a fragile selector blocks progress on stable fields.

## Field Matching

- Match by visible label, placeholder, aria/name text, nearby section title, and current error message.
- Do not assume that two pages from the same ATS have the same personal-information schema.
- When a field's label is ambiguous, inspect surrounding labels before writing. Example: after gender, one page may ask for ID/ethnicity/political status while another asks for current location/highest degree/school/graduation date.
- For school and major autocomplete fields, type the intended value, wait for suggestions, click the closest candidate, then verify the field value. These actions are especially sensitive to shared mouse/keyboard interference.

## Validation Discipline

- Treat red text such as `必填项未填写` as the page's truth even if a value appears visually.
- After filling dynamic sections, rescan required errors before moving to the next section.
- If setting a value through UI Automation does not clear validation, perform a real user-like selection from the dropdown/candidate menu.
- Keep a short list of unresolved fields with reason: missing source data, uncertain mapping, UI blocked, or explicit user permission needed.
