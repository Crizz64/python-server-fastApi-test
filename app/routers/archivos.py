from fastapi import APIRouter

router = APIRouter()

@router.post("/enviar-archivo")
async def enviar_archivo():
    return {
        "status": 1,
        "data": {
            "actions": [
                {"type": "sendText", "text": "Te comparto un archivo PDF"},
                {
                    "type": "sendFile",
                    "url": "https://cdn.liveconnect.chat/421/lc/2/biblioteca/1815/60739/manual_de_conexion_canales_whatsapp_api_cloud_actualizado_ene25.pdf",
                },
            ]
        },
    }
