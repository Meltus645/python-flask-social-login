from app.views.auth_view import login, logout, callback
from flask import Blueprint

auth =Blueprint('auth', __name__)

auth.route('', methods =['GET','POST'])(login)
auth.route('<string:provider>-auth', methods =['GET','POST'])(login)
auth.route('/callback/<string:provider>', methods =['GET'])(callback)
auth.route('/logout', methods =['GET'])(logout)