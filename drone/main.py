from flask import Flask
import os.path as op
from flask_sqlalchemy import SQLAlchemy

#---- db instance ---#

db = SQLAlchemy()

#----- create flask instance and config flask -----#
def create_app(config,config_override=None):
    """
    Application factory
    Args:
        config:             Extra config to load
        config_override:    Configuration object or filename to override

    """
    global  app
    app = Flask(__name__)

    # add Route log
    #app.after_request(log_route)

    #configure your app here
    load_config(app, config, config_override)

    init_app(app)
    return app

#initzalize your app here
def init_app(app):

    from drone import api_start

    app.register_blueprint(api_start.api)


def load_config(app,extra_config=None,override=None):
    """
    Load config to given application
    * ``/<app_root>/config/config_common.py``
            Required file with common configs.
    * ``extra_config`` - Optional path to file or configuration name.
      If it's a relative path then ``/<app_root>/config/<extra_config>``
      will be used.

      If ``extra_config`` has no ``.py`` extension then it will be appended.

    Args:
        app: Flask application object.
        extra_config: Path to configuration file or configuration name.


        For example you want to load ``myconfig.py``::

        load_config(app, 'myconfig.py')

        # it will load:
        # /<app_root>/config/config_common.py
        # /<app_root>/config/myconfig.py
        # /<app_root>/config/config_override.py

    Returns:

    """

    app._loaded_config_list = []
    _do_load_config(app, 'common.py')





def _do_load_config(application, filename, silent=False):
    """Load configuration to the application.

    Args:
        application: Flask application
        filename: Configuration name or file path.
        silent: Don't raise exception if the config is not present.
    """
    filename = op.expanduser(op.expandvars(filename))

    if not filename.endswith('.py'):
        filename += '.py'

    if filename.startswith('.'):
        filename = op.abspath(filename)

    if not op.isabs(filename):
        # Load /<app_root>/config/<filename>
        filename = op.join(application.root_path, 'config', filename)

    if not silent or op.exists(filename):
        application.logger.info('Loading configuration [%s] ...', filename)

    if not silent and not op.exists(filename):
        raise MissingConfigurationError(filename)

    application.config.from_pyfile(filename, silent=silent)

    # See load_config().
    application._loaded_config_list.append(filename)




class MissingConfigurationError(Exception):
    def __init__(self, filename):
        self.filename = filename
        Exception.__init__(self, filename)