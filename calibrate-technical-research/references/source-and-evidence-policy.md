# Source and Evidence Policy

## Separate Explanation From Verification

Assign every source one or both roles:

- **Explanatory source:** Builds intuition, supplies terminology, examples, or experienced synthesis.
- **Evidentiary source:** Supports a factual claim about a method, result, system, organization, or current practice.

Use Zhihu and technical blogs freely as explanatory sources when they are unusually clear. Verify consequential or time-sensitive claims with primary evidence.

## Route Basic-Cognition Questions

Prefer, in order:

1. High-quality Zhihu articles or answers by identifiable researchers or experienced practitioners.
2. Technical blogs from research groups, engineering teams, or respected practitioners.
3. Official tutorials, documentation, or educational material.
4. Primary papers when a definition is disputed or the explanation needs verification.

Assess explanatory quality using substance rather than popularity alone:

- Does the author show relevant expertise or primary-source familiarity?
- Does the explanation distinguish commonly confused concepts?
- Are examples, diagrams, code, or citations technically consistent?
- Do independent sources converge on the same stable judgment?

Label personal experience and judgment as such. Do not present it as universal industry practice.

## Route Deep-Research Questions

Prefer, in order:

1. Model-company technical reports, model cards, system cards, and official research publications.
2. Papers from leading research teams and top conferences.
3. Official repositories, documentation, and technical presentations.
4. Older foundational papers for history, definitions, or concepts omitted by recent sources.
5. Secondary commentary only to discover terminology, disagreements, or additional primary sources.

For fast-moving areas, search the previous 12 months first. Expand backward only when recent primary evidence is absent or foundational context is necessary, and explain the reason.

Never use a paper's recency as a substitute for relevance or quality. Prefer a slightly older direct disclosure over a new paper that only mentions the topic indirectly.

## Investigate Current Company Practice

Ask of every claimed practice:

1. Does the source explicitly say the team used it?
2. Is it a general proposal rather than a deployment disclosure?
3. Is the claim about one training run, one product, or a broad organizational standard?
4. Is the behavior directly stated, implied by an architecture, or merely technically possible?
5. Could the absence of detail reflect non-disclosure rather than non-use?

Use these evidence labels consistently:

- **明确披露:** The primary source directly states the claim.
- **作者观点:** The source argues or recommends it but does not establish broad adoption.
- **合理推断:** Multiple disclosed facts support the inference, but the source does not state it directly.
- **未披露:** Public material does not answer the question. Never rewrite this as “没有使用”.

## Build Evidence Cards

Include evidence cards only for claims central to the answer. Two to four strong cards are usually better than a long bibliography.

Each card must contain:

- A direct link to the original source, not a search-results page.
- A precise locator: PDF page, section, figure, table, appendix, or stable HTML heading.
- A complete claim-bearing English sentence or a short semantically complete passage when the source is English.
- A Chinese interpretation explaining both the support and the boundary of the evidence.
- One evidence label.

Keep source quotations within applicable copyright limits. Never stitch separated fragments together as though they were continuous prose. Use ellipses only when omission does not change meaning.

## Select Images Sparingly

Use zero images by default. An image qualifies only if it is authoritative, readable, directly relevant, and more efficient than prose.

Strong candidates include:

- A system diagram that locates the component being discussed among at least three interacting modules.
- A training or deployment diagram that distinguishes two easily confused update paths.
- A result figure that directly supports a central comparison and has legible axes and conditions.

Reject decorative overview images, crowded figures requiring extensive reconstruction, redundant screenshots, and figures whose main point can be stated in one sentence.

When a figure is useful but reproduction would add reading burden, cite its number and page without embedding it.

## Resolve Conflicts

When sources disagree:

- Check whether they discuss different definitions, stages, model generations, or deployment settings.
- Prefer direct first-party disclosure for what a team did.
- Prefer controlled peer-reviewed evidence for comparative scientific claims.
- Present unresolved disagreement instead of forcing a false consensus.

When no primary source answers the question, state the gap and offer the best bounded inference separately.
