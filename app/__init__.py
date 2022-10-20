from flask import Flask
from app.utils.constants import BASEDIR
from app.routes import auth, public 
# from app.utils.login_manager import manage_login

def createapp(test_config:dict =None)->Flask:
    """
    Creates and returns a new Flask app instance

    :param test_config? {dict} - app test configurations
    :return app {Flask} - Flask instance created 
    """

    app =Flask(__name__, template_folder =BASEDIR /'templates', static_folder =BASEDIR /'static')

    if test_config: app.config.from_object(test_config)
    else: app.config.from_pyfile(BASEDIR /'config.py') 
    # manage_login(app =app)

    app.register_blueprint(public, url_prefix ='/')
    app.register_blueprint(auth, url_prefix ='/auth')

    return app