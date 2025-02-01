from google.oauth2 import service_account
from googleapiclient.discovery import build

# Project directory
from config import global_settings

def get_cloud_scope_policies():
    """
    Retrieves the required scope policies for Google Drive API access.

    :return: A list of OAuth 2.0 scope policies for Google Drive.
    """
    return ["https://www.googleapis.com/auth/drive"]

def get_credentials_config():
    """
    Creates Google API credentials using a service account.

    :return: An authenticated `Credentials` object for Google Drive API access.
    """
    scope_policies = get_cloud_scope_policies()

    creds_info = {
        "project_id": global_settings.GOOGLE_API_PROJECT_ID,
        "client_id": global_settings.GOOGLE_API_SERVICE_ID,
        "client_email": global_settings.GOOGLE_API_SERVICE_EMAIL,
        "private_key_id": global_settings.GOOGLE_API_SERVICE_PRIVATE_KEY_ID,
        "private_key": global_settings.GOOGLE_API_SERVICE_PRIVATE_KEY,
        "token_uri": "https://oauth2.googleapis.com/token",
        "universe_domain": "googleapis.com",
    }

    creds = service_account.Credentials.from_service_account_info(
        info=creds_info, scopes=scope_policies
    )
    return creds

def get_google_drive_service():
    """
    Initializes and returns a Google Drive API service instance.

    :return: A `Resource` object for interacting with Google Drive API.
    """
    creds = get_credentials_config()
    return build("drive", "v3", credentials=creds)