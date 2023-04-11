import streamlit as st

st.set_page_config(
    page_title = 'PyUniban',
    page_icon = r"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png",
    layout = 'centered'
)


st.title("Curso introductorio a Python")
st.caption("Orientado a matemáticas")

st.title("Clases")
st.markdown(f"""
 [Clase No. 1:](https://colab.research.google.com/github/frncscp/PyUniban/blob/main/Clase_1.ipynb) cadenas y números, funciones predeterminadas, operadores y fundamentos de sintaxis. 

 [Clase No. 2:](https://colab.research.google.com/github/frncscp/PyUniban/blob/main/Clase_2.ipynb) manipulación de cadenas, formato, acotaciones de operadores, introducción a los métodos. 
""")
st.caption("Para poder usar los jupyter notebooks, primero se debe dar click al botón \"Copiar en Drive\".")
