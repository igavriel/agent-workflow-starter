# Portable Development Workflow

[![Template version](https://img.shields.io/badge/template-0.6.1-blue)](VERSION)
[![Agents](https://img.shields.io/badge/agents-Claude%20Code%20%7C%20Codex-6f42c1)](AGENTS.md)
[![Tasks](https://img.shields.io/badge/tasks-Repository%20Markdown%20%7C%20Jira-0a7ea4)](#systems-of-record)
[![Knowledge](https://img.shields.io/badge/knowledge-OKF%20Markdown%20%7C%20Notion-3178c6)](#systems-of-record)
[![Token Optimizer](https://img.shields.io/badge/token%20optimizer-external%20plugin-orange)](https://github.com/alexgreensh/token-optimizer)

Version: `0.6.1` (`VERSION` is authoritative).

This repository is a small starter for carrying a product-to-delivery workflow into a new project. It supports Claude Code and Codex through thin root entry files and lets each project select task management and knowledge storage independently.

## Copy and initialize

### Add it to an existing repository

1. Create a working branch in the target repository and preserve its existing changes.
2. Copy the starter files from this repo at a reviewed version, excluding this repo's `.git/` and `project.config.yml`.
3. Merge `AGENTS.md`, `CLAUDE.md`, `README.md`, `.gitignore`, and editor settings with existing files; do not overwrite project guidance or local configuration blindly.
4. Use the [existing-repository installation guide](docs/INSTALLATION.md) and its ready-to-paste agent prompt to adapt the files, choose task and knowledge authorities, configure OKF validation when applicable, and begin discovery.

The template repository itself cannot update an existing repository automatically. Review the resulting changes in the target repo before merging them.

### Start a new repository

1. If this repository is enabled as a GitHub template, create the new repository with **Use this template**; otherwise create an empty repository and copy the starter files without this starter's `.git/` directory.
2. In the new repository, copy `project.config.template.yml` to `project.config.yml` and fill only the required fields; leave unknown optional settings explicitly unset.
3. Read `AGENTS.md`, `CLAUDE.md`, and `workflow/OPERATING-MODEL.md`.
4. Run the bootstrap prompt in `prompts/bootstrap.md` with the agent that will work in the new repository.
5. Review and approve the adapted project instructions and first discovery record before treating them as authoritative.
6. Keep this template version in the project configuration and record local changes in `workflow/LOCAL-CUSTOMIZATIONS.md`.

See [`docs/INSTALLATION.md`](docs/INSTALLATION.md) for the installation diagram and adoption prompt, and [`docs/WORKFLOW.md`](docs/WORKFLOW.md) for the template contents and product-to-delivery pipeline diagrams.

No application package dependency is bundled. Repository knowledge uses the package-provided validator `scripts/validate-okf.py` (Python 3 standard library only) when OKF is selected; wire its command into CI and make it a required check. Branch protection must be enabled separately in the hosting service. The workflow also uses the external [token-optimizer plugin](https://github.com/alexgreensh/token-optimizer), which must be installed for the selected agent after reviewing its license and privacy behavior; it is not bundled. The upstream project currently declares a [PolyForm Noncommercial 1.0.0 license](https://github.com/alexgreensh/token-optimizer/blob/main/LICENSE), so review its terms before using it in a commercial project. Jira or Notion require separately configured access and remain authoritative only when selected.

## Files

- `docs/INSTALLATION.md` explains new and existing repository setup with a ready-to-paste adoption prompt and Mermaid diagram.
- `docs/WORKFLOW.md` maps the supplied components and the product-to-delivery process as Mermaid diagrams.
- `workflow/OPERATING-MODEL.md` describes the reusable stages, roles, artifacts, authority choices, approval points, completion bar, and handoff practice.
- `workflow/TOKEN-OPTIMIZER.md` documents the external plugin's reviewed Claude Code and Codex setup paths.
- `workflow/CLAUDE-USAGE-REPORTING.md` documents the optional local-event-to-Markdown reporting lifecycle for Claude Code.
- `scripts/validate-okf.py` checks OKF frontmatter delimiters and the required non-empty `type` field; it uses Python 3 standard-library modules only.
- `.gitignore`, `.gitattributes`, `.editorconfig`, and `.vscode/settings.json` provide small repository and editor defaults without adding an application runtime dependency.
- `project.config.template.yml` separates required project inputs and independently maps task management, knowledge, and operational records.
- `templates/` contains OKF-ready knowledge templates plus concise Markdown templates for tasks, plans, handoffs, and token usage.
- `prompts/bootstrap.md` is a ready-to-paste prompt for inspecting a new repository, selecting authorities independently, and beginning product discovery.
- `skills/` contains locally maintained response-format guidance, an adapted MIT-licensed Git workflow skill, attribution, and instructions for evaluating other third-party skills.
- `SOURCE-INVENTORY.md` maps the source material to exported components and exclusions.
- `CHANGELOG.md` records template-level changes; `VERSION` is the simple template version identifier.

## Systems of record

At bootstrap, choose task management and product knowledge independently. For tasks, choose repository Markdown or Jira. For product direction, specifications, and decisions, choose repository OKF or Notion. The repository option means every durable knowledge concept in the configured OKF bundle has a YAML frontmatter `type`; CI can enforce the package's validation command. Jira and Notion are not coupled: a project can use Jira tasks with OKF knowledge, or repository tasks with Notion knowledge.

Session handoffs and token usage reports remain operational Markdown records at their configured locations. They are not knowledge concepts and do not need OKF frontmatter. Do not maintain editable copies of records owned by Jira or Notion. This package does not connect to external services; configure and authorize any connector separately.

## Knowledge format and validation

OKF is an open format for a bundle of Markdown concepts with YAML frontmatter. See the [OKF specification](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md). This template's repository knowledge minimum is the required non-empty `type` field; it does not invent a separate taxonomy. The validator checks frontmatter delimiters and that field. It is intentionally not a full YAML parser, so additional frontmatter syntax should be checked with an existing project YAML validator if required.

Run `python3 scripts/validate-okf.py docs/knowledge` after replacing the path with the configured knowledge bundle. Configure the exact command in `workflow.okf_validation_command`, run it locally, and add it as a required CI status check. Enable branch protection in hosting settings; the template cannot configure those settings across all repositories.

## Skills

The locally maintained `manager-response-format` skill source is included in `skills/manager-response-format/SKILL.md`. The required `token-optimizer` plugin is external; see `skills/README.md` and `workflow/TOKEN-OPTIMIZER.md` for the Claude Code and Codex setup paths.

Token usage is part of each session handoff and task completion record. Use actual platform measurements when available, record `unavailable` otherwise, and never estimate. The platform's measurements are authoritative; `templates/token-usage.md` is a concise project summary. Claude Code projects may optionally capture ignored local lifecycle events and generate Markdown reports at a configured consolidation point; other agents continue using their configured measurement source.

## Example bootstrap walkthrough

See the final section of `SOURCE-INVENTORY.md` for a hypothetical small mobile app initialized in a different domain. It demonstrates the independent task and knowledge choices, OKF requirement for repository knowledge, and product discovery without building the application.

## Versioning, improvements, and upgrades

The starter is the central template. When a project discovers a reusable improvement, keep it project-local first, then propose the generalized change to this repository with any domain names, commands, secrets, and path assumptions removed. Update `VERSION` and `CHANGELOG.md` here after accepting the improvement.

To upgrade a project, compare the new template with its installed base version, review each file, merge only reusable updates, preserve project-specific sections and local customizations, update the recorded template version, and note the upgrade in the project's change history. Never replace customized instructions wholesale.
