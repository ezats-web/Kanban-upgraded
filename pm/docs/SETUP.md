# Local Setup Notes

## Where to put API keys

- Create `pm/.env` from `pm/.env.example`.
- Add your key as:
  - `GROQ_API_KEY=...`

`pm/.env` is ignored by git.

## Tools installed during setup

- Python 3.12
- uv 0.11.0
- Frontend npm dependencies (`frontend/node_modules`)

## Docker Desktop

No API key is needed for Docker itself in this project.
When your Docker Desktop license is confirmed:

- Start with:
  - Windows: `scripts/start-windows.ps1`
  - macOS: `bash scripts/start-macos.sh`
  - Linux: `bash scripts/start-linux.sh`
- Stop with:
  - Windows: `scripts/stop-windows.ps1`
  - macOS: `bash scripts/stop-macos.sh`
  - Linux: `bash scripts/stop-linux.sh`

## Validation status

- Windows Docker flow has been validated end-to-end:
  - `docker compose up -d --build`
  - endpoint checks at `http://localhost:8000`
  - `scripts/start-windows.ps1` and `scripts/stop-windows.ps1`
- macOS/Linux shell scripts are validated for bash syntax and script flow in a Linux bash container.
