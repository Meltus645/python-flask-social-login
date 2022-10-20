import requests, os  
from dotenv import load_dotenv
from oauthlib.oauth2 import WebApplicationClient

load_dotenv()
def google_web_client(request:list)->tuple:
    GOOGLE_DISCOVERY_URL =os.getenv('GOOGLE_DISCOVERY_URL')
    provider_config =requests.get(GOOGLE_DISCOVERY_URL) 
    provider_config_json = provider_config.json() 
    GOOGLE_CLIENT_ID =os.getenv('GOOGLE_CLIENT_ID') 
    client =WebApplicationClient(GOOGLE_CLIENT_ID)  
    if type(request) is str: request =[request]

    return client, {req: provider_config_json.get(req) for req in request}  