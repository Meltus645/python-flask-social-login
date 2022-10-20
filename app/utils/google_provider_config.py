from os import getenv
from dotenv import load_dotenv
import requests

load_dotenv()
def provider_config():
    GOOGLE_DISCOVERY_URL =getenv('GOOGLE_DISCOVERY_URL')
    provider_config =requests.get(GOOGLE_DISCOVERY_URL) 
    return provider_config.json()   
