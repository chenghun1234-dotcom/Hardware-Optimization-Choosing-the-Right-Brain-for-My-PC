import os
from fastapi import Header, HTTPException

async def verify_rapidapi_secret(
    x_rapidapi_proxy_secret: str = Header(None, alias="X-RapidAPI-Proxy-Secret")
):
    expected_secret = os.environ.get("RAPIDAPI_PROXY_SECRET")
    if expected_secret and x_rapidapi_proxy_secret != expected_secret:
        raise HTTPException(status_code=403, detail="Invalid RapidAPI Secret")
    return True
