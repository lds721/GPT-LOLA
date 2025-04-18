from fastapi import APIRouter
from pydantic import BaseModel
from core.calculator import calcular_reparto

router = APIRouter()

class InputDatos(BaseModel):
    cantidades: list[float]
    tipo: str  # 'coste' o 'beneficio'

@router.post("/reparto")
def calcular(data: InputDatos):
    df = calcular_reparto(data.tipo, data.cantidades)
    resultado = df.to_dict(orient='records')
    return {"reparto": resultado}
