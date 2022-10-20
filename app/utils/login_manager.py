from flask_login import LoginManager
from app.models.userModel import UserModel

def manage_login(app):
    login_manager =LoginManager()
    login_manager.init_app(app=app)  
    return login_manager