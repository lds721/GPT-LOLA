# 🧮 Chatbot Económico Interactivo

Asistente educativo para el cálculo de **ahorro en costes** y **beneficios conjuntos** usando modelos proporcionales y logarítmicos, basado en economía de escala y teoría logarítmica.

---

## 🚀 Características
- Selección entre **cálculo de ahorro** o **beneficio de inversión**.
- Entrada personalizada de cantidades (consumos o aportaciones).
- Comparativa entre **reparto proporcional** y **logarítmico**.
- Gráficas automáticas con `matplotlib`.
- Explicaciones claras y educativas.
- Modular y fácil de mantener.

---

## 📁 Estructura del Proyecto
```
inversion_chatbot/
├── app/
│   ├── main.py                  # Entrada principal del chatbot
│   ├── chatbot_interface.py     # Lógica conversacional
│   ├── user_session.py          # Estado de sesión del usuario
│   └── ui.py                    # Textos y etiquetas
│
├── core/
│   ├── models.py                # Fórmulas matemáticas (log y prop)
│   ├── calculator.py            # Aplicación de modelos + gráficas
│
├── requirements.txt            # Librerías necesarias
└── README.md                   # Documentación
```

---

## ✅ Requisitos
- Python 3.9+
- Streamlit
- Numpy
- Pandas
- Matplotlib

Instalación:
```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución
Desde la carpeta principal:
```bash
streamlit run app/main.py
```

---

## 🧠 Modelos matemáticos
- **Costes**: \( G(x) = a \cdot \ln(x) \)
- **Beneficio conjunto**: \( F(c) = a \cdot (\ln(c) - c) \)
- **Reparto proporcional**: según el peso relativo de cada participante.
- **Reparto logarítmico**: según modelos subaditivos y concavos.

---

## 📚 Licencia y uso
Este proyecto forma parte de un Trabajo de Fin de Grado en Matemáticas. 
Su propósito es educativo y divulgativo.

---

## ✨ Autor
autor: Lola Durán Sánchez
universidad: Universidad de Almería
contacto: lds721@inlumine.ual.es
#   G P T - L O L A  
 