from flask import request, jsonify, redirect, url_for, session
from app.services.auth_service import manual_auth_service
from app.utils.constants import PROVIDER_AUTH_SERVICES, PROVIDER_AUTH_CALLBACK_SERVICES

def login(provider =None): 
    """
        Authenticate and manage user sessions

        :param provider {str} - provider to navigate to. 
    """ 
    service =PROVIDER_AUTH_SERVICES.get(provider)()
    if request.method =='POST':
        form =request.form
        service =manual_auth_service({**form})  
    if not service: return {'error': 'Page Not Found'}

    return service

def callback(provider:str): 

    """
        Provider callback view. Bridge between the provider auth service and the client app

        :param provider {str} - the provider from which we are fetching the data
        :returns data {dict} - the client information received from the callback url
    """
    service =PROVIDER_AUTH_CALLBACK_SERVICES.get(provider)() 
    return service

def logout(): 
    """
        Ends user session and redirects user to the login screen
    """
    session.clear()
    session =None
    return redirect(url_for('public.home'))