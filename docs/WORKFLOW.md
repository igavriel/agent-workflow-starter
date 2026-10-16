# What the template provides and how work flows

## Template contents

The package supplies portable process guidance and starter artifacts. It does not supply application code or Jira/Notion connections. Configure the two system choices independently: Jira or repository task records; Notion or repository OKF knowledge. Repository knowledge must pass the OKF validator. The external `token-optimizer` skill must be installed for the chosen agent only after its license and privacy behavior have been reviewed.

```mermaid
flowchart LR
    subgraph Entry[Agent entry points]
        A[AGENTS.md for Codex and shared agent guidance]
        B[CLAUDE.md for Claude Code]
    end
    subgraph Process[Shared process]
        C[workflow/OPERATING-MODEL.md]
        D[prompts/bootstrap.md]
        E[docs/INSTALLATION.md]
    end
    subgraph Config[Project configuration]
        F[project.config.template.yml]
        G[Task authority: Jira or repository Markdown]
        H[Knowledge authority: Notion or repository OKF]
    end
    subgraph Artifacts[Templates and checks]
        I[OKF product direction, specification, decision templates]
        J[Task, plan, handoff, and token usage templates]
        K[OKF minimum-contract validator]
    end
    subgraph Skills[Skills and usage]
        L[git-workflow-and-versioning]
        M[manager-response-format]
        N[token-optimizer external plugin]
        O[Optional Claude usage report adapter]
    end
    A --> C
    B --> C
    C --> D
    E --> D
    C --> F
    F --> G
    F --> H
    H -->|OKF in repository| I
    H -->|OKF in repository| K
    G --> J
    F --> J
    C --> L
    C --> M
    C --> N
    F --> O
```

## Product-to-delivery process

Stages may collapse for small changes, but the relevant approval and verification gates remain. Discovery starts from the repository's actual state: if product direction is not approved, the agent asks essential questions and explores the problem instead of assuming a finished specification.

```mermaid
flowchart TD
    A[Inspect repository and initialize configuration] --> B[Choose task and knowledge authorities]
    B --> C{Is product direction already approved?}
    C -->|No| D[Product discovery: user, problem, current workaround, outcome, constraints]
    C -->|Yes| E[Read current authoritative product knowledge]
    D --> F[Owner reviews and approves direction]
    E --> G[Specify observable behavior and success criteria]
    F --> G
    G --> H[Owner approves specification and resolves blocking questions]
    H --> I[Plan dependencies and create one focused task]
    I --> J{Task ready?}
    J -->|No| I
    J -->|Yes| K[Implement in a focused session; invoke token-optimizer]
    K --> L[Review task-scoped changes and run configured verification]
    L --> M{Criteria, review, and verification satisfied?}
    M -->|No| K
    M -->|Yes| N[Present verified result and request configured delivery approval]
    N --> O{Delivery approved?}
    O -->|No| P[Stop at approval gate and wait]
    O -->|Yes| Q[Perform only authorized delivery actions]
    Q --> R[Record actual token usage or unavailable]
    P --> S[Write handoff: state, evidence, blockers, next action]
    R --> S
    S --> T[Next session verifies current repo state and resumes]
    T --> I
```

The token optimizer supports context reduction at task start and before handoff or compaction. It must preserve the active task, authoritative sources, unresolved blockers, privacy rules, and verification evidence. Token and cost figures in handoffs are actual measurements only; record `unavailable` when the platform does not expose them. See [`workflow/TOKEN-OPTIMIZER.md`](../workflow/TOKEN-OPTIMIZER.md) and [`workflow/OPERATING-MODEL.md`](../workflow/OPERATING-MODEL.md).
