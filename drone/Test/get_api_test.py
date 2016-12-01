import json
from drone.main import create_app

app = create_app('local')
tester = app.test_client()


class APPCONFIG(object) :
    ENV = 'testing'
    USERNAME = 'test'
    KEY = 'test'



def test_status_code():
    response = tester.get('/users')
    assert response.status_code == 412




class CommonTestCase():

    def get_app_config(self):
        return APPCONFIG

    def setup(self):
        self.app = create_app(self.get_app_config())
        self.client = self.app.test_client()

    def sign_get(self,url, headers, query, **kwargs):
        content_type = None
        if 'data' in kwargs:
            kwargs['data'] = json.dumps(kwargs['data'])
            content_type = 'application/json'