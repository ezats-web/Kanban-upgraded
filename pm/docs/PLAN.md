# Project Plan Checklist

## Ground rules

- Pin dependencies to the latest stable version available at install time.
- Keep implementation minimal and direct; avoid extra architecture.
- Use root `.env` for runtime secrets and never hardcode API keys.
- Scope remains local-only Dockerized MVP.

---

## Part 1: Planning and documentation

### Checklist

- [x] Expand this plan with concrete implementation and verification steps.
- [x] Add `frontend/AGENTS.md` documenting current frontend architecture and testing.
- [x] Update root `AGENTS.md` technical direction to Groq API and correct known doc issues.

### Tests

- [x] Manual review for consistency between `AGENTS.md`, `docs/PLAN.md`, and `frontend/AGENTS.md`.

### Success criteria

- Plan is executable phase by phase without ambiguity.
- AI provider and env-var naming are consistent in all docs.
- Frontend starting point is clearly documented for future work.

---

## Part 2: Scaffolding

### Checklist

- [x] Create backend FastAPI service in `backend/` with health endpoint.
- [x] Add simple HTML response at `/` from backend for initial integration validation.
- [x] Add one example API endpoint (for example `/api/ping`) returning JSON.
- [x] Add Dockerfile and container entrypoint to run backend app.
- [x] Add OS scripts under `scripts/` for start/stop on Windows, macOS, and Linux.
- [x] Add backend dependency and tool configuration using `uv`.

### Tests

- [x] Run local backend without Docker and verify `/` and `/api/ping`.
- [x] Build Docker image successfully.
- [x] Run container and verify endpoints from host machine.
- [x] Verify each start/stop script starts and stops cleanly on its target OS syntax.

### Success criteria

- One command per OS starts the MVP stack.
- Backend serves HTML and JSON from containerized runtime.
- Project can be bootstrapped from clean checkout using docs/scripts only.

---

## Part 3: Add frontend static build and serving

### Checklist

- [x] Build Next.js frontend as static assets in a reproducible build step.
- [x] Serve frontend static output from FastAPI at `/`.
- [x] Preserve existing Kanban interactions from current frontend.
- [x] Integrate frontend build into Docker image.

### Tests

- [x] Frontend unit tests pass.
- [x] Frontend e2e tests pass against the frontend application flow.
- [x] Containerized app renders Kanban at `/`.

### Success criteria

- App root shows current Kanban demo from static frontend build.
- No regression in existing board interactions (rename/add/delete/drag).

---

## Part 4: Add fake sign-in experience

### Checklist

- [ ] Implement login screen shown before board access.
- [ ] Accept only hardcoded credentials: `user` / `password`.
- [ ] Implement logout control.
- [ ] Persist login state across browser refresh for better UX in MVP.
- [ ] Guard frontend routes so unauthenticated users cannot access board UI.

### Tests

- [ ] Unit tests for auth state and route guard behavior.
- [ ] Integration/e2e tests for login success, login failure, refresh persistence, logout.

### Success criteria

- User must log in before board becomes visible.
- Invalid credentials are rejected with clear feedback.
- Logout returns user to login view and blocks board access.

---

## Part 5: Database modeling

### Checklist

- [ ] Define SQLite schema supporting multiple users.
- [ ] Store board state as JSON per user (single board per user in MVP).
- [ ] Add migration/init flow that creates DB and schema when missing.
- [ ] Document schema and rationale in `docs/`.
- [ ] Obtain user sign-off on schema doc before backend CRUD implementation.

### Tests

- [ ] Unit tests for schema initialization and default record creation.
- [ ] Verify DB file and required tables are created from clean state.

### Success criteria

- Data model supports current MVP and future multi-user extension.
- Board JSON can be loaded/saved without schema ambiguity.

---

## Part 6: Backend board APIs

### Checklist

- [ ] Implement auth endpoint(s) for dummy credential flow.
- [ ] Implement board read endpoint for authenticated user.
- [ ] Implement board update endpoint for authenticated user.
- [ ] Ensure DB auto-creation on first startup.
- [ ] Add request/response validation with clear error messages.

### Tests

- [ ] Backend unit tests for auth acceptance/rejection.
- [ ] Backend unit tests for board read/update happy and failure paths.
- [ ] Backend tests for DB initialization on missing file.

### Success criteria

- Authenticated user can read and persist board state.
- Unauthenticated requests are rejected.
- Backend behavior is deterministic and covered by tests.

---

## Part 7: Connect frontend to backend

### Checklist

- [ ] Replace frontend local board source with backend API integration.
- [ ] Load board on app startup after login.
- [ ] Persist edits (rename/add/delete/move) through backend calls.
- [ ] Add loading and error states for network operations.

### Tests

- [ ] Unit tests for API client and state transitions.
- [ ] Integration tests for frontend-backend flow.
- [ ] E2E tests covering persistent edits across reload.

### Success criteria

- Board is persisted in SQLite and survives app restart.
- Core board interactions remain smooth and consistent.

---

## Part 8: AI connectivity with Groq

### Checklist

- [ ] Add backend Groq client configuration via `GROQ_API_KEY`.
- [ ] Implement minimal connectivity endpoint/service that asks `2+2`.
- [ ] Handle API failures with clear backend error responses.
- [ ] Document required env vars and local setup.

### Tests

- [ ] Integration test for Groq connectivity using mocked client.
- [ ] Optional manual smoke test against live API key in local env.

### Success criteria

- Backend can successfully call Groq model and receive a response.
- Failures are observable and do not crash the service.

---

## Part 9: AI structured board updates

### Checklist

- [ ] Define structured response schema including:
  - assistant message text
  - optional board update payload
- [ ] Send current board JSON + user prompt + in-memory chat history to AI.
- [ ] Validate and parse structured AI responses robustly.
- [ ] Apply optional board updates server-side before returning response.
- [ ] Keep conversation history in memory per app run (not persisted).

### Tests

- [ ] Unit tests for response parsing/validation.
- [ ] Backend integration tests for:
  - message-only responses
  - message + board update responses
  - malformed response handling

### Success criteria

- AI endpoint returns deterministic typed payloads.
- Valid board updates are applied automatically.
- Invalid AI payloads fail gracefully without corrupting board data.

---

## Part 10: Sidebar AI chat UI with auto-apply

### Checklist

- [ ] Add right sidebar chat component with conversation view and input.
- [ ] Wire chat submit to backend AI endpoint.
- [ ] Automatically refresh board UI when backend returns board update.
- [ ] Keep UX polished and aligned with project color/theme system.
- [ ] Preserve existing board usability while chat is active.

### Tests

- [ ] Component tests for chat rendering and interactions.
- [ ] Integration tests for AI request/response flow.
- [ ] E2E tests verifying board auto-update after AI response.

### Success criteria

- User can chat naturally from sidebar while working on board.
- AI-driven board changes appear automatically without manual refresh.
- MVP behavior matches business requirements in root `AGENTS.md`.