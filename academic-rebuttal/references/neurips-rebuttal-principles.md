# NeurIPS Rebuttal Principles

Read this document before analyzing, planning, drafting, revising, or
quality-checking a rebuttal. Use it as an AC-first strategy layer on top of the
main skill workflow.

## Core Framing: Rebuttal Is Not Revision

A rebuttal is a limited decision-influencing response, not a promise to revise
everything. Do not answer every request with unconditional agreement or a long
list of future changes. Especially when scores are uniformly weak, repeated
"yes, we will add this" responses can reinforce the impression that the submitted
paper is incomplete.

Prioritize the few concerns that determine whether the paper's current central
claim is credible. Distinguish:

- evidence or clarification that resolves a decision-critical concern now;
- a concrete presentation change that makes existing substance easier to verify;
- longer-horizon revision work that should not be presented as necessary for the
  paper's present validity.

## 1. Write for the AC, Not Only the Reviewer

The immediate addressee is the reviewer, but the decisive reader may be the Area
Chair. Optimize every major response for two questions:

1. Has the reviewer's underlying doubt been resolved?
2. Can the AC see that the remaining issue is bounded and fixable rather than a
   fundamental failure of the paper?

Make the paper's strongest defensible contribution, evidence, and scope legible
to a neutral decision-maker. Do not assume that a reviewer score increase alone
guarantees acceptance.

## 2. Lead with the Conclusion, Then Evidence, Then Revision

Whenever possible, answer the core question in the first sentence. Give the AC a
clear conclusion before explanation.

Use:

1. **Direct answer:** one sentence stating the conclusion.
2. **Evidence:** exact results, controls, equations, figures, tables, sections, or
   verified manuscript locations.
3. **Revision:** the precise wording, figure, table, or explanation that will
   change.

Do not bury the answer under background, ceremonial thanks, or several paragraphs
of theory. Theory without verifiable support is not a substitute for evidence.

## 3. Concede Presentation Issues Carefully; Do Not Invent Away Fundamental Ones

When the underlying method and evidence are sound but the exposition caused
confusion, explicitly own the presentation problem and state the exact fix.

Do not casually characterize a criticism as a fundamental flaw. First determine
whether it is actually:

- an unclear assumption;
- a missing pointer to existing evidence;
- an overly broad claim that can be narrowed;
- a scope mismatch;
- an incomplete explanation of controls or protocol.

However, never conceal a real correctness problem, data issue, invalid evaluation,
or unsupported central claim. If a fundamental issue is real, respond truthfully,
narrow the claim where possible, and assess whether rebuttal or resubmission has
the higher expected value.

## 4. Be Firm Without Becoming Combative

Correct factual errors directly and confidently, but keep the public response
professional. Do not insult the reviewer, speculate about intent, or accuse them
of not reading.

For an unusually problematic review:

- quote only the necessary text;
- identify the factual or process issue precisely;
- provide documentary evidence;
- explain its consequence for fair evaluation;
- use a confidential AC/chair channel when the venue provides one.

A sharp response should make the error obvious through evidence, not through
hostile language.

## 5. Define Novelty at the Contribution Level

When a reviewer says individual components already exist, do not rely on claiming
that each module is unprecedented. Reconstruct novelty around the paper's
contribution:

- the new architecture or formulation;
- the capability enabled by the integration;
- the assumptions removed or relaxed;
- the mechanism or guarantee introduced;
- the empirical or analytical finding made possible;
- why these differences matter in the target setting.

Use a delta comparison against the closest prior work. Explain how the
architecture makes known elements work differently or better, rather than merely
calling the combination novel.

## 6. Add Experiments Selectively

Do not add experiments merely to demonstrate effort. Add an experiment during the
rebuttal period only when it is decision-critical, feasible, controlled, and
interpretable.

Experiments are often justified when a central claim lacks direct support,
including:

- parameter sensitivity essential to the claim;
- computational complexity or matched-cost analysis;
- a missing decisive baseline;
- a central ablation;
- statistical reliability needed to interpret the reported gain.

Be cautious with requests for entirely new experiment types or evaluation regimes
that were absent from the original comparison framework. First determine whether
the request is outside the paper's intended scope. Prefer existing evidence,
clarification, or claim narrowing when these answer the underlying concern.

For every proposed experiment, state:

- which concern it resolves;
- the minimum viable protocol and controls;
- the result needed to support the claim;
- what a negative or inconclusive result would mean;
- the fallback response if it cannot be completed reliably.

## 7. Use Scope Before Blanket Defense

When a reviewer evaluates the paper under a different imagined deployment,
dataset, task, or goal, bring the discussion back to the paper's intended
setting.

State:

- the exact target scenario;
- the claim made within that scenario;
- why the evaluation matches it;
- which broader scenarios are not claimed;
- what limitation or scope sentence will be clarified.

Do not claim universal validity simply to satisfy a request. A narrow, supported
claim is stronger than a broad, weakly defended one.

## 8. Treat Genuine Misunderstandings as Presentation Signals

When the manuscript supports the authors' interpretation but the reviewer
misunderstood it, write:

1. the correct interpretation;
2. the existing manuscript evidence;
3. how the current presentation allowed the misunderstanding;
4. the exact clarification to be added.

Prefer language such as "our presentation may have obscured this distinction."
Do not automatically label every disagreement a misunderstanding. Verify the
paper actually contains the claimed support and flag missing locations.

## 9. Make Resolvability Visible to the AC

The overall rebuttal should make it easy for the AC to audit that:

- central technical concerns have direct answers;
- claims are linked to supplied evidence;
- fair-comparison and reliability controls are explicit;
- novelty is distinguished from the closest prior work;
- scope is bounded and defensible;
- presentation fixes are concrete;
- remaining limitations do not invalidate the central contribution.

Order the response by decision impact rather than reviewer order when the venue
format permits. Merge shared concerns, emphasize resolved major issues, and group
minor fixes compactly.

## Final AC-First Check

Before returning any rebuttal draft, verify:

- Does each major section begin with a conclusion?
- Can every empirical or manuscript claim be traced to verified evidence?
- Does the response distinguish a fixable presentation issue from a real
  substantive limitation?
- Is novelty defined through contribution and capability rather than isolated
  components?
- Are requested experiments truly necessary for the decision?
- Is scope used honestly instead of making unsupported universal claims?
- Is the tone calm enough that a neutral AC can trust it?
- Does the full response make the paper look auditable and the remaining work
  bounded?

These principles do not override evidence integrity or venue rules. Never invent
results, manuscript locations, citations, reviewer intent, or completed work.
