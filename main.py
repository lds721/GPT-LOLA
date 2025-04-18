import streamlit as st
from app.chatbot_interface import start_chatbot
from app.user_session import init_session_state, set_modo


def main():
    init_session_state()
    st.set_page_config(page_title="Asistente de Reparto Económico", layout="centered")
    st.title("🤖 Chatbot Económico Interactivo")

    st.markdown("""
    Bienvenido al asistente financiero especializado en repartos de costes y beneficios.

    Este Chatbot te permitirá:
    - Calcular **ahorro en costes** si compartes consumos con otras entidades.
    - Calcular **beneficios conjuntos** cuando inviertes junto con otros inversores.
    - Ver explicaciones detalladas y gráficas comparativas.
    """)

    tipo_calculo = st.radio("¿Qué deseas calcular?", (
        "Ahorro en costes (consumo compartido)",
        "Beneficio en inversión conjunta"
    ))

    if tipo_calculo:
        modo = "coste" if "costes" in tipo_calculo else "beneficio"
        set_modo(modo)
        start_chatbot(modo)

if __name__ == "__main__":
    main()