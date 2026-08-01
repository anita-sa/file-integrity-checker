import json
import os

DATABASE_FILE = "hashes.json"


def load_hashes():

    if not os.path.exists(DATABASE_FILE):
        return {}

    try:
        with open(DATABASE_FILE, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return {}



def save_hash(file_name, file_hash):

    hashes = load_hashes()

    hashes[file_name] = file_hash

    with open(DATABASE_FILE, "w") as file:
        json.dump(hashes, file, indent=4)



def get_hash(file_name):

    hashes = load_hashes()

    return hashes.get(file_name)