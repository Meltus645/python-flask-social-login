from dotenv import load_dotenv 
import os, json, sqlite3, requests 
from oauthlib.oauth2 import WebApplicationClient
from flask import redirect, request 
from app.utils.google_web_client import google_web_client

load_dotenv()   
def logout_service(): pass
def callback_service(): pass

def manual_auth_service(credentials): 
    return credentials 

def web_client():
    GOOGLE_CLIENT_ID =os.getenv('GOOGLE_CLIENT_ID') 
    client =WebApplicationClient(GOOGLE_CLIENT_ID) 
    return client


def google_auth_service():  
    client, configs =google_web_client(['authorization_endpoint']) 
    authorization_endpoint =configs.get('authorization_endpoint')
    request_uri =client.prepare_request_uri( 
        authorization_endpoint,
        redirect_uri=f"{'/'.join(request.base_url.split('/')[:-1])}/callback/google",
        scope=['openid', 'email', 'profile']
    )
    return redirect(request_uri)


def twitter_auth_service():
    pass

def facebook_auth_service():
    pass

def github_auth_service():
    pass


def google_auth_callback_service():
    code =request.args.get('code') 
    client, configs =google_web_client(['authorization_endpoint', 'userinfo_endpoint'])  
    token_endpoint =configs.get('token_endpoint') 
    token_url, headers, body =client.prepare_token_request(
        token_url=token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code =code
    )

    token_response =requests.post(
        token_url, headers =headers, data =body,
        auth =(os.getenv('GOOGLE_CLIENT_ID'), os.getenv('GOOGLE_CLIENT_SECRET'))
    )

    client.parse_request_body_response(json.dumps(token_response.json()))
    userinfo_endpoint = configs.get('userinfo_endpoint')
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body) 
    return userinfo_response.json()