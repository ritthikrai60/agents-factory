# Troubleshooting the Agents Factory

## 1. Agents Loop Infinitely
**Symptom:** Implementer and QA agent keep bouncing a task back and forth without resolving the error.
**Cause:** The repair loop limit wasn't respected, or the error message wasn't passed correctly.
**Fix:** 
- Check the `TASK_BOARD.md` to see the current failure count.
- Manually intervene, set the task to `NEEDS_HUMAN_DECISION`.
- Instruct the agent: "Stop retrying. Let's analyze the error together."

## 2. Factory Refuses to Run Destructive Commands
**Symptom:** Agent refuses to run `terraform destroy` or `DROP TABLE`.
**Cause:** The `<RULE[accidental-data-loss-prevention]>` is active.
**Fix:** This is by design. You must explicitly give permission, e.g., "I am the human decision maker. I authorize the dropping of the table `users_tmp`."

## 3. Cannot Find Skills
**Symptom:** Agent says "I don't know how to run factory-prepare".
**Cause:** The skill isn't in `.gemini/skills/` of your current workspace.
**Fix:** Ensure you are running the agent from the root of the Agents Factory repository, or that the skills have been copied to your target project's `.gemini` folder.
