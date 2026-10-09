# Security Model

The Factory enforces a least-privilege security model for all generated teams.

## 1. Agent Permissions
- **Read-Only Agents:** Researchers, Code Reviewers, and QA Agents (who only verify).
- **Write-Restricted Agents:** Implementation agents can edit code but cannot run `terraform apply`, database drop commands, or deployment scripts.
- **Privileged Agents:** CI/CD or Release agents, which MUST require Human Approval for destructive actions.

## 2. Destructive Action Bounding
Generated rules include the `<RULE[accidental-data-loss-prevention]>` standard. No agent may execute:
- `DROP`, `TRUNCATE`, or broad `DELETE` on databases.
- Deletion of cloud storage buckets or KMS keys.
- Production deployments.
Without explicit Human verification via interactive prompt.

## 3. Secret Management
Agents are prohibited from generating code that hardcodes credentials. All Factory-generated architectures default to using environment variables or Secret Managers.
