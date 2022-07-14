from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    args = request.args

    word = None
    definition = None

    if args.get("word"):
        url = "http://127.0.0.1:8080/Dictionary/dictionary/data"
        data = {
            "query": {
                "column_id": "word",
                "value": args.get("word")
            }
        }
        res = requests.get(url, data=json.dumps(data), headers={'content-type':'application/json'})
        res = json.loads(res.content.decode('utf8').replace("'", '"'))
        res = res.get("result")[0]

        print(res)

        word = res.get("word")
        definition = res.get("definition")

    return render_template("home.html", word=word, definition=definition)

if __name__ == "__main__":
    app.run(debug=True, port=5500)