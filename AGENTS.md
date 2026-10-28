# docker-training — Docker learning exercises

This file is the project's AI context (Cursor, Kiro, Antigravity, and Claude Code read `AGENTS.md`). No chat history existed for this folder; this summary comes from the files as of 28 Oct 2026. Owner: Dinesh Kumar R (GitHub `dineshwondersoft-2509`). Built on a company-managed Windows 11 laptop with Docker Desktop and no admin rights. The user wants direct action, then a short plain-language result. Update **Current state** here after changes that matter.

## Purpose

The user's hands-on Docker practice. Keep examples minimal and explain each instruction when asked. The user has "Docker knowledge" listed as a skill (knowledge level, not production experience).

## Exercises

1. **Single container** (`Dockerfile`, `index.html`): `nginx:alpine` serving a static "Hello from Docker!" page.

   ```powershell
   cd docker-training
   docker build -t my-docker-app .
   docker run --rm -p 8080:80 my-docker-app     # http://localhost:8080
   ```

2. **Three-tier compose lab** (`docker-prof/`): browser -> nginx frontend -> Flask API -> Postgres 16.

   | Service | Build / image | Notes |
   |---|---|---|
   | `frontend` | `docker-prof/frontend` (nginx:alpine) | Published on host port **8080**. `default.conf` serves `index.html` and proxies `/api/` to `http://api:5000/`. Page has "Test API" and "Test Database" buttons. |
   | `api` | `docker-prof/api` (python:3.12-slim, Flask, psycopg2-binary) | Internal only (`expose: 5000`). `GET /` status JSON; `GET /db` connects to Postgres and returns `SELECT version()`. |
   | `db` | `postgres:16` | Named volume `postgres_data`. Credentials `trainingdb` / `traininguser` / `trainingpass` are throwaway training values. |

   ```powershell
   cd docker-training\docker-prof
   docker compose up --build        # http://localhost:8080
   docker compose down              # add -v to also delete the Postgres volume
   ```

## Machine notes

Docker Desktop's WSL data (`docker-desktop` distro, 5.2 GB) was unregistered on 18 Aug 2026 to free space on `C:`. Docker Desktop is still installed and recreates an empty engine on next start, so all images are pulled again on the first run.

## Current state

No open work.
