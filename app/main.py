from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from get_definition import get_definition
from prepare import prepare

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request, word: str = None):
    prepare()

    definition = None
    if word:
        definition = get_definition(word)
    return templates.TemplateResponse(
        "home.html",
        {"request": request, "word": word, "definition": definition},
        context={"request": request},
    )


if __name__ == "__main__":
    app.run(debug=True, port=5500)
