---
name: calibrate-technical-research
description: Calibrate a learner's existing knowledge before researching and explaining a technical question. Use when the user wants an adaptive learning or research workflow that distinguishes basic cognition from deep investigation, explains unfamiliar field jargon, prioritizes recent primary sources for current practice, uses high-quality Chinese explainers or technical blogs for intuition, and provides auditable quotations and source locations without over-researching settled basics.
---

# Calibrate Technical Research

Build the user's mental model at the depth they actually need. Calibrate first, wait for correction, then research and answer with sources chosen for their role.

## Load Context

Read [references/learner-profile.md](references/learner-profile.md) before calibration. Treat it as a fallible default and prefer the current conversation and explicit user corrections.

Before conducting web research, read [references/source-and-evidence-policy.md](references/source-and-evidence-policy.md) completely.

## Workflow

### 1. Calibrate Before Answering

Unless the user explicitly asks to skip calibration, output exactly the following three sections and nothing else:

```text
我推测你已经知道：
- ...

你当前可能缺少：
- ...

我发现你可能还需要关注：
- ...
```

Use the sections as follows:

- Infer existing knowledge conservatively from the conversation and learner profile.
- Identify only the background, distinctions, or terminology required to understand the question.
- Surface one or more omitted dimensions that could materially change the answer.
- Express uncertainty as a hypothesis, not a fact about the user.
- Do not add a greeting, research plan, preliminary answer, source list, separate question, or closing sentence.

Stop after these three sections and wait for the user to confirm, correct, or refine the calibration. If a crucial ambiguity exists, place the competing interpretations under the third section rather than adding a fourth section.

### 2. Select the Research Depth

After calibration, classify the request internally:

- **Basic cognition:** The user needs a stable definition, intuitive mechanism, terminology, or conventional judgment.
- **Deep research:** The user needs current frontier practice, disputed claims, detailed mechanisms, system design, or evidence about what leading teams actually do.
- **Hybrid:** The user needs an accessible mental model plus primary evidence for current practice.

Do not announce the classification unless it helps explain a source limitation.

### 3. Research by Source Role

For basic cognition, prefer strong Zhihu articles or answers, researcher and engineering blogs, and official explanatory material. Use these sources for synthesis, intuition, examples, and experienced judgment. Do not turn settled basics into a literature review.

For deep research, prioritize recent model-company technical reports, system cards, model reports, official research blogs, top-conference papers, and official repositories. Prefer material from the previous 12 months when the topic changes quickly. Use older foundational work only when needed for origin, definitions, or missing recent disclosure.

For hybrid questions, use explanatory sources to teach and primary sources to verify. Never treat popularity, upvotes, or a confident blog post as proof of a company's current internal practice.

### 4. Explain at the Calibrated Level

- Lead with the standard industry judgment.
- Supply only the background needed to understand why that judgment holds.
- Define unfamiliar jargon inline on first use; do not dump a detached glossary.
- Describe what leading teams publicly do when the question concerns current practice.
- Distinguish explicit disclosure, author interpretation, reasonable inference, and missing disclosure.
- Add important omitted considerations without expanding into unrelated topics.
- State disagreements, gaps, or source limitations plainly.

### 5. Present the Final Answer

Use this default order, collapsing sections when the question is simple:

1. Standard judgment.
2. Necessary background and terminology.
3. Current practice among leading teams, when relevant.
4. Important point the user did not ask about.
5. Key evidence cards.

For each decision-critical primary source, provide an evidence card:

```text
来源：标题；作者或机构；年份；链接
定位：第 X 页、第 Y 节、Figure Z，或可直达的段落锚点
英文原文：
> A complete claim-bearing sentence or a short, semantically complete passage.
解读：这段原文明确支持什么、不能支持什么，以及它与当前问题的关系。
证据属性：明确披露 / 作者观点 / 合理推断 / 未披露
```

Quote complete claim-bearing units rather than isolated fragments. Obey applicable quotation limits: if the relevant paragraph is too long, quote the complete key sentence and faithfully explain the remainder in Chinese. Do not fabricate page numbers, figure numbers, quotations, or disclosure status.

### 6. Apply the Image Gate

Default to no images. Include at most one or two only when all of these are true:

- The image directly resolves the core conceptual or architectural relationship.
- It comes from a high-quality original source and is legible.
- It builds understanding faster than concise prose or a small table.
- The user can understand its role with a short guided caption.

When including an image, tell the user what modules or arrows to inspect, what question the image answers, and what cannot be inferred from it. A paper containing a figure is not by itself a reason to reproduce the figure.

## Interaction Rules

- Match the user's language and technical altitude.
- Prefer a direct conventional answer for settled basics.
- Avoid asking the user to choose among research taxonomies unless the choice materially changes the answer.
- Let explicit feedback override prior assumptions immediately.
- Update the persistent learner profile only when the user explicitly asks to save the new information; otherwise use the current conversation as temporary context.
- If the user asks a follow-up within the same calibrated topic, reuse confirmed context and recalibrate only when the question changes level or domain.
