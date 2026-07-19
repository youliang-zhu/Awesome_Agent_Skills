# {{PROJECT_NAME}} Architecture (current state)

Single source of truth for how the project is built **today**. Direction and
boundaries live in [`../idea/idea.md`](../idea/idea.md). Historical planning and
superseded designs live in git history and in [`decisions/`](decisions/) (ADRs),
not here — this file describes the present, not the past.

## Overview

{{ONE_PARAGRAPH_HOW_IT_WORKS}}

## Layers / components

```text
{{TOP_LEVEL_FLOW_OR_LAYERS}}
```

## Module map

| Module | Role | Status |
|---|---|---|
| {{MODULE_1}} | {{ROLE_1}} | {{STATUS_1}} |
| {{MODULE_2}} | {{ROLE_2}} | {{STATUS_2}} |

<!-- "Status" = built / partial / planned. This table is the honest current state;
     update it as modules land. Do not enumerate raw file trees — describe roles. -->

## Key principles / invariants

- {{ARCH_PRINCIPLE_1}}
- {{ARCH_PRINCIPLE_2}}

## Near-term direction

- {{WHATS_NEXT_1}}
- {{WHATS_NEXT_2}}
