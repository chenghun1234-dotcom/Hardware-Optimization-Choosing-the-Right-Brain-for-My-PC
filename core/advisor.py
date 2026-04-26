"""Advanced Hardware Advisor Engine v2.0"""

def get_ai_recommendations(vram, ram, cpu):
    if vram >= 24:
        return {"model": "DeepSeek-R1:32b/70b", "quant": "Q4_K_M", "use_case": "Professional"}
    elif vram >= 14:
        return {"model": "DeepSeek-R1:14b", "quant": "Q8_0", "use_case": "Business"}
    return {"model": "DeepSeek-R1:8b", "quant": "F16", "use_case": "Speed"}

def get_game_recommendations(vram, gpu_model):
    if vram >= 12:
        return {"tier": "4K Ultra", "games": ["Cyberpunk 2077", "Alan Wake 2"]}
    return {"tier": "1080p Ultra", "games": ["Forza Horizon 5", "Apex Legends"]}

def calculate_optimization_score(vram, ram, cpu):
    return {"power_score": (vram * 2) + ram, "tier": "High-End"}
