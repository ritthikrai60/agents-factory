$ErrorActionPreference = "Stop"
$factoryRoot = "d:\Coding Projects\Agents Factory"

Write-Host "Starting Factory Validation..."

# Check directories
$dirs = @(
    "docs",
    "templates",
    "catalog/agent-roles",
    "catalog/rules",
    "catalog/skills",
    "catalog/project-profiles",
    "schemas"
)

foreach ($dir in $dirs) {
    if (-not (Test-Path "$factoryRoot\$dir")) {
        Write-Error "Missing required directory: $dir"
    } else {
        Write-Host "PASS: Directory $dir exists."
    }
}

# Check critical files
$files = @(
    "README.md",
    "FACTORY_MANIFEST.md",
    "docs/FACTORY_ARCHITECTURE.md",
    "docs/HOW_TO_PREPARE_A_PROJECT.md",
    "docs/SECURITY_MODEL.md",
    "templates/project-intake.md",
    "templates/task-contract.md",
    "schemas/task-contract.schema.json",
    "catalog/skills/factory-prepare/SKILL.md",
    "catalog/rules/team-coordination/team-coordination.md",
    "catalog/agent-roles/tech-lead/ROLE.md",
    "catalog/agent-roles/code-reviewer/ROLE.md",
    "catalog/agent-roles/qa-engineer/ROLE.md",
    "catalog/project-profiles/small-web-app.md",
    "catalog/project-profiles/production-saas.md"
)

foreach ($file in $files) {
    if (-not (Test-Path "$factoryRoot\$file")) {
        Write-Error "Missing required file: $file"
    } else {
        Write-Host "PASS: File $file exists."
    }
}

# Validate JSON schema format
$jsonSchema = Get-Content "$factoryRoot\schemas\task-contract.schema.json" | ConvertFrom-Json
if ($jsonSchema.title -eq "Task Contract Schema") {
    Write-Host "PASS: JSON schema is valid."
} else {
    Write-Error "Invalid JSON schema."
}

Write-Host "Validation Complete: ALL PASS."
