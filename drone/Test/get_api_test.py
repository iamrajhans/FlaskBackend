import pytest
from drone.main import create_app

def test_users_api():
    app = create_app('local')
    tester = app.test_client()
    response = tester.get('/users')
    assert response.status_code == 412