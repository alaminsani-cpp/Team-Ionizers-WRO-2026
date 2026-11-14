# Team Ionizers - optional Windows PowerShell helper.
# Run inside this extracted folder, after creating the empty public GitHub repository.
# It does not invent files, proof of testing, or historical Git commits.
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
Write-Host 'TEAM IONIZERS | WRO 2026' -ForegroundColor Cyan
Write-Host 'First review START_HERE.md and add original code and evidence.'
$answer = Read-Host 'Type PUSH to continue (anything else cancels)'
if ($answer -cne 'PUSH') { Write-Host 'Cancelled'; exit 0 }
$repoUrl = Read-Host 'Paste the URL for your NEW EMPTY GitHub repository (https://github.com/USERNAME/REPO.git)'
if ($repoUrl -notmatch '^https://github\.com/[A-Za-z0-9-]+/[A-Za-z0-9._-]+(?:\.git)?$') {
  throw 'Enter a valid GitHub HTTPS repository URL.'
}
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { throw 'Git is not installed or not on PATH.' }
if (Test-Path '.git') { throw 'This folder already has Git history; use ordinary git commands to preserve it.' }
& git init
if ($LASTEXITCODE -ne 0) { throw 'git init failed' }
& git add .
if ($LASTEXITCODE -ne 0) { throw 'git add failed' }
& git commit -m 'Add Team Ionizers WRO Future Engineers 2026 repository'
if ($LASTEXITCODE -ne 0) { throw 'git commit failed; configure Git author name/email first.' }
& git branch -M main
if ($LASTEXITCODE -ne 0) { throw 'git branch failed' }
& git remote add origin $repoUrl
if ($LASTEXITCODE -ne 0) { throw 'Could not configure remote' }
& git push -u origin main
if ($LASTEXITCODE -ne 0) { throw 'Push failed; check remote creation and authentication.' }
Write-Host 'Repository pushed. Verify it is PUBLIC and view README on GitHub.' -ForegroundColor Green
