FROM node:24-alpine AS frontend-builder

WORKDIR /app/frontend

COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci

COPY frontend /app/frontend
RUN npm run build

FROM python:3.12-slim

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:0.11.0 /uv /uvx /bin/
COPY backend/pyproject.toml backend/README.md /app/backend/
RUN uv sync --project /app/backend --no-dev

COPY backend /app/backend
COPY --from=frontend-builder /app/frontend/out /app/backend/static

EXPOSE 8000

CMD ["uv", "run", "--project", "/app/backend", "uvicorn", "app.main:app", "--app-dir", "/app/backend", "--host", "0.0.0.0", "--port", "8000"]
