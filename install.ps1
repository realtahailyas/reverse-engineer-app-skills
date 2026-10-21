# Installs the Replica skills into ~/.claude/skills so every Claude Code project can use them.
$ErrorActionPreference = 'Stop'
$repo = 'https://github.com/realtahailyas/reverse-engineer-app-skills'
$dest = if ($env:CLAUDE_SKILLS_DIR) { $env:CLAUDE_SKILLS_DIR } else { Join-Path $HOME '.claude\skills' }
$tmp = Join-Path ([IO.Path]::GetTempPath()) ([Guid]::NewGuid())
git clone --depth 1 $repo "$tmp\repo" | Out-Null
New-Item -ItemType Directory -Force $dest | Out-Null
Copy-Item -Recurse -Force "$tmp\repo\skills\replica-*" $dest
Remove-Item -Recurse -Force $tmp
Write-Host "Installed 11 Replica skills into $dest"
Write-Host 'Open Claude Code and type: /replica-recon <app url>'
