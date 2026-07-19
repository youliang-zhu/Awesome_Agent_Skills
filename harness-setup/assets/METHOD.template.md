# {{HARNESS_NAME}} — Test / Debug Method

How to run and reproduce checks for this docs harness. Keep this concrete and
grounded in the real scripts, commands, and artifacts for `{{HARNESS_DIR}}`.

## How to run

```
{{HOW_TO_BUILD_AND_RUN}}
```

## Reproducing a failure

{{HOW_TO_CAPTURE_EVIDENCE_LOGS_ARTIFACTS}}

## What to record

Each debug/test round goes into [`log/`](log/). Record:

- date, target, version/input set
- command or manual procedure
- result and key metrics
- artifact path or id
- follow-up change and retest result

## Artifact rules

{{ARTIFACT_RULES}}

Sensitive or generated local-only outputs must not be committed:

{{SENSITIVE_PATHS}}
