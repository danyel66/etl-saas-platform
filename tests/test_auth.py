import pytest


def test_signup(client):
    response = client.post("/signup/", json={
        "email": "test@example.com",
        "full_name": "Test User",
        "password": "secret123",
    })
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["role"] == "user"
    assert "id" in data


def test_signup_duplicate_email(client):
    payload = {"email": "dup@example.com", "full_name": "Dup", "password": "pass"}
    client.post("/signup/", json=payload)
    response = client.post("/signup/", json=payload)
    assert response.status_code == 400
    assert "already registered" in response.json()["detail"]


def test_login(client):
    client.post("/signup/", json={
        "email": "login@example.com",
        "full_name": "Login User",
        "password": "mypassword",
    })
    response = client.post("/login/", data={
        "username": "login@example.com",
        "password": "mypassword",
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password(client):
    client.post("/signup/", json={
        "email": "user@example.com",
        "full_name": "User",
        "password": "correct",
    })
    response = client.post("/login/", data={
        "username": "user@example.com",
        "password": "wrong",
    })
    assert response.status_code == 401


def test_me_endpoint(client):
    client.post("/signup/", json={
        "email": "me@example.com",
        "full_name": "Me User",
        "password": "pass123",
    })
    login = client.post("/login/", data={
        "username": "me@example.com",
        "password": "pass123",
    })
    token = login.json()["access_token"]

    response = client.get("/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["email"] == "me@example.com"


def test_protected_data_requires_auth(client):
    response = client.get("/protected-data")
    assert response.status_code == 401


def test_admin_only_forbidden_for_regular_user(client):
    client.post("/signup/", json={
        "email": "regular@example.com",
        "full_name": "Regular",
        "password": "pass",
    })
    login = client.post("/login/", data={
        "username": "regular@example.com",
        "password": "pass",
    })
    token = login.json()["access_token"]

    response = client.get("/admin-only", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 403
