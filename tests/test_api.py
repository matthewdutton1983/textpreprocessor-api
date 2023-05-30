import pytest
from flask import json
from api import app


@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert data['message'] == 'Server is running'


def test_methods(client):
    response = client.get('/methods')
    assert response.status_code == 200


def test_pipeline_no_json(client):
    response = client.post('/pipeline')
    assert response.status_code == 400


def test_pipeline_no_text(client):
    response = client.post('/pipeline', json={})
    assert response.status_code == 400


def test_unknown_route(client):
    response = client.get('/unknown')
    assert response.status_code == 404
