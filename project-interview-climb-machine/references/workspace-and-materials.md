# Workspace and Materials

## Conversation entry

Ask for the workspace path at the start of every new conversation unless the
user already supplied it. Do not use a default and do not store a cross-session
path configuration.

Use the workspace script for deterministic operations:

```text
python scripts/project_workspace.py init --workspace <path>
python scripts/project_workspace.py list --workspace <path>
python scripts/project_workspace.py create --workspace <path> --name <name>
python scripts/project_workspace.py check --workspace <path>
```

Pass `--slug <slug>` to `create` only when the user specifies or needs a stable
directory name.

## Runtime layout

```text
<workspace>/
├── portfolio.md
└── projects/
    └── <project-slug>/
        ├── project.md
        ├── materials/
        ├── exports/
        └── .cache/
```

Do not place user data inside the installed skill or its source repository.
Do not create a central project index. Discover projects by scanning
`projects/*/project.md`.

`project.md` is the sole main document for one project. Keep different roles
and companies in sections of that same document. Use `portfolio.md` only for
content spanning multiple projects, including M10; keep its different role
contexts in that same file.

## Minimal project base

Keep the project base minimal and incremental. Do not require a fixed inventory
of ownership, alternatives, experiments, failures, limitations, or retrospective
changes. Ask for one of those only when the user's current task needs it.

Separate these content types visibly:

- confirmed project facts;
- external sources or current developments;
- candidate reflections and working ideas;
- AI suggestions awaiting user choice.

Never save an inference or AI suggestion as a confirmed project fact.

## Material intake

Support three material forms:

1. Files the user places under `materials/`.
2. Conversation attachments the user asks to preserve.
3. External local paths or remote links, especially for large code repositories.

Keep `materials/` flat by default. Permit user-created subdirectories. Preserve
original names when practical. Treat originals as read-only; do not overwrite,
rename, move, or delete them without an explicit request. Store requested
generated files under `exports/`. Store only reproducible extraction or preview
artifacts under `.cache/`.

The presence of a file is not permission to inspect its contents. On resume,
you may list newly discovered filenames. Read a file in detail only when:

- the user explicitly asks to inspect, analyze, or cite it; or
- it appears materially useful to the active task, you explain why, and the
  user agrees to the read.

When the user uploads an attachment:

- persist it under `materials/` only when the user asks to add it to the project;
- otherwise treat it as temporary context;
- apply the same detailed-reading permission rule either way.

Register only the path or link and a short user-confirmed purpose in
`project.md`. Do not copy long excerpts or full extracted text into the main
document.

## Safe document updates

Before every write:

1. Re-read the current `project.md` or `portfolio.md`.
2. Locate the exact target heading.
3. Preserve unknown headings, user prose, and manual edits.
4. Update only the target section.
5. If the target is ambiguous or duplicated, ask before writing.

Create module headings lazily. Do not fill a new project with empty M0–M10
sections. Write only content the user has confirmed. If a fact change may affect
another section, add a concise review flag or tell the user; do not silently
rewrite the other section.
