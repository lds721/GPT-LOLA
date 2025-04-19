from fastapi import FastAPI
from app.routes import router

# Instancia principal de la API
app = FastAPI(
    title="API GPT-LOLA: Reparto Económico",
    description="Servicio para calcular el reparto de costes y beneficios usando modelos proporcionales y logarítmicos.",
    version="1.0.0"
)

# Incluimos todas las rutas definidas en routes.py
app.include_router(router)
