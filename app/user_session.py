# user_session.py — Gestión simple de sesión de usuario en Streamlit
import streamlit as st

def init_session_state():
    """Inicializa valores de sesión si no existen"""
    if 'modo' not in st.session_state:
        st.session_state.modo = None
    if 'cantidades' not in st.session_state:
        st.session_state.cantidades = []

def set_modo(modo):
    st.session_state.modo = modo

def get_modo():
    return st.session_state.get('modo', None)

def set_cantidades(lista):
    st.session_state.cantidades = lista

def get_cantidades():
    return st.session_state.get('cantidades', [])