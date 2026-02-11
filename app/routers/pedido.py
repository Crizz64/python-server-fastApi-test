from fastapi import APIRouter, Request

@app.post("/pedido")
async def pedido(request: Request):
    body = await request.json()
    inputs = body.get("inputs", {})
    respuesta_cliente = body.get("userInput")
    pedido = inputs.get("pedido")

    print("Respuesta cliente:", respuesta_cliente)

    if not pedido:
        return {
            "status": 1,
            "status_message": "Ok",
            "data": {
                "actions": [
                    {
                        "type": "sendText",
                        "text": "Ingresa el id de tu pedido. (Pedidos de prueba: 12345 y 67890)",
                    },
                    {"type": "input"},
                ]
            },
        }

    valor = respuesta_cliente or pedido

    respuestas = {
        "12345": "El pedido 12345 está en camino",
        "67890": "El pedido 67890 está en camino",
        "si": "si",
        "no": "no",
    }

    respuesta = respuestas.get(valor)

    if respuesta is None:
        return {
            "status": 1,
            "status_message": "Ok",
            "data": {
                "actions": [
                    {"type": "sendText", "text": "Te vamos a transferir al bot de nuevo"},
                    {"type": "teamDelegate", "id_team": "5559"},
                    {"type": "input"},
                ]
            },
        }

    if respuesta == "si":
        return {
            "status": 1,
            "status_message": "Ok",
            "data": {
                "actions": [
                    {"type": "sendText", "text": "Ingresa el id de tu pedido."},
                    {"type": "input"},
                ]
            },
        }

    if respuesta == "no":
        return {
            "status": 1,
            "status_message": "Ok",
            "data": {
                "actions": [
                    {"type": "sendText", "text": "Ok, hasta pronto."},
                    {"type": "userDelegate", "id_user": "36909"},
                ]
            },
        }

    return {
        "status": 1,
        "status_message": "Ok",
        "data": {
            "actions": [
                {"type": "sendText", "text": respuesta},
                {
                    "type": "sendText",
                    "text": "Quieres consultar otro pedido? (Escribe 'si' o 'no')",
                },
                {"type": "input"},
            ]
        },
    }
