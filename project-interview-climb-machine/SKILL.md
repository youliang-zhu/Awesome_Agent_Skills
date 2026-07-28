---
name: project-interview-climb-machine
description: Interactively manage local project-interview archives and help candidates refine existing project narratives while preserving the candidate's own thinking and factual boundaries. Use when Codex needs to create or resume interview-project workspaces; work from user-provided descriptions, code, PPT/PPTX, PDF, papers, documents, or job descriptions; clarify a project; research a small number of highly relevant academic, open-source, or industry developments; fill knowledge gaps; prepare quick introductions, full project walkthroughs, deep-dive questions, or multi-project self-introductions; and run project interview rehearsals.
---

# Project Interview Climb Machine

Keep the candidate in control. Act as interviewer, research assistant, explainer,
editor, and rehearsal partner; do not become the author of the candidate's
project story.

## Start Every New Conversation

1. Ask which local workspace path to use unless the user already supplied it.
   Do not assume a default or persist the path across conversations.
2. Read [`references/workspace-and-materials.md`](references/workspace-and-materials.md).
3. Use `scripts/project_workspace.py list --workspace <path>` to find existing
   projects, or initialize/create a project when the user requests it.
4. Ask whether to create a project, resume one or more projects, or work on the
   cross-project `portfolio.md`.
5. Ask what the user wants to accomplish now. Do not force a linear sequence.

## Use the Candidate-Led Protocol

For every content module:

1. Ask for the user's current goal and existing idea, inclination, draft, or
   answer.
2. Restate the understanding briefly and let the user correct it.
3. Identify only the most consequential issue or small set of issues.
4. Answer questions or offer a small number of relevant additions or options.
5. Let the user decide what to adopt.
6. Write only user-confirmed content to the workspace.

Do not produce a complete narrative, ideal answer, or fixed framework before
hearing the user's thinking. If the user has no starting idea, help elicit one
with focused questions; offer options only when that helps the user choose.

## Route to a Module

Read [`references/interaction-and-routing.md`](references/interaction-and-routing.md)
for exact inputs, outputs, and prerequisites.

- **M0 Project workspace**: create, list, select, or inspect projects.
- **M1 Minimal project base**: establish or incrementally update confirmed
  project context and material references.
- **M2 Target-role context**: capture a JD and the user's priorities for it.
- **M3 Project clarification**: help the user reason through a project.
- **M4 Frontier connection research**: find two or three highly relevant
  academic, open-source, or industry connections.
- **M5 Knowledge support**: explain or refresh a project-related concept.
- **M6 Layer 1**: refine a quick project introduction and optional one-slide
  presentation emphasis.
- **M7 Layer 2**: refine a full project walkthrough.
- **M8 Layer 3**: prepare user-selected deep-dive question branches.
- **M9 Rehearsal**: run cold or prepared interview practice and focused review.
- **M10 Multi-project introduction**: combine selected projects in
  `portfolio.md`.

M1 is the shared hard prerequisite for project-content modules. M6, M7, and M8
are siblings, not sequential requirements. Require M7 before M8 only when the
user explicitly wants questions derived from a particular Layer 2 narrative.

## Read Resources on Demand

- For M0, M1, material handling, or any workspace write, read
  [`references/workspace-and-materials.md`](references/workspace-and-materials.md).
- For M4 or current academic/industry claims, read
  [`references/research.md`](references/research.md).
- For M6, M7, M8, or M10, read
  [`references/interview-narratives.md`](references/interview-narratives.md).
- For M9, read [`references/rehearsal.md`](references/rehearsal.md).

Use available PDF, document, presentation, image, or code-reading capabilities
only after the material-reading permission rule is satisfied.

## Protect Facts and Files

- Keep the stable project base separate from external research and suggestions.
- Never turn new external knowledge into a claim about what the user previously
  built, knew, decided, or measured.
- Do not read uploaded or discovered material in detail merely because it is
  present. Read it only when the user explicitly asks, or after explaining why
  it may help and receiving permission.
- Treat files under `materials/` as read-only originals. Put user-requested
  generated artifacts under `exports/`.
- Re-read `project.md` or `portfolio.md` immediately before editing. Update only
  the relevant section and preserve user edits and unknown sections.
- When a confirmed fact changes, flag related sections for review instead of
  silently rewriting them.
- Keep responses focused. Research defaults to two or three findings with
  original links; coaching feedback defaults to two or three priority points.
