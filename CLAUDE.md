# Claude Code entry point

Before project work, read `project.config.yml` and `workflow/OPERATING-MODEL.md`, then read only the task and authoritative sources relevant to the current step. If `project.config.yml` is missing, use `prompts/bootstrap.md` to inspect the repository and initialize the workflow before implementation.

During bootstrap, ask independently whether tasks are managed in Jira or repository task documents, and whether product knowledge is managed in Notion or repository OKF. When repository knowledge is selected, all durable knowledge concepts must use OKF in the configured bundle and pass the configured validator. Do not treat task, handoff, or token-report Markdown as knowledge concepts. Follow one authority per information type; never maintain duplicate editable records.

Use the configured `token-optimizer` plugin at the start of task work and before a context handoff or compaction, following its installed instructions without dropping required context or verification. Setup and review guidance is in `workflow/TOKEN-OPTIMIZER.md`. Record actual token usage at session end when the platform exposes it; otherwise record `unavailable`. Never estimate, infer, or record zero for missing values.

If `project.config.yml` enables `workflow.claude_usage_reporting`, follow `workflow/CLAUDE-USAGE-REPORTING.md` for local event capture and the configured Markdown consolidation point. Never commit raw event logs or update generated usage reports before that point.
