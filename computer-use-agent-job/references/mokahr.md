# Mokahr Reference

## Identification

Use this reference when the URL or page content contains `mokahr`, `moka`, `app.mokahr.com`, or the page layout resembles Mokahr campus recruitment forms.

## High-Value Lessons

- Mokahr fields can display a value while still failing validation. `ValuePattern.SetValue()` is often insufficient for selects, cascades, and autocomplete fields.
- Dropdowns and autocomplete fields must usually be confirmed by clicking an actual candidate option.
- Adding repeated entries can insert blank cards near the current viewport and shift control order. Fill and verify one entry before adding the next.
- Do not rely on fixed edit/control indices after scrolling or adding entries.
- `ScrollItemPattern.ScrollIntoView()` is useful for hidden controls, but visual verification is still required.
- GPA fields may appear as `Spinner` controls rather than `Edit` controls.

## Section Strategy

### Personal Information

Read labels every time. Different Mokahr customers can use different schemas in the same visual layout. For example, one application may ask for ID number, ethnicity, and political status after gender; another may ask for current location, highest degree, highest-degree school, and graduation time.

### Education

Fill one education entry fully before adding another. For school and major:

1. Type the source value.
2. Wait for candidate suggestions.
3. Click the closest official candidate.
4. Verify visible text and required-error state.

Use the profile document's common education rules for degree type, study mode, highest-degree flag, lab, mentor, research direction, rank, GPA, and GPA total.

### Internships and Projects

Prefer textarea `ValuePattern` or paste for descriptions, then verify line breaks and section placement. If only a limited number of projects is accepted, follow `references/role-strategies.md`.

### Awards and Skills

Fill stable award name/time/level fields first. If proof upload is optional, do not upload unless asked. For skills, prefer compact keyword lists with mastery level if required.

## Known Mokahr Failures

- Visible select values such as gender, highest degree, intended city, education type, study mode, highest-degree flag, and rank may remain red until an option is truly selected.
- Candidate menus may fail if the user moves the mouse or uses the keyboard during selection. Computer-use needs exclusive mouse/keyboard control for Mokahr dropdowns and autocomplete menus.
- School/major autocomplete may visually show a typed value but internally remain unconfirmed.
- Required resume upload may block final validation. Do not upload unless current-turn permission is explicit.

## Previously Observed Applications

- ZTE Mokahr: field values could be set through UI Automation for many text fields and spinners, but several education dropdowns remained invalid until true option selection.
- Sohu Mokahr: same ATS but different personal-information schema. Some dropdowns and autocomplete education fields required visual candidate selection; adding education entries shifted blank cards and made fixed-index filling unreliable.
