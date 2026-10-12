from unittest.mock import MagicMock, patch

import psycopg
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_live_without_database():
    assert client.get("/health/live").json() == {"status": "ok", "mode": "synthetic-development"}


def test_ready_requires_configuration(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    assert client.get("/health/ready").status_code == 503


def test_database_failure_is_sanitized(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql://fictional")
    with patch("app.main.psycopg.connect", side_effect=psycopg.OperationalError("sensitive diagnostic")):
        response = client.get("/health/ready")
    assert response.status_code == 503
    assert response.json() == {"status": "not_ready"}


def test_ready_checks_database(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql://fictional")
    connection = MagicMock()
    cursor = connection.__enter__.return_value.cursor.return_value.__enter__.return_value
    cursor.fetchone.return_value = (1,)
    with patch("app.main.psycopg.connect", return_value=connection):
        assert client.get("/health/ready").json() == {"status": "ready"}
    cursor.execute.assert_called_once_with("SELECT 1")


def test_data_collection_and_public_api_docs_are_absent():
    for path in ["/upload", "/accounts", "/payments", "/tax", "/docs", "/openapi.json"]:
        assert client.post(path).status_code == 404
