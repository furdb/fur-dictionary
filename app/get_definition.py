import os
import requests
import json

from converter import *
from config import *

FURDB_HOST = os.environ.get("FURDB_HOST")
FURDB_PORT = os.environ.get("FURDB_PORT")
FURDB_DATABASE_ID = os.environ.get("FURDB_DATABASE_ID")
FURDB_TABLE_ID = os.environ.get("FURDB_TABLE_ID")


def get_definition(word: str) -> str:
    url = f"{FURDB_HOST}:{FURDB_PORT}/{FURDB_DATABASE_ID}/{FURDB_TABLE_ID}/data"

    res = requests.get(url, data=json.dumps({}), headers={'content-type':'application/json'})
    res = json.loads(res.content.decode('utf8'))

    for result in res.get("results", []):
        [word_encoded, definition_encoded] = result.get("data")

        if decode(word_encoded, WORD_SIZE) == word:
            definition = decode(definition_encoded, DEFINITION_SIZE)
            return definition

    return "Not Found"