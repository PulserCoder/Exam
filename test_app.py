import pytest
from flask import Flask, json
from app import app as flask_app

@pytest.fixture
def app():
    return flask_app

@pytest.fixture
def client(app: Flask):
    return app.test_client()

def test_get_all_schedules(client: Flask):
    response = client.get("/schedules/")
    assert response.status_code == 200



def test_delete_schedule(client: Flask):
    response = client.delete("/schedules/1")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["message"] == "successfully"

