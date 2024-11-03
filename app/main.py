from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI()

# Mount static files for CSS and JavaScript
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# Serve the HTML file
@app.get("/", response_class=HTMLResponse)
async def serve_html():
    index_path = Path("frontend/templates/index.html")
    return index_path.read_text()

# Run the server: use 'uvicorn main:app --reload' in the command line
