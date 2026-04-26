import sys
import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
sys.path.insert(0, _ROOT)

from api.router import router as core_router

app = FastAPI(
    title="Hardware-Match AI Advisor: Local LLM & Gaming Optimizer",
    description="Find the best DeepSeek-R1 models and games for your specific PC specs (VRAM, RAM, CPU).",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ASSETS_DIR = Path(_ROOT) / "static_assets"
if ASSETS_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(ASSETS_DIR)), name="static")

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def landing_page():
    html_path = ASSETS_DIR / "index.html"
    if html_path.exists():
        return html_path.read_text(encoding="utf-8")
    return HTMLResponse("<h1>Hardware-Match AI API Operational</h1>")

@app.get("/dashboard", response_class=HTMLResponse, include_in_schema=False)
async def dashboard_page():
    html_path = ASSETS_DIR / "dashboard.html"
    if html_path.exists():
        return html_path.read_text(encoding="utf-8")
    return HTMLResponse("<h1>SLA Dashboard Not Found</h1>")

@app.get("/health", tags=["System"])
async def health():
    return {"status": "operational", "version": "1.0.0"}

@app.get("/ping", tags=["System"], include_in_schema=False)
async def ping():
    return "pong"

app.include_router(core_router)
