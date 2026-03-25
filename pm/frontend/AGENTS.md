# Frontend Overview

## Purpose

`frontend/` contains the current standalone MVP UI for the Kanban board. It is a Next.js app that currently runs without backend persistence.

## Stack

- Next.js (App Router) with React and TypeScript
- Tailwind CSS for styling
- `@dnd-kit` for drag-and-drop card movement
- Vitest + Testing Library for unit/component tests
- Playwright for end-to-end tests

## Current user-facing behavior

- Renders a single Kanban board at `/`
- Supports:
  - renaming fixed columns
  - adding cards
  - deleting cards
  - moving cards with drag and drop
- Uses in-memory state; data is reset on refresh

## Key files

- `src/app/page.tsx`: app entry that renders the board
- `src/components/KanbanBoard.tsx`: top-level board state and event handlers
- `src/components/KanbanColumn.tsx`: column UI and interactions
- `src/components/KanbanCard.tsx`: card UI and drag handle
- `src/lib/kanban.ts`: board data model, initial state, and move utility
- `src/components/KanbanBoard.test.tsx`: board interaction tests
- `src/lib/kanban.test.ts`: utility-level tests
- `tests/kanban.spec.ts`: Playwright e2e scenarios

## Commands

- Install: `npm install`
- Dev server: `npm run dev`
- Lint: `npm run lint`
- Unit tests: `npm run test:unit`
- E2E tests: `npm run test:e2e`
- All tests: `npm run test:all`

## Constraints for future changes

- Keep UI behavior simple and direct; avoid over-engineering.
- Preserve existing drag-and-drop and card editing behavior during integration.
- Keep tests updated with any behavior changes.
- Follow root project requirements in `../AGENTS.md`.
