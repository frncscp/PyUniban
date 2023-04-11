import streamlit as st

st.set_page_config(
    page_title = 'PyUniban',
    page_icon = r"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png",
    layout = 'wide'
)


st.title("Curso introductorio a Python")
st.caption("Orientado a matemáticas")

st.divider()

col_a, col_b = st.columns(2)

with col_a:

    st.title("Clases")
    st.markdown(f"""
     [Clase No. 1:](https://colab.research.google.com/github/frncscp/PyUniban/blob/main/Clase_1.ipynb) cadenas y números, funciones predeterminadas, operadores y fundamentos de sintaxis. 

     [Clase No. 2:](https://colab.research.google.com/github/frncscp/PyUniban/blob/main/Clase_2.ipynb) manipulación de cadenas, formato, acotaciones de operadores, introducción a los métodos. 
    """)
    st.caption("Para poder usar los Jupyter Notebooks, primero se debe dar click al botón \"Copiar en Drive\".")

with col_b:
    st.latex(r'\sigma(z) = \frac{1} {1 + e^{-z}}')
    st.code(line_numbers = True,
            body = """
from decimal import Decimal
from math import e as euler

def sigmoid(w, x, b): #pesos, entradas, sesgos
    z = 0
    if not len(w) == len(x) == len(b):
        return 'Error: las listas difieren en tamaño.'
    for weight, entrance, bias in zip(w, x, b):
        z+= weight*entrance-bias
    result = 1/Decimal(1+(euler**-z))
    return result

result = sigmoid([1, 2, -2], [4, 1, 6], [2, 1, 7])
print(result)""")

st.divider()

st.markdown("""
## Recursos en línea:

[StackOverflow](https://stackoverflow.com): encuentra soluciones a errores que puedan aparecer en tu código.

[Python desde cero](https://www.youtube.com/playlist?list=PLyvsggKtwbLW1j0d5yaCkRF9Axpdlhsxz): serie de videos en español que profundizan los fundamentos de Python.
"""
