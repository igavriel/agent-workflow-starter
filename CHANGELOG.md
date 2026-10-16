# Changelog

## 0.6.0 — 2026-10-16

- Split system-of-record configuration into independent task-management (Jira or repository Markdown) and knowledge (Notion or repository OKF) choices.
- Made repository knowledge an OKF bundle, updated its templates and bootstrap guidance, and added a standard-library minimum-contract validator with CI/branch-protection setup instructions.
- Kept handoffs and token reports as separately configured operational Markdown records.

## 0.5.0 — 2026-10-16

- Added an adapted, MIT-attributed `git-workflow-and-versioning` skill with portable Git and commit guidance.
- Routed Git changes through the skill and documented its provenance and license.

## 0.4.0 — 2026-10-16

- Added an optional Claude Code usage-reporting adapter contract with ignored local event storage, generated Markdown report/history templates, and a configured idempotent consolidation point.
- Added `token_usage_reports` as a configurable system-of-record type; no Claude hook or tracker implementation is bundled.

## 0.3.0 — 2026-10-16

- Added setup guidance for the owner-selected token-optimizer repository, with separate Claude Code and Codex instructions and license/privacy review notes; no upstream code is bundled.
- Added repository-wide Git ignore/attribute defaults, EditorConfig, and portable VS Code editing defaults while preserving existing workspace color settings.
- Added README badges for template version, supported agents, record systems, and the external optimizer.

## 0.2.0 — 2026-10-16

- Added an explicit choice among repository Markdown, Jira plus Notion, or per-record mixed systems of record.
- Made the `token-optimizer` skill a required configured workflow dependency and added measured token usage capture at session/task handoffs.

## 0.1.0 — 2026-10-16

- Initial portable workflow template extracted from an established single-owner software project.
- Added Claude Code and Codex entry points, shared workflow instructions, configurable sources of truth, Markdown templates, a bootstrap prompt, source inventory, and upgrade guidance.
