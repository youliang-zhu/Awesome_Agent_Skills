# Interaction and Module Routing

## Universal protocol

Run every content module as a user-led conversation:

1. Ask what the user wants from this module now.
2. Ask for the user's current idea, inclination, draft, question, or answer.
3. Restate the understanding briefly and let the user correct it.
4. Focus on the most consequential issue or small set of issues.
5. Supplement, explain, or offer limited options without taking ownership.
6. Let the user decide.
7. Persist only confirmed results.

Avoid a large intake questionnaire. Ask only for information that blocks the
current task. Do not force the user through modules that are merely helpful.

## Prerequisite types

- **Hard**: do not enter the module without it.
- **Conditional**: require it only for the requested variant.
- **Optional**: offer it when useful; do not force it.

## M0 — Project workspace

Input: user-specified workspace path and create/resume/multi-project intent.

Output: active project(s) or `portfolio.md`, a short state summary, and the
user's selected next module.

Prerequisite: none. Ask for the path once per conversation.

## M1 — Minimal project base

Input: any project description the user wants to provide, permitted materials,
and user corrections.

Output: a concise confirmed base, material references, and only genuinely
blocking unknowns.

Hard prerequisite: M0.

Allow a one-sentence initial base. Expand it only as later work requires.

## M2 — Target-role context

Input: JD, role/company context, and the user's own priorities or interpretation.

Output: a concise role context, two or three priority signals, and
user-confirmed emphasis.

Hard prerequisite: M0. Require M1 only when relating the role to a project.
Store multiple roles as sections of the same project document or `portfolio.md`.

## M3 — Project clarification

Input: M1, the user's current understanding, and the issue they want to untangle.

Output: user-confirmed understanding, clarified relationships, remaining
questions, and optional confirmed updates to M1.

Hard prerequisite: M1. M3 is not required before M6–M8.

## M4 — Frontier connection research

Input: M1, the user's research angle, academic/industry/both scope, and optional
M2 context.

Output: two or three highly relevant findings, original links, concise
relevance, and one possible thought direction per finding.

Hard prerequisite: M1. M2 is optional. Do not merge results into a narrative
without the user's choice.

## M5 — Knowledge support

Input: M1, a user-selected concept or forgotten point, desired depth, and
optional sources.

Output: a focused explanation, its direct project connection, necessary
original sources, and the user's remaining question or confirmed takeaway.

Hard prerequisite: M1. M4 is conditional when current claims are required.

## M6 — Layer 1: quick introduction

Input: M1, the user's current approach, desired first impression, time limit,
and optional slide, M2, M4, or M5 context.

Output: user-confirmed introduction approach, optional short wording, one-slide
emphasis, and natural hooks for follow-up.

Hard prerequisite: M1. M2–M5 are optional. M7 and M8 are not prerequisites.

## M7 — Layer 2: full walkthrough

Input: M1, the user's outline or natural narration, desired emphasis and time,
plus optional M2, M4, or M5 context.

Output: user-confirmed narrative line, ordering and emphasis changes, issues to
clarify, and a full script only when requested.

Hard prerequisite: M1. M6 is not required.

## M8 — Layer 3: deep-dive preparation

Input: M1, user-selected concerns or likely topics, the user's current answers,
and optional M2, M4, M5, or M7 context.

Output: question branches, why they may be asked, focused corrections or
supplements to the user's answers, confirmed answer points, and possible
follow-ups.

Hard prerequisite: M1. M7 is conditional only when deriving questions from a
particular full walkthrough.

## M9 — Rehearsal and review

Input: M1, cold/Layer 1/Layer 2/Layer 3 mode, optional prepared content, and the
user's preferred interviewer direction, depth, and feedback cadence.

Output: rehearsal record, two or three priority improvements, user-approved
changes, and optional updates to the relevant section.

Hard prerequisite: M1 for a cold run. M6, M7, or M8 is conditional for rehearsal
of an existing version.

## M10 — Multi-project introduction

Input: selected projects with M1, the user's current ordering and time idea, and
optional M2 or M6 content.

Output: user-confirmed selection/order, time and emphasis, transitions, and
projects that need M6 revision.

Hard prerequisites: M0 and M1 for every selected project. Store the result in
`portfolio.md`, not in any one project's `project.md`.
