import numpy as np
import matplotlib.pyplot as plt
import streamlit as st  # ✅ Importación necesaria para mostrar gráficos en la app

def mostrar_comparativa(xs, metodo1, metodo2, labels=('Proporcional', 'Logarítmico')):
    """
    Genera un gráfico de barras comparativo entre dos métodos de reparto.

    Args:
        xs (list of float): valores de entrada (consumos o aportaciones)
        metodo1 (callable): función del primer método (ej. proporcional)
        metodo2 (callable): función del segundo método (ej. logarítmico)
        labels (tuple): etiquetas de los métodos
    """
    r1 = metodo1(xs)
    r2 = metodo2(xs)
    labels_indices = [f"Individuo {i+1}" for i in range(len(xs))]

    x = np.arange(len(xs))
    width = 0.35

    fig, ax = plt.subplots()
    ax.bar(x - width/2, r1, width, label=labels[0])
    ax.bar(x + width/2, r2, width, label=labels[1])

    ax.set_ylabel('Asignación')
    ax.set_title('Comparativa entre métodos de reparto')
    ax.set_xticks(x)
    ax.set_xticklabels(labels_indices)
    ax.legend()

    plt.tight_layout()
    st.pyplot(fig)  # ✅ Mostrar el gráfico en Streamlit
