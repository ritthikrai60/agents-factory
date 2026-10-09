# Native vs Orchestrator

## Native Antigravity Execution (Default)
The Factory defaults to using **Native Antigravity** capabilities.

**When to use Native:**
- Solo developer workflows with AI assistance.
- Single repository projects.
- Short-lived or interactive task loops (e.g., generating code, reviewing in real-time).
- Context sharing via Artifacts and Subagent conversations.

## External Orchestrator (Optional)
Sometimes native execution is not enough to enforce strict organizational pipelines.

**When to use an Orchestrator:**
- You need persistent cross-session task queues that survive agent restarts.
- Machine-enforced approval gates (e.g., CI/CD gating deployments).
- Distributed multi-agent execution across different repositories.
- Hard retry policies (e.g., "retry 3 times, then alert PagerDuty").

**Integration:**
When the Factory detects a High-Risk or Multi-Repo profile, it will suggest creating a `adapters/orchestrator/` configuration, such as a GitHub Action workflow or a step-function pipeline, to govern agent invocation.
