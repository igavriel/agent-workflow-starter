# Operating model

## Purpose and adaptation

This workflow carries a product idea through discovery, an approved specification, a plan, small implementation tasks, focused verification, review, and a clear handoff. Adapt the artifacts, status names, role names, and commands in `project.config.yml` to the new repository before relying on them. The workflow is a process guide, not a product or technology specification.

The source project separates product discussion from engineering and stores only approved conclusions. A new project may use one agent for discovery and engineering, or different tools for them; the portable rule is that an implementing agent must follow the owner's approved product decisions and surface contradictions rather than resolve them silently.

## Stages and gates

| Stage | Main activity | Durable output | Gate to proceed |
|---|---|---|---|
| Inspect and initialize | Read existing agent guidance, product artifacts, architecture, task systems, commands, and local changes selectively. | Completed project configuration and source-of-truth map. | Owner confirms unknown required inputs or accepts explicitly recorded unknowns before implementation. |
| Product discovery | Understand user, problem, current workaround, desired outcome, constraints, and what is out of scope. Ask only essential unresolved questions. | Approved product direction or a discovery note with open questions. | Product owner approves the direction; do not pretend an idea is a complete specification. |
| Specify | Turn approved direction into observable behavior and success criteria; distinguish known facts, assumptions, and unresolved questions. | Specification in the configured knowledge authority. | Product owner approves scope and unresolved questions needed by the next task are resolved. |
| Plan and task | Order dependencies and prepare one focused task with scope, exclusions, acceptance criteria, verification, and blockers. | Plan and task record in the configured task-management authority. | Task is explicitly marked ready only when blockers and prerequisites are resolved. |
| Implement | Work one ready task in a focused session and isolated branch/worktree if configured; make small, coherent increments. | Code/documentation changes, task status, and concise evidence. | Acceptance criteria are met and a coherent reviewable state exists. |
| Review and verify | Review the task-scoped diff against criteria; resolve actionable findings; run the exact prescribed final verification. Use specialist reviewers only when their domain is affected. | Review findings/resolutions and verification evidence attached to the task or authoritative record. | No unresolved blocking or should-fix findings; final verification passes or an owner-approved exception is explicit. |
| Delivery decision | Present the concrete verified result and ask for the configured release/merge/deploy approval when required. | Approval record and delivery result. | No external state change without explicit approval as configured. A declined gate stops delivery and waits for direction. |
| Resume | Start a fresh focused session or compact with a written handoff that identifies exact state and next action. | Updated handoff in its configured authoritative system. | The next agent verifies branch/commit/changed paths and reads only the task plus named sources. |

Stages may collapse for tiny changes, but do not bypass necessary product approval, task readiness, verification, or external-action approval. Do not add stages merely for completeness.

## Roles

- **Product owner:** decides product direction, approves specifications and scope, resolves owner-controlled questions, and authorizes external actions.
- **Implementing agent:** inspects the repository, follows the ready task, implements changes, runs appropriate checks, maintains records, and reports uncertainty.
- **Reviewer:** checks a stable task-scoped change against its criteria and concrete failure scenarios; the reviewer does not expand scope or implement fixes unless explicitly assigned.
- **Verification runner:** may run one exact prescribed command and return compact evidence; failures go to the implementing agent for diagnosis.
- **Delivery operator:** may perform approved merge, publish, deployment, or cleanup steps after a verified handoff; stops on unexpected state.
- **Specialist reviewer:** optional, narrow review triggered by affected domain risks such as security, privacy, accessibility, or critical calculations.

One person or agent may hold several roles in a small project, but keep approval ownership explicit. Independent review is useful when the change warrants it and an independent reviewer is available; no particular model, agent count, or vendor is required.

## Artifact and authority map

Choose task management and knowledge storage independently in `project.config.yml`.

| Information | Authority and minimum content |
|---|---|
| Product direction, specifications, and decisions | Either Notion, or an in-repository OKF knowledge bundle (commonly `docs/knowledge/`). In the repository option, every durable knowledge concept must be OKF with YAML frontmatter containing a non-empty `type`. |
| Plan, tasks, and completion record | Either Jira, or repository task documents using the configured templates. This choice is independent of the knowledge choice. |
| Session handoff and token usage report | Repository Markdown at the configured operational-record locations; these are workflow records, not OKF concepts. |

When Notion is selected for knowledge, it is authoritative for product direction, specifications, and decisions; do not keep competing editable copies in the repository. When repository knowledge is selected, keep those concepts in the configured OKF bundle and do not use Notion as a second editable authority. When Jira is selected for task management, Jira owns plans/tasks/completion as configured; do not maintain competing editable repository task records. At bootstrap, ask each choice separately and confirm exact project/database/path locations and access before using external systems.

### Repository knowledge must use OKF

When `systems_of_record.knowledge.system` is `okf_markdown`, the configured directory is an OKF knowledge bundle. Each knowledge concept is a Markdown file with a YAML frontmatter block and a non-empty `type` field; use the OKF specification for other fields and bundle conventions. `index.md` and `log.md` are reserved bundle filenames and do not contain concept frontmatter. The package-provided validator checks this minimum contract; configure its exact command as `workflow.okf_validation_command`, run it during work, and make it a required CI check so invalid knowledge cannot merge. If the repository uses another CI system, wire the same command into its required check. Branch protection must be enabled in the host settings.

Do not force tasks, handoffs, token reports, README files, or code documentation outside the knowledge bundle into OKF solely because they are Markdown. If knowledge is stored in Notion, the repository OKF validator may be omitted unless the repository separately maintains an OKF bundle.

## Task readiness and completion

A task is ready only when its objective and scope are clear, dependencies are satisfied, acceptance criteria are falsifiable, verification is known, and no owner-controlled decision needed for implementation remains open. If a prerequisite or decision is unresolved, record it as a blocker and stop at that boundary.

A task is complete when its acceptance criteria and configured Definition of Done are satisfied, required reviews are clean or explicitly dispositioned, verification has passing evidence, durable records are updated, and the handoff states what remains. Keep `done` distinct from `released` if release requires a separate approval. Do not mark work done because code exists or because a command was attempted.

## Context efficiency and session handoff

- Invoke the configured `token-optimizer` plugin at the start of task work and before a context handoff or compaction; follow its installed instructions and report concrete recommendations. See `workflow/TOKEN-OPTIMIZER.md` for installation and privacy/licensing review. Do not invent commands or claim use when the plugin is unavailable.
- The optimizer may shorten or prioritize context, but it must preserve required instructions, the active task, named authoritative sources, unresolved blockers, safety/privacy rules, and verification evidence.
- Inspect repository entry points and targeted references; do not read the whole codebase or history without a concrete reason.
- For implementation, read the current task and only its named authoritative sources, plus directly relevant files.
- Load only the skill or reviewer needed for the current phase. Avoid broad, overlapping reviews and repeated narration of already-known context.
- Keep command output compact; retain verbose logs and artifacts on disk and surface only the evidence needed for a decision.
- Prefer one focused task per implementation session. Before switching tasks or ending, update the handoff with branch/commit, changed paths, current task status, decisions, blockers, verification, and the exact next action.
- A resumed session checks current repository state before acting and does not assume the prior agent's result is still current.
- At session end, record actual input/output and cache token counts when the platform exposes them, plus cost only when the platform reports it. If no measurement is available, record `unavailable`, never zero or an estimate. Label cumulative snapshots as cumulative and do not compare them as per-session deltas. When the optional Claude-to-Markdown adapter is enabled, hooks keep raw events local and the configured consolidation command alone updates tracked reports; see `workflow/CLAUDE-USAGE-REPORTING.md`.

Use `templates/session-handoff.md` and `templates/token-usage.md` for ordinary handoffs and summaries. Product direction, specifications, and decisions in repository mode use the OKF-ready templates. Optional Claude reports use `templates/claude-usage-report.md` and `templates/claude-usage-history.md`. Configure one authoritative location for usage reports; platform-reported measurements remain the source of truth.

## Git, review, and external actions

Use the configured branch strategy and project commands; do not copy commands from a different repository. Load `skills/git-workflow-and-versioning/SKILL.md` when handling Git changes, commits, branches, or versioning. Keep changes scoped, inspect the final diff, preserve unrelated user work, and avoid commits unless the project configuration or user request authorizes them. Record review findings with their resolution and evidence. Do not push, publish, merge, deploy, send messages, or perform other external state changes unless the configured approval gate is satisfied.

## Ambiguities to configure, not infer

The source workflow uses a single-owner approval model, a dedicated branch per task, named Claude subagents, a Haiku verification runner, a GitHub pull request flow, and hooks that record measured session usage. Those are not universal requirements. Set or remove each behavior in the project configuration; do not install a vendor tool, add a dependency, create an account, or invent a measurement process to imitate the source project.

This template requires the external `alexgreensh/token-optimizer` plugin as a workflow dependency. Review its current license and privacy behavior before installing. Record the installed source and agent-specific version in project configuration. Do not substitute a similarly named skill or copy upstream code; if the plugin is missing, record a blocker before implementation while continuing any independent discovery work.
