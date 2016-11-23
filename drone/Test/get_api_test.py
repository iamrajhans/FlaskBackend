import unittest
from drone.main import create_app

app = create_app('local')
tester = app.test_client()

def test_status_code():
    response = tester.get('/users')
    assert response.status_code == 412

