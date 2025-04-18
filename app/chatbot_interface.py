import streamlit as st
from core.calculator import calcular_reparto, explicar_diferencias
from app.ui import (
    INTRO_MENSAJE,
    EJEMPLO_ENTRADA,
    ERROR_CANTIDADES,
    ERROR_ENTRADA,
    LEYENDA_COSTE,
    LEYENDA_BENEFICIO,
    TITULO_TABLA,
    TITULO_EXPLICACION,
    LABEL_INPUT
)
from app.user_session import set_cantidades


def start_chatbot(modo):
    """
    Interfaz principal del asistente según el modo ('coste' o 'beneficio').
    """
    st.header(f"📊 Asistente de Cálculo - {'Ahorro en Costes' if modo == 'coste' else 'Beneficio en Inversión'}")

    st.markdown(INTRO_MENSAJE)
    st.markdown(EJEMPLO_ENTRADA)

    entrada = st.text_input(LABEL_INPUT, value="10, 20, 30")

    if entrada:
        try:
            cantidades = [float(x.strip()) for x in entrada.split(",") if x.strip() != ""]
            if any(c <= 0 for c in cantidades):
                st.error(ERROR_CANTIDADES)
                return

            set_cantidades(cantidades)

            st.success("✅ Datos cargados correctamente. Procesando...")

            # Mostrar cálculo + gráfico + tabla
            df = calcular_reparto(modo, cantidades)

            # Mostrar explicación del modelo
            st.subheader(TITULO_EXPLICACION)
            st.markdown(explicar_diferencias())

            st.info(LEYENDA_COSTE if modo == "coste" else LEYENDA_BENEFICIO)

        except ValueError:
            st.error(ERROR_ENTRADA)
