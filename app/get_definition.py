import os
import requests
import json

from converter import encode, decode

FURDB_HOST = os.environ.get("FURDB_HOST")
FURDB_PORT = os.environ.get("FURDB_PORT")
FURDB_DATABASE_ID = os.environ.get("FURDB_DATABASE_ID")
FURDB_TABLE_ID = os.environ.get("FURDB_TABLE_ID")


def get_definition(word: str) -> str:
    url = f"{FURDB_HOST}:{FURDB_PORT}/{FURDB_DATABASE_ID}/{FURDB_TABLE_ID}/data"
    word_encoded = encode(word)

    body = {
        "entries": {
            "value": {
                "columnIndex": 0,
                "value": word_encoded,
            }
        }
    }

    res = requests.get(
        url, data=json.dumps(body), headers={"content-type": "application/json"}
    )

    res = json.loads(res.content.decode("utf8"))

    if res.get("response").get("resultCount") > 0:
        definition_encoded = res.get("response").get("results")[0].get("data")[1]
        definition = decode(definition_encoded)
    else:
        definition = "Not Found"

    return definition
