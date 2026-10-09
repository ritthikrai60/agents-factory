# Factory Architecture

## Core Concept
The Agents Factory acts as a "compiler" for an AI engineering organization. It takes a Project Profile and Intake specifications, and compiles them into a ready-to-use Antigravity workspace containing specific Rules, Skills, and Agent Role definitions.

## Layers

### 1. Layer A: Native Antigravity
The primary execution layer. We use:
- **Rules (`<RULE>`)**: To enforce project standards, coding guidelines, and safety boundaries.
- **Skills (`SKILL.md`)**: To teach agents reusable capabilities (e.g., Code Review, DB Migration, Integration Test).
- **Subagents**: To separate concerns. A project may have a `Technical Lead`, `Code Reviewer`, and `QA Engineer` operating as subagents.
- **Artifacts**: To persist task states, architectures, and handover reports.

### 2. Layer B: Portable Engineering Assets
These are the files the Factory injects into the target repository:
- `PROJECT_BRIEF.md`, `ARCHITECTURE.md`
- `TASK_BOARD.md` or JSON equivalent
- `catalog/` exports mapped to `.gemini/rules` and `.gemini/skills`

### 3. Layer C: External Orchestrator (Optional)
For state-heavy workflows spanning days, CI pipelines, or multiple repositories, the Factory can emit configuration for external orchestrators (e.g., temporal, airflow, github actions) to coordinate agent triggers.

## Factory Lifecycle
1. **Phase 0 (Discovery):** Agent inspects current directory structure.
2. **Phase 1 (Intake):** Gathers missing requirements.
3. **Phase 2 (Classification):** Categorizes project (e.g., prototype, SaaS).
4. **Phase 3 (Team Design):** Selects agent roles from `catalog/agent-roles/`.
5. **Phase 4 (Shared Context):** Generates markdown docs for architecture and scope.
6. **Phase 5 (Rules/Skills):** Generates `.gemini` folder configurations.
7. **Phase 6 (Decomposition):** Breaks work into tasks.
8. **Phase 7-10 (Loop):** Implementation, bounded repair, quality gates, and release.
9. **Phase 11 (Handover):** Generates handover packages.
