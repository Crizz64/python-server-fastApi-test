from fastapi import APIRouter, Request
import asyncio

router = APIRouter()

@router.post("/callback-timeout")
async def callback_timeout(request: Request):
    await asyncio.sleep(5)
    return {
        "status": 1,
        "data": {
            "actions": [
                {"type": "sendText", "text": "Hola desde callback"}
            ]
        }
    }
