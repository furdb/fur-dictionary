import os
import requests
import json

from converter import encode, decode
from config import WORDS, WORD_SIZE, DEFINITION_SIZE

FURDB_HOST = os.environ.get("FURDB_HOST")
FURDB_PORT = os.environ.get("FURDB_PORT")
FURDB_DATABASE_ID = os.environ.get("FURDB_DATABASE_ID")
FURDB_TABLE_ID = os.environ.get("FURDB_TABLE_ID")


def prepare():
    delete_database()
    create_database()
    create_table()
    insert_words()


def delete_database():
    url = f"{FURDB_HOST}:{FURDB_PORT}/{FURDB_DATABASE_ID}"
    requests.delete(url)


def create_database():
    url = f"{FURDB_HOST}:{FURDB_PORT}/{FURDB_DATABASE_ID}"
    requests.post(url)


def create_table():
    url = f"{FURDB_HOST}:{FURDB_PORT}/{FURDB_DATABASE_ID}/{FURDB_TABLE_ID}"

    data = {
        "tableColumns": [
            {"size": WORD_SIZE},
            {"size": DEFINITION_SIZE},
        ],
    }

    requests.post(
        url, data=json.dumps(data), headers={"content-type": "application/json"}
    )


def insert_words():
    url = f"{FURDB_HOST}:{FURDB_PORT}/{FURDB_DATABASE_ID}/{FURDB_TABLE_ID}/data"

    data = {"data": [[encode(word), encode(definition)] for word, definition in WORDS]}

    requests.post(
        url, data=json.dumps(data), headers={"content-type": "application/json"}
    )


def get_words():
    url = f"{FURDB_HOST}:{FURDB_PORT}/{FURDB_DATABASE_ID}/{FURDB_TABLE_ID}/data"

    data = {}

    res = requests.get(
        url, data=json.dumps(data), headers={"content-type": "application/json"}
    )
    res = json.loads(res.content.decode("utf8"))

    res = res.get("results", [])

    decoded = [
        [decode(r.get("data")[0], WORD_SIZE), decode(r.get("data")[1], DEFINITION_SIZE)]
        for r in res
    ]

    return decoded
