# Skills

## Required external workflow skill

The workflow requires the [token-optimizer plugin](https://github.com/alexgreensh/token-optimizer) at task start and before handoff or compaction. Follow [`workflow/TOKEN-OPTIMIZER.md`](../workflow/TOKEN-OPTIMIZER.md) to install it for Claude Code or Codex, review its privacy behavior, and record the installed version for each agent in `project.config.yml`. Do not substitute a similarly named skill or claim it was used before it is installed. If it is missing, block implementation while continuing independent product discovery. Its upstream repository declares a PolyForm Noncommercial 1.0.0 license; review the current [license terms](https://github.com/alexgreensh/token-optimizer/blob/main/LICENSE) before using it for commercial work.

## Included locally maintained guidance

`manager-response-format/SKILL.md` is a small project-maintained skill adapted from the source repository's own response-format guidance. It is portable source material, not automatically installed for either agent; add it to the tool's configured skill directory only when desired.

## Included adapted third-party skill

`git-workflow-and-versioning/SKILL.md` is adapted from the MIT-licensed `agent-skills` repository. It contains generic Git, commit, verification, and versioning practices. Repository task gates, scripts, hook wiring, and external delivery actions must still come from the new project's own configuration. Attribution and the MIT license are in `THIRD_PARTY_NOTICES.md`.

## Third-party skills

The source repository used selected MIT-licensed skills from [pm-skills](https://github.com/phuryn/pm-skills) and [agent-skills](https://github.com/addyosmani/agent-skills), but those skills are not copied into this starter. Upstream content, dependencies, availability, and licenses can change; review the exact skill and license before installing it in a new project.

Useful source-project candidates to evaluate individually include `interview-me`, `spec-driven-development`, `planning-and-task-breakdown`, `incremental-implementation`, `test-driven-development`, `debugging-and-error-recovery`, `code-review-and-quality`, `security-and-hardening`, and `documentation-and-adrs` from agent-skills, plus `identify-assumptions-new`, `create-prd`, `pre-mortem`, and `user-stories` from pm-skills. These are suggestions from the source repository, not required dependencies.

Install only a specific skill that fits a real project need. Check its references for dead links, commands or stack assumptions, license notices, overlapping guidance, and tool compatibility. Adapt it to the configured workflow, record its source and license, and remove references to skills that are not installed. Do not bulk-copy a repository or run upstream install scripts without a separate review and explicit authorization.
