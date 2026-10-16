# Optional Claude usage reporting

This optional adapter turns locally captured Claude Code usage events into committed Markdown reports. It is disabled by default, does not add a runtime dependency, and does not define Claude hook names or a tracker implementation for every project.

## Enable only when applicable

Enable `workflow.claude_usage_reporting` only when Claude Code is used, the platform exposes verifiable usage measurements, a project-specific capture/consolidation adapter exists, and the owner wants a Markdown report. Set `systems_of_record.operational_records.token_usage_reports` to the configured repository Markdown location. Usage reports are operational records, separate from the independent task-management and knowledge authorities.

Configure the event location, generated report and history locations, one consolidation point, and the exact consolidation command in `project.config.yml`. The default example is consolidation after a task has merged to the default branch, once the authoritative task record says it is complete. Projects without that delivery flow must choose a suitable point explicitly. Do not enable the adapter while the consolidation point or command is unset.

## Capture and consolidate

1. At Claude session and subagent start/end, the project-specific adapter may append lifecycle events with identifiers, task/branch context, model, timestamps, and only actual usage snapshots exposed by the platform.
2. Keep event files under the configured local event location, which must be ignored by Git. Do not store prompts, transcript text, tool output, credentials, or private product data in these events.
3. Routine hooks append local events only. They do not edit tracked Markdown reports or commit changes.
4. At the single configured consolidation point, run the configured command. It should validate the target state, match complete start/end pairs, derive deltas only from compatible measured snapshots, render the completed-task report, and move open or legacy lifecycles to the history report with their measurement type labeled.
5. Make consolidation idempotent: retrying the same task without new events must not duplicate rows. Preserve local event data if report generation fails; do not commit a partial report.

The completed-task report should show task, agent/model, scope, lifecycle count, measured input/output/cache values, reported cost, and measurement source/type. The history report should retain incomplete or legacy rows with clear `open`, `cumulative`, or `unavailable` labels. Never interpret missing values as zero or estimate them.

Before summing sessions or subagents, verify what the platform counters include. Do not add child usage to parent totals when parent measurements already include it. If snapshot semantics, attribution, or task association cannot be established, preserve separate rows or mark the affected values unavailable rather than inventing an aggregation.

## Privacy, Git, and scope

The local event directory is ignored so detailed raw measurements stay on the machine. Only the generated Markdown summaries are candidates for Git. Keep raw-event retention and cleanup behavior explicit in the project adapter; never silently purge events before a successful consolidation.

This starter provides the reporting contract, configuration fields, report templates, and lifecycle guidance. It does not ship a Claude hook installer, transcript parser, usage collector, or consolidation script. Implement those only after checking the current Claude Code hook API and the actual measurement fields available in the target project. If any field is unavailable, report `unavailable`.

For sessions without this optional adapter, use `templates/token-usage.md` and the configured usage-report authority for measured summaries.
