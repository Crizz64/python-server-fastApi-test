from fastapi import FastAPI
from app.routes import (
    patente,
    pedido,
    callbacks,
    intranet,
    archivos,
    historial
)

app = FastAPI(title="Servidor de Callbacks Local")

app.include_router(patente.router)
app.include_router(pedido.router)
app.include_router(callbacks.router)
app.include_router(intranet.router)
app.include_router(archivos.router)
app.include_router(historial.router)