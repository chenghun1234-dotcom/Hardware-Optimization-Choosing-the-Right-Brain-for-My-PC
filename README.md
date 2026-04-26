# Hardware-Optimization: Choosing the Right Brain for My PC

A high-performance FastAPI service designed to recommend the best local AI models (DeepSeek-R1) and gaming profiles based on your specific hardware specs (VRAM, RAM, CPU).

## Features
- **AI Model Matching**: Get specific models and quantization levels for your VRAM.
- **Gaming Optimization**: Suggested titles and settings.
- **SLA Dashboard**: Monitor API health.

## Quick Start
```bash
pip install -r requirements.txt
uvicorn api.index:app --reload
```
