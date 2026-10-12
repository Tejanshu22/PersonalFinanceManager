"""Synthetic local foundation. No document, account, payment or tax routes."""
import os

import psycopg
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Personal Finance API", version="0.1.0", docs_url=None, redoc_url=None, openapi_url=None)


@app.get("/health/live")
def live():
    return {"status": "ok", "mode": "synthetic-development"}


@app.get("/health/ready")
def ready():
    database_url = os.environ.get("DATABASE_URL")
    if not database_url:
        return JSONResponse({"status": "not_ready"}, status_code=503)
    try:
        with psycopg.connect(database_url, connect_timeout=3, options="-c statement_timeout=3000") as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                if cursor.fetchone() != (1,):
                    return JSONResponse({"status": "not_ready"}, status_code=503)
    except psycopg.Error:
        # Never expose connection strings, credentials or database exception text.
        return JSONResponse({"status": "not_ready"}, status_code=503)
    return {"status": "ready"}
