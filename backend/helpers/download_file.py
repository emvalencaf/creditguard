from io import BytesIO
import io
import aiohttp
from os.path import join,abspath,dirname
import asyncio
from googleapiclient.http import MediaIoBaseDownload

from cloud import get_google_drive_service

# Where models folder in the deployed backend
REMOTE_MODEL_FOLDER = "./artifacts/models"

async def download_google_drive_file(file_id: str,
                                     local_filename: str) -> str:
    """
    Asynchronously downloads a file from Google Drive and saves it locally.

    :param file_id: The ID of the file in Google Drive.
    :param local_filename: The name to save the file locally.
    :return: The local file path where the file is saved.
    """
    service = get_google_drive_service()
    file_path = join(REMOTE_MODEL_FOLDER, local_filename)

    await asyncio.to_thread(download_file, service, file_id, file_path)

    return file_path


def download_file(service, file_id: str, file_path: str):
    """
    Synchronously downloads a file from Google Drive and saves it locally.

    :param service: Authenticated Google Drive service instance.
    :param file_id: The ID of the file to be downloaded.
    :param file_path: The local file path to save the model.
    """
    request = service.files().get_media(fileId=file_id)
    
    with open(file_path, "wb") as file:
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while not done:
            _, done = downloader.next_chunk()