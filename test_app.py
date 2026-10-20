import pytest
import app as app_module


@pytest.fixture
def client():
    app_module.tasks.clear()
    app_module.app.config["TESTING"] = True
    with app_module.app.test_client() as c:
        yield c


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}


def test_home_page(client):
    assert client.get("/").status_code == 200


def test_add_and_list_task(client):
    res = client.post("/api/tasks", json={"title": "Write report"})
    assert res.status_code == 201
    assert res.get_json()["title"] == "Write report"
    assert len(client.get("/api/tasks").get_json()) == 1


def test_add_task_without_title(client):
    assert client.post("/api/tasks", json={}).status_code == 400


def test_toggle_task(client):
    tid = client.post("/api/tasks", json={"title": "A"}).get_json()["id"]
    assert client.put(f"/api/tasks/{tid}").get_json()["done"] is True


def test_delete_task(client):
    tid = client.post("/api/tasks", json={"title": "A"}).get_json()["id"]
    assert client.delete(f"/api/tasks/{tid}").status_code == 204
    assert client.get("/api/tasks").get_json() == []


def test_not_found(client):
    assert client.put("/api/tasks/999").status_code == 404
    assert client.delete("/api/tasks/999").status_code == 404
