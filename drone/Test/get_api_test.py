import json
from drone.main import create_app

app = create_app('local')
tester = app.test_client()


class APPCONFIG(object) :
    ENV = 'testing'
    USERNAME = 'test'
    KEY = 'test'

def get_app_config():
    return  APPCONFIG

def test_status_code():
    config = get_app_config()
    response = tester.get('/users')
    assert response.status_code == 412


def setup():
    app = create_app(get_app_config())
    client = app.test_client()

def sign_get(url,headers,query,**kwargs):
    content_type = None
    if 'data' in kwargs:
        kwargs['data'] = json.dumps(kwargs['data'])
        content_type = 'application/json'
