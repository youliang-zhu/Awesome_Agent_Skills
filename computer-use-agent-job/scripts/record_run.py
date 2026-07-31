"""Append one sanitized ATS run record to the skill's learning log."""

from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LOG = SKILL_ROOT / "references" / "validation-and-failure-log.md"

SENSITIVE_PATTERNS = {
    "email address": re.compile(r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b"),
    "long numeric identifier": re.compile(r"(?<!\d)\d{7,}(?!\d)"),
    "credential-like value": re.compile(
        r"(?i)\b(?:bearer\s+\S+|(?:password|passwd|token|cookie|authorization)\s*[:=]\s*\S+)"
    ),
    "local filesystem path": re.compile(r"(?i)(?:[A-Z]:\\|/Users/|/home/)"),
    "URL with path or query": re.compile(r"https?://[^\s/]+[/\?][^\s]*"),
}


def compact(value: str) -> str:
    return " ".join(value.split()).strip()


def slug(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return normalized or "unknown"


def validate_privacy(values: dict[str, str]) -> None:
    for field, value in values.items():
        for label, pattern in SENSITIVE_PATTERNS.items():
            if pattern.search(value):
                raise ValueError(f"{field} contains a possible {label}; generalize it before logging")


def build_record(args: argparse.Namespace) -> str:
    timestamp = args.timestamp or datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    parsed = datetime.fromisoformat(timestamp)
    run_id = f"RUN-{parsed.strftime('%Y%m%d-%H%M%S')}-{slug(args.ats)}-{slug(args.company)}"
    values = {
        "company": compact(args.company),
        "host": compact(args.host),
        "ats": compact(args.ats),
        "variant": compact(args.variant),
        "scope": compact(args.scope),
        "difficulties": compact(args.difficulties),
        "successful tactics": compact(args.successful_tactics),
        "failed tactics": compact(args.failed_tactics),
        "rule changes": compact(args.rule_changes),
        "unresolved": compact(args.unresolved),
    }
    validate_privacy(values)
    return (
        f"\n### {run_id}\n\n"
        f"- Date: {parsed.date().isoformat()}\n"
        f"- Company / host: {values['company']} / {values['host']}\n"
        f"- ATS / variant: {values['ats']} / {values['variant']}\n"
        f"- Scope: {values['scope']}\n"
        f"- Outcome: {args.outcome}\n"
        f"- Difficulties: {values['difficulties']}\n"
        f"- Successful tactics: {values['successful tactics']}\n"
        f"- Failed tactics: {values['failed tactics']}\n"
        f"- Rule changes: {values['rule changes']}\n"
        f"- Unresolved: {values['unresolved']}\n"
        "- Privacy check: no personal values, credentials, attachments, or page transcript\n"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--company", required=True)
    parser.add_argument("--host", required=True, help="Hostname only; do not include a path or query")
    parser.add_argument("--ats", required=True)
    parser.add_argument("--variant", default="unknown")
    parser.add_argument("--scope", required=True)
    parser.add_argument("--outcome", choices=("completed", "partial", "blocked"), required=True)
    parser.add_argument("--difficulties", default="none")
    parser.add_argument("--successful-tactics", default="none")
    parser.add_argument("--failed-tactics", default="none")
    parser.add_argument("--rule-changes", default="none")
    parser.add_argument("--unresolved", default="none")
    parser.add_argument("--timestamp", help="ISO timestamp override for deterministic testing")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    record = build_record(args)
    if args.dry_run:
        print(record, end="")
        return
    with DEFAULT_LOG.open("a", encoding="utf-8", newline="\n") as stream:
        stream.write(record)
    print(record.splitlines()[1])


if __name__ == "__main__":
    main()
