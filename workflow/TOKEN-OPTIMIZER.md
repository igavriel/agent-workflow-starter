# Token Optimizer setup

The workflow uses the external [alexgreensh/token-optimizer plugin](https://github.com/alexgreensh/token-optimizer) to help reduce context use and capture platform-reported usage. The plugin is not vendored here, and no installer or hook is run automatically.

## Review before installation

The upstream repository declares the PolyForm Noncommercial 1.0.0 license. Review the current [license](https://github.com/alexgreensh/token-optimizer/blob/main/LICENSE) and [privacy documentation](https://github.com/alexgreensh/token-optimizer/blob/main/PRIVACY.md) before installing, especially for commercial projects or repositories with sensitive content. Upstream documents local access to agent transcripts/settings/skills and local storage of session aggregates and selected cached content; confirm those data paths and retention behavior against the current upstream documentation. The source project states that normal runtime does not transmit data externally, but installation/update may contact GitHub; verify current behavior before relying on that statement.

Installation changes agent configuration. Review the requested scope and authorize it before running commands. Do not run setup hooks globally by default; use project-scoped setup only when the project owner wants hooks.

## Claude Code

In Claude Code, add and install the upstream marketplace plugin using its documented commands:

```text
/plugin marketplace add alexgreensh/token-optimizer
/plugin install token-optimizer@alexgreensh-token-optimizer
```

Then invoke `/token-optimizer` once to initialize its documented hooks. Check the installed plugin UI for its current version and record it in `project.config.yml`. Do not copy upstream plugin code into this starter.

For Claude Code cloud sessions, the upstream project also documents a repository `.claude/settings.json` configuration that registers and enables its marketplace. Adding that configuration enables installation in each cloud session; include it only after the project owner approves that behavior and the privacy review.

## Codex

Add the upstream plugin marketplace from the Codex CLI, then use the Codex `/plugins` interface to install `token-optimizer` from `alexgreensh-token-optimizer`:

```sh
codex plugin marketplace add alexgreensh/token-optimizer
```

The upstream Codex adapter documents an optional hook setup command. It installs globally unless a project path is supplied. If the owner wants project-scoped hooks, locate the script in the installed plugin source and pass the target project path explicitly; the path below is a placeholder because marketplace cache locations are agent-managed:

```sh
TOKEN_OPTIMIZER_RUNTIME=codex python3 <installed-plugin-path>/skills/token-optimizer/scripts/measure.py codex-install --project <project-path>
```

Review upstream `docs/codex.md` for current profiles and behavior. The upstream setup documentation requires Python 3.9 or later. Use the plugin's currently documented default profile unless the project has a concrete reason to choose another.

## Workflow use and records

At task start and before context handoff or compaction, invoke the installed optimizer according to its current instructions. Keep its optimization from removing the active task, authoritative source links, unresolved decisions, privacy/safety constraints, or verification evidence. At session end, record only actual usage values exposed by the agent platform; mark unavailable fields as `unavailable` and never estimate. Record the installed source and version separately for Claude Code and Codex if they differ.

Marketplace installs may auto-update, so they are not a reproducible pin. Record the actual installed version or revision separately for Claude Code and Codex in `project.config.yml`. The plugin's availability does not make its usage figures authoritative when the agent platform does not expose measurements. The project's `templates/token-usage.md` is a summary; the platform remains the source of measured usage.
