from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/patente")
async def patente(request: Request):
    body = await request.json()
    answer = body.get("userInput")

    if not answer:
        return {
            "status": 1,
            "data": {
                "actions": [
                    {"type": "sendText", "text": "Indícanos el número de la patente"}
                ]
            }
        }

    if answer == "1234":
        return {
            "status": 1,
            "data": {
                "actions": [
                    {
                        "type": "sendText",
                        "text": "la fecha de caducidad es 02/03/2025",
                    }
                ]
            }
        }
