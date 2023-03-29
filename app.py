import streamlit as st

st.set_page_config(
    page_title = 'PyUniban',
    layout= 'wide',
    page_icon = "escudo.png"
)

col_a, col_b, = st.columns(2)

with col_a:
    st.title("Curso introductorio a Python")
    st.caption("organizado por el Semillero de Matemáticas orientadas a la Ingeniería del Instituto Unibán (SEMATI)")
    st.image('escudo.png')

with col_b:
    st.title("Clases")
    st.markdown(f"""
    [Clase No. 1: cadenas y números, funciones predeterminadas, operadores y fundamentos de sintaxis.](https://colab.research.google.com/github/frncscp/PyUniban/blob/main/Clase_1.ipynb)
    [Clase No. 2: manipulación de cadenas, formato, acotaciones de operadores, introducción a los métodos.](https://colab.research.google.com/github/frncscp/PyUniban/blob/main/Clase_2.ipynb)
    """)
    st.caption("Para poder usar los jupyter notebooks, primero se debe dar click al botón \"copiar en Drive\"")
