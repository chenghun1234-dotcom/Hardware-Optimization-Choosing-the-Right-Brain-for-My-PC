import time
from fastapi import APIRouter, Security
from api.models import HardwareSpecs
from api.auth import verify_rapidapi_secret
from core.advisor import get_ai_recommendations, get_game_recommendations, calculate_optimization_score

router = APIRouter()

def _wrap(data: dict, endpoint: str, elapsed_ms: float) -> dict:
    return {
        "status": "success",
        "api": "Hardware-Match AI Advisor v1.0",
        "endpoint": endpoint,
        "elapsed_ms": round(elapsed_ms, 2),
        "data": data
    }

@router.post("/match/ai", tags=["Advisory"])
async def match_ai(
    body: HardwareSpecs,
    _: bool = Security(verify_rapidapi_secret)
):
    """Highly sophisticated AI model matching including Quantization and Bottlenecks."""
    t0 = time.perf_counter()
    ai_data = get_ai_recommendations(body.vram_gb, body.ram_gb, body.cpu_cores)
    return _wrap(ai_data, "/match/ai", (time.perf_counter() - t0) * 1000)

@router.post("/match/games", tags=["Advisory"])
async def match_games(
    body: HardwareSpecs,
    _: bool = Security(verify_rapidapi_secret)
):
    """Suggest games based on GPU model and VRAM."""
    t0 = time.perf_counter()
    games = get_game_recommendations(body.vram_gb, body.gpu_model)
    return _wrap(games, "/match/games", (time.perf_counter() - t0) * 1000)
