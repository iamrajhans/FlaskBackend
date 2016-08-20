from drone.main import create_app
from flask_script import Manager,Server


#setup your app
def setup_app(config):
    app =create_app(config)
    #migrate
    return app


manager = Manager(setup_app,help='Manage script')
manager.add_command("runserver",Server())
manager.add_option('--app-config',dest='config',default='local',help='Application config load ')

if __name__ == "__main__":
    manager.run()