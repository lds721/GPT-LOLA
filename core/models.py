import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Constantes por defecto
default_a_cost = 1440
default_a_invest = 2

# ----------------------
# FUNCIONES BASE
# ----------------------
def gasto_logaritmico(x, a=default_a_cost):
    return a * np.log(x)

def beneficio_logaritmico(c, a=default_a_invest):
    return (np.log(c) - c) * a

# ----------------------
# REPARTO LOGARÍTMICO DE COSTES ENTRE DOS
# ----------------------
def reparto_logaritmico_costes_dos(x1, x2, a=default_a_cost, n=100):
    if x1 <= 0 or x2 <= 0:
        raise ValueError("Los consumos deben ser positivos.")
    if x1 >= x2:
        raise ValueError("x1 debe ser menor que x2.")

    h = (x2 - x1) / n
    y = gasto_logaritmico(2 * x1, a) / 2

    for k in range(n):
        x = k * h
        g1 = gasto_logaritmico(x1, a)
        g2 = gasto_logaritmico(x1 + x, a)
        g3 = gasto_logaritmico(x1 + x + h, a)
        g_sum1 = gasto_logaritmico(2 * x1 + x, a)
        g_sum2 = gasto_logaritmico(2 * x1 + x + h, a)

        A = g1 + g3 - g_sum2
        B = g1 + g2 - g_sum1
        delta = (A - B) / (g1 + g3)
        y -= delta

    y1 = y
    y2 = gasto_logaritmico(x1 + x2, a) - y1
    return y1, y2

# ----------------------
# REPARTO LOGARÍTMICO DE COSTES ENTRE N
# ----------------------
def reparto_logaritmico_costes(xs, a=default_a_cost, n=100):
    xs = sorted(xs)
    asignaciones = [0] * len(xs)
    suma_total = sum(xs)
    G_total = gasto_logaritmico(suma_total, a)

    for i in range(len(xs)):
        otros = xs[:i] + xs[i+1:]
        suma_otros = sum(otros)
        y1, _ = reparto_logaritmico_costes_dos(xs[i], suma_otros, a=a, n=n) if suma_otros > 0 else (G_total / len(xs), 0)
        asignaciones[i] = y1

    normalizador = sum(asignaciones)
    if normalizador > 0:
        asignaciones = [v / normalizador * G_total for v in asignaciones]

    return asignaciones

# ----------------------
# REPARTO LOGARÍTMICO DE BENEFICIOS ENTRE DOS
# ----------------------
def reparto_logaritmico_beneficios_dos(x1, x2, a=default_a_invest, n=100):
    if x1 <= 0 or x2 <= 0:
        raise ValueError("Las aportaciones deben ser positivas.")
    if x1 >= x2:
        raise ValueError("x1 debe ser menor que x2.")

    def F(c):
        return np.log(c) - c

    h = (x2 - x1) / n
    y = (F(2 * x1) ** 2) / 2

    for k in range(n):
        x = k * h
        num1 = (F(2 * x1 + x)) * (1 / (2 * x1 + x) - 1)
        num2 = (F(x1 + x)) * (1 / (x1 + x) - 1)
        den = (F(x1) ** 2 + F(x1 + x) ** 2)
        delta = 2 * ((num1 - num2) / den) * F(x1) ** 2 * h
        y += delta

    y1 = a * y
    y2 = a * (F(x1 + x2) ** 2 - y)
    return y1, y2

# ----------------------
# REPARTO LOGARÍTMICO DE BENEFICIOS ENTRE N
# ----------------------
def reparto_logaritmico_beneficios(xs, a=default_a_invest, n=100):
    xs = sorted(xs)
    asignaciones = [0] * len(xs)
    suma_total = sum(xs)
    F_total = beneficio_logaritmico(suma_total, a)

    for i in range(len(xs)):
        otros = xs[:i] + xs[i+1:]
        suma_otros = sum(otros)
        y1, _ = reparto_logaritmico_beneficios_dos(xs[i], suma_otros, a=a, n=n) if suma_otros > 0 else (F_total / len(xs), 0)
        asignaciones[i] = y1

    normalizador = sum(asignaciones)
    if normalizador != 0:
        asignaciones = [v / normalizador * F_total for v in asignaciones]

    return asignaciones
def reparto_proporcional_costes(xs, a=1440):
    """
    Reparto proporcional del coste total según consumo individual.
    """
    total = sum(xs)
    total_coste = gasto_logaritmico(total, a)
    return [(x / total) * total_coste for x in xs]


def reparto_proporcional_beneficios(xs, a=2):
    """
    Reparto proporcional del beneficio total según aportación individual.
    """
    total = sum(xs)
    total_beneficio = beneficio_logaritmico(total, a)
    return [(x / total) * total_beneficio for x in xs]
