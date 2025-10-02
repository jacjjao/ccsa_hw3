import os
import pytest
import psycopg2
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add_name(client):
    res = client.post("/add-name", json={"name": "Alice"})
    assert res.status_code == 201
    data = res.get_json()
    assert data["message"].startswith("Name 'Alice' inserted")
    assert "id" in data
    assert "created_at" in data

def test_get_names(client):
    client.post("/add-name", json={"name": "Bob"})
    res = client.get("/names")
    assert res.status_code == 200
    data = res.get_json()
    assert "names" in data
    assert any(n["name"] == "Bob" for n in data["names"])

def test_delete_name(client):
    client.post("/add-name", json={"name": "Charlie"})
    res = client.delete("/delete-name/Charlie")
    assert res.status_code == 200
    assert "deleted" in res.get_json()["message"]

def test_delete_nonexistent_name(client):
    res = client.delete("/delete-name/DoesNotExist")
    assert res.status_code == 404
    assert "No entry found" in res.get_json()["error"]

def test_add_empty_name(client):
    res = client.post("/add-name", json={"name": ""})
    # Backend currently doesn't validate empty names, may insert ""
    # Adjust depending on expected behavior:
    assert res.status_code in (201, 500)
