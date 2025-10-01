import streamlit as st
import random
import json

# Configuración inicial
st.set_page_config(page_title="Quiz Villanas Disney", page_icon="👑")

# Cargar preguntas desde archivo JSON
with open("questions.json", "r", encoding="utf-8") as f:
    preguntas = json.load(f)

# Seleccionar 5 preguntas aleatorias (una sola vez)
if "preguntas_seleccionadas" not in st.session_state:
    st.session_state.preguntas_seleccionadas = random.sample(preguntas, 5)
    st.session_state.respuestas_usuario = {}
    st.session_state.quiz_terminado = False
    st.session_state.correctas = 0

st.title("👑 Quiz de Villanas de Disney")
st.markdown("Responde correctamente las 5 preguntas para ganar una *lluvia de pizzas* 🍕")

# Mostrar preguntas si aún no termina
if not st.session_state.quiz_terminado:
    for idx, pregunta in enumerate(st.session_state.preguntas_seleccionadas):
        st.subheader(f"Pregunta {idx + 1}")
        respuesta = st.radio(
            pregunta["pregunta"],
            pregunta["opciones"],
            key=f"pregunta_{idx}"
        )
        st.session_state.respuestas_usuario[idx] = respuesta

    if st.button("Enviar respuestas"):
        correctas = 0
        for idx, pregunta in enumerate(st.session_state.preguntas_seleccionadas):
            if st.session_state.respuestas_usuario.get(idx) == pregunta["respuesta"]:
                correctas += 1
        st.session_state.correctas = correctas
        st.session_state.quiz_terminado = True
        st.rerun()

else:
    if st.session_state.correctas == 5:
        st.success("🎉 ¡Felicidades! Respondiste correctamente las 5 preguntas.")
        st.image("images/pizza.gif", caption="¡Lluvia de pizzas!", use_column_width=True)
        st.balloons()
    else:
        st.error(f"Obtuviste {st.session_state.correctas}/5 respuestas correctas.")
        if st.button("🔁 Intentar de nuevo"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
