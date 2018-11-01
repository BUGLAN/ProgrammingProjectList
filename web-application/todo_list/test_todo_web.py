from todo_web import app
import pytest


@pytest.fixture
def test_flask_app():
    pass


def test_root_api():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert 'todo 小网站'.encode() in response.get_data()
