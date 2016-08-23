from drone.main import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand

#setup your app
def setup_app(config):
    app =create_app(config)
    migrate.init_app(app,db)
    #migrate
    return app
migrate =Migrate()

manager = Manager(setup_app,help='Manage script')
manager.add_command("runserver",Server())
manager.add_command("db",MigrateCommand)
manager.add_option('--app-config',dest='config',default='local',help='Application config load ')

if __name__ == "__main__":
    manager.run()
