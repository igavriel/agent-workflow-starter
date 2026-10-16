# Agent entry point

This file is the Codex-compatible entry point. Before project work, read `project.config.yml` and `workflow/OPERATING-MODEL.md`, then read only the task and authoritative sources relevant to the current step. If `project.config.yml` is missing, use `prompts/bootstrap.md` to inspect the repository and initialize the workflow before implementation.

Follow the configured source of truth for each information type. During bootstrap, confirm whether the project uses repository Markdown, Jira plus Notion, or a configured mixed setup. Do not duplicate editable specifications or tasks in Markdown when another system is authoritative. Surface missing or contradictory decisions; do not invent product scope, requirements, stack choices, commands, or approval.

Use the configured `token-optimizer` plugin at the start of task work and before a context handoff or compaction, following its installed instructions without dropping required context or verification. Setup and review guidance is in `workflow/TOKEN-OPTIMIZER.md`. Record actual token usage at session end when the platform exposes it; otherwise record `unavailable`. Never estimate token or cost values.

When Claude-specific Markdown reporting is enabled in project configuration, follow `workflow/CLAUDE-USAGE-REPORTING.md`; keep raw events local and consolidate generated reports only at the configured point.
