from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Project Management MVP Backend", version="0.1.0")
FRONTEND_STATIC_DIR = Path(__file__).resolve().parents[1] / "static"


if not FRONTEND_STATIC_DIR.exists():

    @app.get("/", response_class=HTMLResponse)
    def root() -> str:
        return """
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>PM MVP Backend</title>
          </head>
          <body style="font-family: Arial, sans-serif; padding: 2rem;">
            <h1>PM MVP Backend is running</h1>
            <p>Frontend static build not found yet.</p>
            <p>Try <code>/api/ping</code> for JSON hello-world response.</p>
          </body>
        </html>
        """


@app.get("/api/ping")
def ping() -> dict[str, str]:
    return {"message": "pong"}


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


if FRONTEND_STATIC_DIR.exists():
    # Keep API routes defined before static mount so /api/* remains handled by FastAPI.
    app.mount("/", StaticFiles(directory=FRONTEND_STATIC_DIR, html=True), name="frontend")
