from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/intranet")
async def intranet(request: Request):
    body = await request.json()
    inputs = body.get("inputs", {})
    answer = body.get("userInput")
    documento = inputs.get("num_documento")

    mensaje = """👋 Bienvenido, Brian

1️⃣ Consultar salario
2️⃣ Consultar inventario
3️⃣ Consultar vacaciones
"""

    if documento == "12345" or answer == "12345":
        return {
            "status": 1,
            "data": {
                "actions": [{"type": "sendText", "text": mensaje}]
            },
        }

    return {
        "status": 1,
        "data": {
            "actions": [
                {
                    "type": "sendText",
                    "text": "El documento no existe, por favor revísalo.",
                },
                {"type": "input"},
            ]
        },
    }
