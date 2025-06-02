from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
#templates = Jinja2Templates(directory="templates")
templates = Jinja2Templates(directory="static")

OLLAMA_API = "http://localhost:11434/api/generate"

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "response": ""})

@app.post("/", response_class=HTMLResponse)
async def chat(request: Request, prompt: str = Form(...)):
    response_text = await get_mistral_response(prompt)
    return templates.TemplateResponse("index.html", {"request": request, "response": response_text, "prompt": prompt})

async def get_mistral_response(prompt: str) -> str:
    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_API, json=payload)
        response.raise_for_status()
        return response.json().get("response", "[No response received]")
    except Exception as e:
        return f"Error communicating with model: {e}"
