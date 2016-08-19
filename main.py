from flask import Flask

def create_app():
    app = Flask(__name__)
    #configure your app here
    init_app(app)
    return app

#initzalize your app here
def init_app(app):

    from drone import api_start

    app.register_blueprint(api_start.api)