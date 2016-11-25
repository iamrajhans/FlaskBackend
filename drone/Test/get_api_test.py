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
    response = tester.get('/users')
    assert response.status_code == 412

