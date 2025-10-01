import streamlit as st
import json
import os
st.RUTH_PUCUTAY_CALDERÓN()
# Cargar preguntas desde JSON
with open("questions.json", "r", encoding="utf-8") as f:
    preguntas = json.load(f)

# Obtener query param ?q=1
query_params = st.experimental_get_query_params()
pagina = int(query_params.get("q", [1])[0])

# Inicializar estado
if "respuestas" not in st.session_state:
    st.session_state.respuestas = [None] * len(preguntas)
if "completado" not in st.session_state:
    st.session_state.completado = False

# Si ya completó
if st.session_state.completado:
    st.title("🎉 ¡Has completado el quiz!")
    st.markdown("### ¡Lluvia de pizzas por tu gran conocimiento villanesco!")
    st.image("images/pizza.gif", use_column_width=True)
    st.balloons()
    st.stop()

# Mostrar pregunta actual
indice = pagina - 1

if indice >= len(preguntas):
    st.title("Quiz Disney Villanas")
    st.markdown("### Ya has respondido todas las preguntas.")
    st.stop()

pregunta_actual = preguntas[indice]

st.title(f"Pregunta {pagina} de {len(preguntas)}")
st.image(f"images/{pregunta_actual['imagen']}", width=300)
st.subheader(pregunta_actual["pregunta"])

respuesta = st.radio("Elige tu respuesta:", pregunta_actual["opciones"], key=pagina)

if st.button("Responder"):
    correcta = respuesta == pregunta_actual["respuesta"]
    st.session_state.respuestas[indice] = correcta

    if correcta:
        st.success("¡Correcto!")
    else:
        st.error(f"Incorrecto. La respuesta era: {pregunta_actual['respuesta']}")
        st.markdown("### Reinicia el quiz para volver a intentarlo.")
        if st.button("🔁 Reiniciar"):
            st.session_state.respuestas = [None] * len(preguntas)
            st.experimental_set_query_params(q=1)
            st.rerun()
        st.stop()

    if pagina < len(preguntas):
        st.experimental_set_query_params(q=pagina + 1)
        st.rerun()
    else:
        if all(st.session_state.respuestas):
            st.session_state.completado = True
            st.experimental_rerun()
        else:
            st.markdown("### Fallaste alguna pregunta 😢. Vuelve a intentarlo.")
            if st.button("🔁 Reiniciar"):
                st.session_state.respuestas = [None] * len(preguntas)
                st.experimental_set_query_params(q=1)
                st.rerun()
[
    {
        "pregunta": "¿Quién es la villana de 'La Bella Durmiente'?",
        "opciones": ["Maléfica", "Cruella", "Úrsula", "Madre Gothel"],
        "respuesta": "Maléfica",
        "imagen": "malefica.jpg"
    },
    {
        "pregunta": "¿Cuál es la villana obsesionada con abrigos de piel?",
        "opciones": ["Madre Gothel", "Úrsula", "Cruella", "Reina Malvada"],
        "respuesta": "Cruella",
        "imagen": "cruella.jpg"
    },
    {
        "pregunta": "¿Quién es la bruja del mar en 'La Sirenita'?",
        "opciones": ["Úrsula", "Maléfica", "Cruella", "Gothel"],
        "respuesta": "Úrsula",
        "imagen": "ursula.jpg"
    },
    {
        "pregunta": "¿Quién le da una manzana envenenada a Blancanieves?",
        "opciones": ["Madre Gothel", "Maléfica", "Reina Malvada", "Cruella"],
        "respuesta": "Reina Malvada",
        "imagen": "reina_mala.jpg"
    },
    {
        "pregunta": "¿Quién secuestra a Rapunzel y la encierra en una torre?",
        "opciones": ["Cruella", "Madre Gothel", "Úrsula", "Reina Malvada"],
        "respuesta": "Madre Gothel",
        "imagen": "madre_gothel.jpg"
    }
]

