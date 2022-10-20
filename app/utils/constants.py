from pathlib import Path
from app.services.auth_service import facebook_auth_service, google_auth_service, github_auth_service, twitter_auth_service
from app.services.auth_service import google_auth_callback_service 
BASEDIR =Path(__file__).resolve().parent.parent.parent

PROVIDER_AUTH_SERVICES ={
    'facebook': facebook_auth_service,
    'github': github_auth_service,
    'google': google_auth_service,
    'twitter': twitter_auth_service, 
} 

PROVIDER_AUTH_CALLBACK_SERVICES ={
    'google': google_auth_callback_service 
}