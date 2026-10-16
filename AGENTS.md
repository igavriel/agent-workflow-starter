# Agent entry point

Before project work, read `project.config.yml` and `workflow/OPERATING-MODEL.md`, then read only the task and authoritative sources relevant to the current step. If `project.config.yml` is missing, use `prompts/bootstrap.md` to inspect the repository and initialize the workflow before implementation.

The bootstrap independently asks where tasks live (Jira or repository task docs) and where product knowledge lives (Notion or repository OKF). If knowledge is stored in the repository, all durable knowledge concepts must use OKF in the configured bundle and pass the configured validator. Do not treat task, handoff, or token-report Markdown as knowledge concepts. Follow one authority per information type; never maintain duplicate editable records.

Use the configured `token-optimizer` plugin at the start of task work and before a context handoff or compaction. See `workflow/TOKEN-OPTIMIZER.md`; preserve required context and verification. Record actual token usage at session end when the platform exposes it; otherwise record `unavailable`. Never estimate usage or cost.

When Claude-specific Markdown reporting is enabled in project configuration, follow `workflow/CLAUDE-USAGE-REPORTING.md`; keep raw events local and consolidate generated reports only at the configured point.
