from core.models import (
    reparto_proporcional_costes,
    reparto_logaritmico_costes,
    reparto_proporcional_beneficios,
    reparto_logaritmico_beneficios
)
from core.plot_utils import mostrar_comparativa

import pandas as pd
import streamlit as st


def calcular_reparto(tipo, cantidades):
    """
    tipo: 'coste' o 'beneficio'
    cantidades: lista de números positivos
    """
    if tipo == 'coste':
        prop = reparto_proporcional_costes(cantidades)
        loga = reparto_logaritmico_costes(cantidades)
    elif tipo == 'beneficio':
        prop = reparto_proporcional_beneficios(cantidades)
        loga = reparto_logaritmico_beneficios(cantidades)
    else:
        raise ValueError("El tipo debe ser 'coste' o 'beneficio'")

    # Construimos DataFrame para comparación
    data = {
        'Participante': [f"Individuo {i+1}" for i in range(len(cantidades))],
        'Cantidad Inicial': cantidades,
        'Reparto Proporcional': [round(val, 2) for val in prop],
        'Reparto Logarítmico': [round(val, 2) for val in loga]
    }
    df = pd.DataFrame(data)

    # Mostrar gráfico comparativo
    mostrar_comparativa(
        cantidades,
        metodo1=reparto_proporcional_costes if tipo == 'coste' else reparto_proporcional_beneficios,
        metodo2=reparto_logaritmico_costes if tipo == 'coste' else reparto_logaritmico_beneficios
    )

    # Mostrar tabla en Streamlit
    st.subheader("📋 Comparativa entre métodos de reparto")
    st.dataframe(df, use_container_width=True)

    return df


def explicar_diferencias():
    explicacion = """
    En el modelo proporcional, cada participante recibe una parte del coste o beneficio en proporción directa a su aporte o consumo.

    En el modelo logarítmico:
    - Para los costes: el que consume menos se beneficia más del ahorro generado por el consumo conjunto.
    - Para los beneficios: el que invierte menos puede recibir un extra mayor en porcentaje gracias al efecto de la subaditividad.

    Este comportamiento está alineado con modelos económicos reales donde existen economías de escala y ventajas por cooperación.
    """
    return explicacion
