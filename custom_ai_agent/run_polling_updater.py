import time
import os
from loaders.gdrive_loader import list_files, download_file
from loaders.document_parser import extract_text_and_images_from_pdf as extract_text_from_pdf
from embedding.embedder import embed_text
from embedding.vector_store import add_to_index
import yaml

with open("configs/config.yaml") as f:
    config = yaml.safe_load(f)

folder_id = config['gdrive']['folder_id']
processed_files = {}

while True:
    files = list_files(folder_id)
    for file in files:
        file_id = file['id']
        file_name = file['name']
        modified_time = file['modifiedTime']

        if file_id not in processed_files or processed_files[file_id] != modified_time:
            filepath = download_file(file_id, file_name)
            text = extract_text_from_pdf(filepath)
            embeddings = embed_text([text])[0]
            add_to_index(text, embeddings)
            processed_files[file_id] = modified_time
            print(f"Processed file: {file_name}")

    time.sleep(300)
