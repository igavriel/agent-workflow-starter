---
name: git-workflow-and-versioning
description: Use when changing Git state, preparing commits, branching, resolving conflicts, working across worktrees, or maintaining project versions and changelogs.
---

# Git Workflow and Versioning

Adapted from [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills), with portable project-specific rules removed. See `skills/THIRD_PARTY_NOTICES.md` for attribution and license.

## Use and scope

Load this guidance for Git changes, commits, branches, conflicts, worktrees, releases, version changes, and changelog updates. The repository's own `AGENTS.md`, `CLAUDE.md`, task instructions, and `project.config.yml` take precedence when they define a concrete workflow. Never import branch names, scripts, status rules, or release actions from another repository without configuration.

## Core practice

- Inspect `git status`, the current branch, and the relevant diff before changing Git state. Preserve unrelated user changes.
- Keep each change scoped and reviewable. Prefer short-lived branches when configured; use a worktree for parallel work only when the project supports it.
- Use small, coherent commits with descriptive messages. Follow the configured commit convention; if none exists, use `<type>: <short purpose>` with a concise explanation when the purpose is not clear from the title.
- Before committing, review the complete staged diff, check for secrets and private data, and run only the checks actually configured and relevant to the change. Never invent commands or claim unrun checks passed.
- Keep `.gitignore` aligned with local secrets, generated output, and private data. Commit editor configuration only when it is intended to be shared by the project.
- Do not use destructive commands such as `reset --hard`, force-push, or broad cleanup to resolve uncertainty. Inspect, preserve, and ask when the safe recovery path is unclear.
- Do not push, publish, open or merge a pull request, deploy, delete a branch, or create a tag unless the user and project approval rules authorize that action.

## Git changes and task completion

When a project has task records, follow the configured readiness, dependency, branch, review, verification, and completion rules. Do not implement blocked or unapproved work. Keep task completion separate from release when the project requires a release approval.

Keep commits focused on the user-authorized change. If an initial repository setup is explicitly requested, it may be committed on its configured initial branch; do not invent an implementation task or branch requirement for setup work.

## Claude usage reports

When the optional Claude usage report is enabled, keep raw hook events in the configured ignored local directory. Update tracked Markdown only through the configured consolidation command and at its configured checkpoint. Follow `workflow/CLAUDE-USAGE-REPORTING.md`; never add estimated values or commit raw event data.

## Versions and changelogs

- Use semantic versioning only when the project declares a versioned consumer-facing artifact. Treat breaking changes as major, backward-compatible functionality as minor, and fixes as patch changes.
- Update the version and human-readable changelog with the change when the repository maintains them. Keep version references consistent; do not create tags automatically.
- If the project has no release/versioning scheme, do not introduce one solely because this skill describes it.

## Commit checklist

- [ ] The staged diff contains only the authorized, related files.
- [ ] No credentials, private data, local event logs, or unintended generated files are staged.
- [ ] The commit message follows the project's convention and describes the purpose.
- [ ] Relevant configured verification has passing evidence, or its unrun/unavailable status is clear.
- [ ] No external Git action is implied by a local commit.
