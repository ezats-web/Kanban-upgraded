$ErrorActionPreference = "Stop"

function Get-DockerCommand {
  $dockerFromPath = Get-Command docker -ErrorAction SilentlyContinue
  if ($dockerFromPath) {
    return $dockerFromPath.Source
  }

  $fallback = "C:\Program Files\Docker\Docker\resources\bin\docker.exe"
  if (Test-Path $fallback) {
    return $fallback
  }

  throw "Docker CLI not found. Install Docker Desktop and restart your terminal."
}

Set-Location -Path (Join-Path $PSScriptRoot "..")
$docker = Get-DockerCommand

& $docker compose down

Write-Host "PM app stopped."
