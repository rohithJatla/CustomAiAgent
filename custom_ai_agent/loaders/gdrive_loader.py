from googleapiclient.discovery import build
from google.oauth2 import service_account
import io
import os
from googleapiclient.http import MediaIoBaseDownload
import yaml

with open("configs/config.yaml") as f:
    config = yaml.safe_load(f)

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def get_drive_service():
    creds = service_account.Credentials.from_service_account_file(
        config['gdrive']['service_account_file'], scopes=SCOPES)
    service = build('drive', 'v3', credentials=creds)
    return service

def list_files(folder_id):
    service = get_drive_service()
    query = f"'{folder_id}' in parents and trashed=false"
    results = service.files().list(q=query, fields="files(id, name, mimeType, modifiedTime)").execute()
    return results.get('files', [])

def download_file(file_id, file_name, download_path="data/"):
    service = get_drive_service()
    os.makedirs(download_path, exist_ok=True)
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(os.path.join(download_path, file_name), 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
    return os.path.join(download_path, file_name)
