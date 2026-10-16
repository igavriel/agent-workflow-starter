# Bootstrap prompt for a new repository

Copy and paste this prompt into Claude Code or Codex while the working directory is the new repository:

```text
Initialize the portable workflow template in this repository, then begin product discovery if the product is not already specified.

First inspect the existing agent entry files, README, relevant product/specification/decision/plan/task documents, repository structure, and available build/test/lint commands. Follow references selectively. Check the working tree and preserve existing changes. Do not scan the entire codebase or Git history unless a concrete question requires it.

Read the copied template's project.config.template.yml and workflow/OPERATING-MODEL.md. Create project.config.yml and adapt AGENTS.md and CLAUDE.md only after identifying the actual project tools and conventions. Ask the owner to choose repository Markdown, Jira plus Notion, or a mixed system-of-record map; set exactly one authority and location for every information type. Do not create competing editable Markdown copies. Confirm authorization and access before connecting external services.

If Claude Code will be used, ask whether the owner wants the optional Claude-to-Markdown usage report. If enabled and an adapter already exists, set `systems_of_record.authorities.token_usage_reports` to one Markdown authority and configure its local event/report paths and consolidation point. If no adapter exists, keep the option disabled and record a separate follow-up only if the owner wants it implemented; do not build a collector during bootstrap. Keep this option disabled for other agents or when Claude measurement data is unavailable.

Check whether the configured `token-optimizer` plugin from `https://github.com/alexgreensh/token-optimizer` is installed for the selected agent and inspect its instructions. Read `workflow/TOKEN-OPTIMIZER.md` for the correct setup path. Before installing, surface its license and local-data handling for owner review; do not run the install or hook setup without authorization. Do not substitute similarly named skills or imitate instructions you have not inspected. Continue independent repository inspection and product discovery while the plugin is unavailable, but do not begin implementation until it is available or the owner changes the workflow requirement.

Identify which actual token usage fields this agent platform exposes and record its measurement source in configuration. Use `templates/token-usage.md` for session summaries. At session end, record measured values or `unavailable`; never estimate, infer, or use zero for missing data.

Do not assume the product is specified because code or a README exists. Identify what is known, what is only an assumption, and what is missing. If an approved product direction and specification already exist, summarize their current authority and continue from their actual state. Otherwise begin discovery: establish who has the problem, what happens today, what outcome matters, why now, and the important constraints and exclusions. Ask only the essential unanswered question that could change the product direction or the next safe step; ask one at a time, wait for the answer, and continue useful repository inspection while waiting. Do not invent answers, requirements, success metrics, users, or stack choices.

After discovery, summarize the intent and ask the owner to approve or correct it before treating it as authoritative. Only then record product direction in its configured system of record. Do not create implementation tasks or mark any task ready until a specification is approved, dependencies are understood, acceptance criteria and verification are concrete, and owner-controlled blockers are resolved. Begin product discovery; do not start building application code in this bootstrap step.

Keep the initialization small. Record unknown optional settings as unset, preserve local customizations, and finish with the configured authorities, token-optimizer plugin status, token measurement availability, known facts, unresolved blockers, and one next action.
```
