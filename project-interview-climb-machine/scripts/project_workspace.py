#!/usr/bin/env python3
"""Manage Project Interview Climb Machine workspaces."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import unicodedata
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parent.parent
PROJECT_TEMPLATE = SKILL_DIR / "assets" / "project-template.md"
PORTFOLIO_TEMPLATE = """# 多项目面试准备

## 当前关注

<!-- 记录跨项目自我介绍当前希望解决的问题。 -->
"""


class WorkspaceError(RuntimeError):
    """A user-actionable workspace error."""


def workspace_path(value: str) -> Path:
    return Path(value).expanduser().resolve()


def projects_dir(workspace: Path) -> Path:
    return workspace / "projects"


def require_workspace(workspace: Path) -> None:
    if not workspace.is_dir():
        raise WorkspaceError(f"Workspace does not exist: {workspace}")
    if not projects_dir(workspace).is_dir():
        raise WorkspaceError(
            f"Workspace is not initialized (missing projects directory): {workspace}"
        )


def slugify(name: str) -> str:
    normalized = unicodedata.normalize("NFKD", name)
    ascii_name = normalized.encode("ascii", "ignore").decode("ascii").lower()
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_name).strip("-")
    if not slug:
        digest = hashlib.sha256(name.encode("utf-8")).hexdigest()[:8]
        slug = f"project-{digest}"
    return slug[:64].rstrip("-")


def validate_slug(slug: str) -> str:
    if not re.fullmatch(r"[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?", slug):
        raise WorkspaceError(
            "Slug must be 1-64 lowercase ASCII letters, digits, or hyphens, "
            "and cannot start or end with a hyphen."
        )
    return slug


def read_project_title(project_file: Path) -> str:
    try:
        with project_file.open("r", encoding="utf-8") as handle:
            for line in handle:
                if line.startswith("# "):
                    return line[2:].strip() or project_file.parent.name
    except UnicodeDecodeError:
        return f"{project_file.parent.name} [project.md is not UTF-8]"
    return project_file.parent.name


def command_init(args: argparse.Namespace) -> int:
    workspace = workspace_path(args.workspace)
    if workspace.exists() and not workspace.is_dir():
        raise WorkspaceError(f"Workspace path is a file: {workspace}")

    workspace.mkdir(parents=True, exist_ok=True)
    projects_dir(workspace).mkdir(exist_ok=True)
    portfolio = workspace / "portfolio.md"
    if not portfolio.exists():
        portfolio.write_text(PORTFOLIO_TEMPLATE, encoding="utf-8", newline="\n")
        portfolio_state = "created"
    else:
        portfolio_state = "preserved"

    print(f"workspace\t{workspace}")
    print(f"portfolio\t{portfolio_state}\t{portfolio}")
    return 0


def command_list(args: argparse.Namespace) -> int:
    workspace = workspace_path(args.workspace)
    require_workspace(workspace)

    found = []
    for project_file in sorted(projects_dir(workspace).glob("*/project.md")):
        found.append(
            (project_file.parent.name, read_project_title(project_file), project_file)
        )

    if not found:
        print("No projects found.")
        return 0

    for slug, title, project_file in found:
        print(f"{slug}\t{title}\t{project_file}")
    return 0


def command_create(args: argparse.Namespace) -> int:
    workspace = workspace_path(args.workspace)
    require_workspace(workspace)

    name = args.name.strip()
    if not name:
        raise WorkspaceError("Project name cannot be empty.")
    slug = validate_slug(args.slug) if args.slug else validate_slug(slugify(name))
    destination = projects_dir(workspace) / slug
    if destination.exists():
        raise WorkspaceError(f"Project directory already exists: {destination}")
    if not PROJECT_TEMPLATE.is_file():
        raise WorkspaceError(f"Project template is missing: {PROJECT_TEMPLATE}")

    template = PROJECT_TEMPLATE.read_text(encoding="utf-8")
    project_text = template.replace("{{PROJECT_NAME}}", name)

    destination.mkdir()
    for directory_name in ("materials", "exports", ".cache"):
        (destination / directory_name).mkdir()
    project_file = destination / "project.md"
    project_file.write_text(project_text, encoding="utf-8", newline="\n")

    print(f"project\t{slug}\t{name}\t{project_file}")
    return 0


def collect_issues(workspace: Path, selected_project: str | None) -> list[str]:
    issues = []
    if not workspace.is_dir():
        return [f"Workspace does not exist: {workspace}"]
    if not (workspace / "portfolio.md").is_file():
        issues.append(f"Missing file: {workspace / 'portfolio.md'}")
    root = projects_dir(workspace)
    if not root.is_dir():
        issues.append(f"Missing directory: {root}")
        return issues

    if selected_project:
        project_dirs = [root / validate_slug(selected_project)]
        if not project_dirs[0].is_dir():
            issues.append(f"Project does not exist: {project_dirs[0]}")
            return issues
    else:
        project_dirs = sorted(path for path in root.iterdir() if path.is_dir())

    for project_dir in project_dirs:
        for relative in ("project.md", "materials", "exports", ".cache"):
            expected = project_dir / relative
            if relative == "project.md":
                if not expected.is_file():
                    issues.append(f"Missing file: {expected}")
            elif not expected.is_dir():
                issues.append(f"Missing directory: {expected}")
    return issues


def command_check(args: argparse.Namespace) -> int:
    workspace = workspace_path(args.workspace)
    issues = collect_issues(workspace, args.project)
    if issues:
        for issue in issues:
            print(f"ERROR\t{issue}")
        return 1
    print(f"OK\t{workspace}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Initialize, list, create, and check interview project workspaces."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Initialize a chosen workspace.")
    init_parser.add_argument("--workspace", required=True)
    init_parser.set_defaults(handler=command_init)

    list_parser = subparsers.add_parser("list", help="List projects in a workspace.")
    list_parser.add_argument("--workspace", required=True)
    list_parser.set_defaults(handler=command_list)

    create_parser = subparsers.add_parser("create", help="Create a project.")
    create_parser.add_argument("--workspace", required=True)
    create_parser.add_argument("--name", required=True)
    create_parser.add_argument("--slug")
    create_parser.set_defaults(handler=command_create)

    check_parser = subparsers.add_parser("check", help="Validate workspace structure.")
    check_parser.add_argument("--workspace", required=True)
    check_parser.add_argument("--project")
    check_parser.set_defaults(handler=command_check)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.handler(args)
    except WorkspaceError as exc:
        print(f"ERROR\t{exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
