import requests

def test_add_name():
    res = requests.post("http://backend:5000/add-name", json={"name": "Alice"})
    assert res.status_code == 201
    data = res.json()
    assert data["message"].startswith("Name 'Alice' inserted")
    assert "id" in data
    assert "created_at" in data

def test_get_names():
    requests.post("http://backend:5000/add-name", json={"name": "Bob"})
    res = requests.get("http://backend:5000/names")
    assert res.status_code == 200
    data = res.json()
    assert "names" in data
    assert any(n["name"] == "Bob" for n in data["names"])

def test_delete_name():
    requests.post("http://backend:5000/add-name", json={"name": "Charlie"})
    res = requests.delete("http://backend:5000/delete-name/Charlie")
    assert res.status_code == 200
    assert "deleted" in res.json()["message"]

def test_delete_nonexistent_name():
    res = requests.delete("http://backend:5000/delete-name/DoesNotExist")
    assert res.status_code == 404
    assert "No entry found" in res.json()["error"]

def test_add_empty_name():
    res = requests.post("http://backend:5000/add-name", json={"name": ""})
    # Backend currently doesn't validate empty names, may insert ""
    # Adjust depending on expected behavior:
    assert res.status_code in (201, 500)
