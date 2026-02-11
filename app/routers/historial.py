from fastapi import APIRouter, Request
import requests

router = APIRouter()

@router.post("/data-historial")
async def data_historial(request: Request):
    body = await request.json()
    return {"ok": True}
