# Token usage: [task or reporting period]

Use one row per agent session. Capture values from the configured platform measurement source; this file is a summary, not a replacement for that source.

If the optional Claude-to-Markdown adapter is enabled, follow `workflow/CLAUDE-USAGE-REPORTING.md`; routine hooks write only ignored local events and the configured consolidation step generates the tracked report.

| Session/date | Agent and model | Scope | Input tokens | Output tokens | Cache read/write tokens | Cost | Measurement type/source |
|---|---|---|---:|---:|---:|---:|---|
| [session/date] | [agent/model] | [task or activity] | [measured value or unavailable] | [measured value or unavailable] | [measured values or unavailable] | [reported value or unavailable] | [session delta/cumulative; source] |

## Rules

- Record only values directly reported by the platform or verified measurement tooling; never estimate or infer missing values.
- Use `unavailable` when the platform does not expose a field; do not substitute zero.
- Mark measurements as per-session deltas or cumulative snapshots. Do not compare cumulative snapshots as task-level usage.
- Keep a measurement source link or platform location when one exists, and do not expose credentials, private prompts, or transcript content in this report.
- A cumulative total may be derived only from compatible measured start/end snapshots from the same session and platform, and must be labeled as a derived delta.
