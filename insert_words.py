import requests
import json

from converter import *
from config import *

def generate():
    delete_database()
    create_database()
    create_table()
    insert_words()
    words = get_words()

    return words


def delete_database():
    # TODO
    pass


def create_database():
    url = f"{FURDB_HOST}:{FURDB_PORT}/{FURDB_DATABASE_ID}"

    data = {
        "database_name": "Dictionary"
    }

    requests.post(url, data=json.dumps(data), headers={'content-type':'application/json'})


def create_table():
    url = f"{FURDB_HOST}:{FURDB_PORT}/{FURDB_DATABASE_ID}/{FURDB_TABLE_ID}"

    data = {
        "table_name": "Dictionary",
        "table_columns": [
            {
                "name": "Word",
                "size": 44
            },
            {
                "name": "Definition",
                "size": 76
            }
        ]
    }

    requests.post(url, data=json.dumps(data), headers={'content-type':'application/json'})


def insert_words():
    url = f"{FURDB_HOST}:{FURDB_PORT}/{FURDB_DATABASE_ID}/{FURDB_TABLE_ID}/data"

    data = {
        "data": [
            [encode(word), encode(definition)] for word, definition in WORDS
        ]
    }

    res = requests.post(url, data=json.dumps(data), headers={'content-type':'application/json'})
    res = json.loads(res.content.decode('utf8'))


def get_words():
    url = f"{FURDB_HOST}:{FURDB_PORT}/{FURDB_DATABASE_ID}/{FURDB_TABLE_ID}/data"

    data = {}

    res = requests.get(url, data=json.dumps(data), headers={'content-type':'application/json'})
    res = json.loads(res.content.decode('utf8'))

    res = res.get("results", [])

    decoded = [[decode(r.get("data")[0], WORD_SIZE), decode(r.get("data")[1], DEFINITION_SIZE)] for r in res]

    return decoded