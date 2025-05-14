import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.schemas.auth import LoginData
from app.services.authenticator import AuthService

client = TestClient(app)


def test_main_route():
    response = client.get("/api/main")
    assert response.status_code == 200
    assert response.json() == {"message": "ok"}


def test_auth_service_success(monkeypatch):
    login_data = LoginData(login="admin", password="admin")

    # правильные значения из config
    from app.core.config import config
    monkeypatch.setattr(config, "USER_LOGIN", "admin")
    monkeypatch.setattr(config, "USER_PASSWORD", "admin")

    service = AuthService()
    assert service.authenticate_user(login_data) is True


def test_auth_service_fail(monkeypatch):
    login_data = LoginData(login="wrong", password="wrong")

    # неправильные значения
    from app.core.config import config
    monkeypatch.setattr(config, "USER_LOGIN", "admin")
    monkeypatch.setattr(config, "USER_PASSWORD", "admin")

    service = AuthService()
    assert service.authenticate_user(login_data) is False
