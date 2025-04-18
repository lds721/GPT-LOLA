from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="API para Reparto Económico",
    description="Esta API permite calcular el reparto de ahorro en costes y beneficios en inversión conjunta.",
    version="1.0.0"
)

app.include_router(router)
