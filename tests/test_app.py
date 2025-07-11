import pytest
from main import app

@pytest.fixture


def client():
    with app.test_client() as client:
        yield client


def test_hello_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello from test2!" in response.data


def test_add_valid(client):
    response = client.get('/add?a=5&b=7')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["result"] == 12.0


def test_add_invalid(client):
    response = client.get('/add?a=five&b=six')
    json_data = response.get_json()
    assert response.status_code == 400
    assert "error" in json_data
    