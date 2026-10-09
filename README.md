# Agents Factory

*[อ่านเอกสารเป็นภาษาไทย (Read in Thai)](README_TH.md)*

The **Agents Factory** is a reusable meta-system designed for the Antigravity 2.0 Agent Manager. It configures, validates, and provisions an AI-assisted engineering team for future projects.

Instead of generating one monolithic setup, this Factory generates an adaptive workspace structure tailored to project scope, complexity, and risk.

## Philosophy
- **Minimal Viable Intelligence:** Instantiate the smallest team that can safely and correctly deliver a project.
- **Durable Coordination:** Utilize task contracts, evidence-based review, and explicit handoffs rather than relying purely on context windows and conversational history.
- **Fail-Safes:** Bounded repair loops, escalation paths to human review, and explicit quality gates.

## Usage

See the [How to Prepare a Project](docs/HOW_TO_PREPARE_A_PROJECT.md) guide.

## Repository Structure
- `templates/` — Markdown templates for specs, architectures, decision records, etc.
- `catalog/` — The master registry of Agent Roles, Skills, Rules, and Quality Gates.
- `factory/` — Core preparation logic (Intake, Discovery, Classification, Team Generation).
- `schemas/` — JSON Schemas defining the structure of factory contracts.
- `docs/` — Operating manuals and architectural notes.

## Execution

The Agents Factory utilizes native Antigravity 2.0 features (Skills, Rules, Artifacts, Subagents). 
Where an orchestrator is necessary for persistent state machines or distributed execution, it can adapt to external systems (see [Native vs Orchestrator](docs/NATIVE_VS_ORCHESTRATOR.md)).
