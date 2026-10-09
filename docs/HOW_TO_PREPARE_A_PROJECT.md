# How to Prepare a Project

## Pre-requisites
- Ensure you have Antigravity 2.0 installed.
- Ensure your target repository is initialized (or you are starting a greenfield project in a new folder).

## Preparation Steps

1. **Initialize the Factory Run**
   Ask Antigravity in the project workspace:
   > "I need to initialize this project using the Agents Factory."

2. **Complete the Intake**
   The agent will invoke the `factory-prepare` skill. It will run through a checklist, looking at `templates/project-intake.md`. It may ask you clarifying questions about:
   - Security constraints
   - Expected scale
   - Tech stack

3. **Review the Blueprint**
   The agent will present a proposed team structure (e.g., "Full-stack Engineer + QA Reviewer"). Approve or modify this structure.

4. **Generation**
   The agent will copy the required assets from the Factory catalog into the project's `.gemini` and `docs/` folders.
   - Project-specific `SKILL.md` files will be created.
   - Global `<RULE>` files will be injected.

5. **Start Development**
   Once preparation is complete, you can begin task execution using the `TASK_BOARD.md`.
