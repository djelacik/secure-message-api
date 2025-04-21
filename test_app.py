import pytest
from app import create_app, db
from app.models import Message
from test_config import TestConfig

@pytest.fixture
def client():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        yield app.test_client()

def test_send_and_retrieve_message(client):
    #post / send message
    response = client.post("/send", json={"content": "This is a test message"})
    assert response.status_code == 201

    #get / fetch message
    response = client.get("/messages")
    assert response.status_code == 200
    data = response.get_json()

    assert len(data) == 1
    assert data[0]["content"] == "This is a test message"