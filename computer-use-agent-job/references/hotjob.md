# HotJob / CGN-Style Forms

Use this reference for old-style HotJob pages such as CGN `cgn.hotjob.cn` resume forms.

## Page Shape

- The resume is a long single page with left-side section status indicators and repeated local `保存 / 修改 / 删除` links.
- Section save links may remain in the UI Automation tree even when slightly outside the viewport. Prefer invoking the section-local `保存` link whose JavaScript value matches the current section id, and verify the left-side status icon afterward.
- Red validation messages may remain visible until the section is saved. Treat the left-side green/red status and post-save inline errors as the final signal.
- Do not click `完成` unless the user explicitly authorizes final completion or submission behavior for that run.

## Filling Tactics

- Textareas in personal-experience sections accept UI Automation `ValuePattern.SetValue`; use compact paragraphs to avoid long-field truncation.
- The `个人经历` section may not have separate internship/project cards. Map content as follows:
  - `科研项目经历` gets the role-strategy projects, usually Agent Memory, Apertus, and GUI Agent.
  - `社会实践及实习经历` gets internships, usually Swiss AI & EPFL first, then Volvo.
  - `在校期间获奖情况` gets scholarships and competition awards.
  - `个人兴趣爱好及特长` gets profile hobbies.
  - `是否受过处分` should be `否` when the profile has no disciplinary record.
- `求职意向` may ask for broad job categories rather than the exact job. For Agent/algorithm roles, choose `设计研发类` when no AI-specific option exists. If salary has no `面议`, choose a conservative role-appropriate range and report the assumption.

## Known Blockers

- Some education fields, especially `学校` and `专业`, can be read-only catalog-backed fields. Direct UIA value setting and keyboard paste can leave the visible value unchanged or fail validation. If clicking the field does not open a picker, stop and ask the user to select the catalog entry manually.
- Overseas schools may not be selectable by plain text. After saving, verify that the school field is not blank and that the left-side `教育经历` status turns green.
- English ability may expose only CET-4/CET-6 options. Do not invent CET scores from IELTS. Ask the user whether to leave it blank, map IELTS to a note elsewhere, or provide a confirmed CET certificate and score.
- Personal information may require a photo and emergency contact number even when the profile source does not contain them. Photo upload requires explicit user authorization for that exact run.
