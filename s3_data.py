import requests
import json
import gzip
import shutil
import time
import os
from io import BytesIO
import xml.etree.ElementTree as ET 

S3_BUCKET_URL = "https://vcthackathon-data.s3.us-west-2.amazonaws.com"

# (game-changers, vct-international, vct-challengers)
LEAGUE = "game-changers"

# (2022, 2023, 2024)
YEAR = 2024

def download_gzip_and_write_to_json(file_name):
    if os.path.isfile(f"{file_name}.json"):
        return False

    remote_file = f"{S3_BUCKET_URL}/{file_name}.json.gz"
    response = requests.get(remote_file, stream=True)

    if response.status_code == 200:
        gzip_bytes = BytesIO(response.content)
        with gzip.GzipFile(fileobj=gzip_bytes, mode="rb") as gzipped_file:
            with open(f"{file_name}.json", 'wb') as output_file:
                shutil.copyfileobj(gzipped_file, output_file)
            print(f"{file_name}.json written")
        return True
    elif response.status_code == 404:
        # Ignore
        return False
    else:
        print(response)
        print(f"Failed to download {file_name}")
        return False


def download_esports_files():
    directory = f"{LEAGUE}/esports-data"

    if not os.path.exists(directory):
        os.makedirs(directory)

    esports_data_files = ["leagues", "tournaments",
                          "players", "teams", "mapping_data"]
    for file_name in esports_data_files:
        download_gzip_and_write_to_json(f"{directory}/{file_name}")


def download_games():
    start_time = time.time()

    local_mapping_file = f"{LEAGUE}/esports-data/mapping_data.json"
    with open(local_mapping_file, "r") as json_file:
        mappings_data = json.load(json_file)

    local_directory = f"{LEAGUE}/games/{YEAR}"
    if not os.path.exists(local_directory):
        os.makedirs(local_directory)

    game_counter = 0

    for esports_game in mappings_data:
        s3_game_file = f"{LEAGUE}/games/{YEAR}/{esports_game["platformGameId"]}"

        response = download_gzip_and_write_to_json(s3_game_file)
        
        if (response == True):
            game_counter += 1
            if game_counter % 10 == 0:
                print(f"----- Processed {game_counter} games, current run time: {
                    round((time.time() - start_time)/60, 2)} minutes")


def download_fandom_files():
    directory = "fandom"
    if not os.path.exists(directory):
        os.makedirs(directory)

    fandom_url = f"{S3_BUCKET_URL}/?prefix={directory}/"
    response = requests.get(fandom_url)

    if response.status_code == 200:
        root = ET.fromstring(response.content)
        namespace = {'s3': 'http://s3.amazonaws.com/doc/2006-03-01/'}
        for content in root.findall('s3:Contents', namespace):
            key = content.find('s3:Key', namespace).text
            if key.endswith('.xml.gz'):
                file_name = os.path.basename(key)
                file_url = f"{S3_BUCKET_URL}/{key}"
                local_file_path = os.path.join(directory, file_name[:-3])  # Remove .gz extension
                
                if not os.path.isfile(local_file_path):
                    print(f"Downloading {file_name}")
                    file_response = requests.get(file_url, stream=True)
                    if file_response.status_code == 200:
                        with gzip.open(file_response.raw, 'rb') as f_in:
                            with open(local_file_path, 'wb') as f_out:
                                shutil.copyfileobj(f_in, f_out)
                        print(f"Downloaded and extracted {file_name}")
                    else:
                        print(f"Failed to download {file_name}")
    else:
        print(f"Failed to list fandom directory contents")



if __name__ == "__main__":
    #download_esports_files()
    #download_games()
    download_fandom_files()
