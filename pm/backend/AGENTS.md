# Backend Overview

## Purpose

`backend/` contains the FastAPI service for the Project Management MVP.

## Part 2 and Part 3 scope implemented

- FastAPI app entrypoint at `app/main.py`
- Endpoints:
  - `GET /` serves static frontend build when available
  - `GET /` falls back to a simple backend HTML page when static build is not present
  - `GET /api/ping` returns JSON `{ "message": "pong" }`
  - `GET /api/health` returns JSON `{ "status": "ok" }`
- Python dependency management defined in `pyproject.toml` (for use with `uv`)
- Static frontend output is expected at `backend/static` in container runtime

## Run notes

- Local run command:
  - `uv run --project backend uvicorn app.main:app --app-dir backend --host 0.0.0.0 --port 8000`
- Docker run is managed through root `Dockerfile` and scripts in `scripts/`.
- Docker multi-stage build compiles the frontend and copies `frontend/out` into `backend/static`.