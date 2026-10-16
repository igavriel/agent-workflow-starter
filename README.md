# Portable Development Workflow

[![Template version](https://img.shields.io/badge/template-0.5.0-blue)](VERSION)
[![Agents](https://img.shields.io/badge/agents-Claude%20Code%20%7C%20Codex-6f42c1)](AGENTS.md)
[![Systems of record](https://img.shields.io/badge/records-Markdown%20%7C%20Jira%20%7C%20Notion-0a7ea4)](#systems-of-record)
[![Token Optimizer](https://img.shields.io/badge/token%20optimizer-external%20plugin-orange)](https://github.com/alexgreensh/token-optimizer)

Version: `0.5.0` (`VERSION` is authoritative).

This repository is a small starter for carrying a product-to-delivery workflow into a new project. It supports Claude Code and Codex through thin root entry files and keeps project rules, tools, and systems of record configurable.

## Copy and initialize

1. Copy the starter files into the new repository root; exclude this starter's `.git/` directory and merge existing project files instead of overwriting local work.
2. In the new repository, copy `project.config.template.yml` to `project.config.yml` and fill only the required fields; leave unknown optional settings explicitly unset.
3. Read `AGENTS.md`, `CLAUDE.md`, and `workflow/OPERATING-MODEL.md`.
4. Run the bootstrap prompt in `prompts/bootstrap.md` with the agent that will work in the new repository.
5. Review and approve the adapted project instructions and first discovery record before treating them as authoritative.
6. Keep this template version in the project configuration and record local changes in `workflow/LOCAL-CUSTOMIZATIONS.md`.

No runtime or package dependencies are added by this template. The workflow uses the external [token-optimizer plugin](https://github.com/alexgreensh/token-optimizer), which must be installed for the selected agent after reviewing its license and privacy behavior; it is not bundled. The upstream project currently declares a [PolyForm Noncommercial 1.0.0 license](https://github.com/alexgreensh/token-optimizer/blob/main/LICENSE), so review its terms before using it in a commercial project. Jira or Notion require separately configured access and remain authoritative only when selected in the project configuration.

## Files

- `workflow/OPERATING-MODEL.md` describes the reusable stages, roles, artifacts, approval points, completion bar, and handoff practice.
- `workflow/TOKEN-OPTIMIZER.md` documents the external plugin's reviewed Claude Code and Codex setup paths.
- `workflow/CLAUDE-USAGE-REPORTING.md` documents the optional local-event-to-Markdown reporting lifecycle for Claude Code.
- `.gitignore`, `.gitattributes`, `.editorconfig`, and `.vscode/settings.json` provide small repository and editor defaults without adding a runtime dependency.
- `project.config.template.yml` separates required project inputs from optional workflow settings and assigns a single source of truth to each information type.
- `templates/` contains concise Markdown templates for projects using Markdown as the configured system of record, including optional Claude usage report and history formats.
- `prompts/bootstrap.md` is a ready-to-paste prompt for inspecting a new repository and beginning product discovery.
- `skills/` contains locally maintained response-format guidance, an adapted MIT-licensed Git workflow skill, attribution, and instructions for evaluating other third-party skills.
- `SOURCE-INVENTORY.md` maps the source material to exported components and exclusions.
- `CHANGELOG.md` records template-level changes; `VERSION` is the simple template version identifier.

## Systems of record

At bootstrap, choose `markdown_repository`, `jira_notion`, or `mixed` in `project.config.yml`. `markdown_repository` keeps each record in repository Markdown, as in the source project. `jira_notion` uses Notion for specifications and Jira for tasks, then explicitly assigns one authority to every other record type; a common mapping is only a suggestion for owner approval. `mixed` assigns a system per information type. Do not maintain editable copies of the same information in multiple places; link to the authority or label an exported copy as a non-authoritative snapshot.

This package does not connect to external services. Configure and authorize any connector separately, then follow that system's access and change controls.

## Skills

The locally maintained `manager-response-format` skill source is included in `skills/manager-response-format/SKILL.md`. The required `token-optimizer` plugin is external; see `skills/README.md` and `workflow/TOKEN-OPTIMIZER.md` for the Claude Code and Codex setup paths.

Token usage is part of each session handoff and task completion record. Use actual platform measurements when available, record `unavailable` otherwise, and never estimate. The platform's measurements are authoritative; `templates/token-usage.md` is a concise project summary. Claude Code projects may optionally capture ignored local lifecycle events and generate Markdown reports at a configured consolidation point; other agents continue using their configured measurement source.

## Versioning, improvements, and upgrades

The starter is the central template. When a project discovers a reusable improvement, keep it project-local first, then propose the generalized change to this repository with any domain names, commands, secrets, and path assumptions removed. Update `VERSION` and `CHANGELOG.md` here after accepting the improvement.

To upgrade a project, compare the new template with its installed base version, review each file, merge only reusable updates, preserve project-specific sections and local customizations, update the recorded template version, and note the upgrade in the project's change history. Never replace customized instructions wholesale.

## Source-based walkthrough

See the final section of `SOURCE-INVENTORY.md` for a hypothetical initialization of a small mobile web app in a different domain. It shows discovery and configuration choices only; it does not build the app or select an unapproved stack.
