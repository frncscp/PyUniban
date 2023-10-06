import streamlit as st

st.set_page_config(
    page_title = 'Hello, world!',
    page_icon = r"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png",
    layout = 'wide'
)


st.title("Curso introductorio a Python")
st.caption("Orientado a matemáticas")

st.divider()

col_a, col_b = st.columns(2)

with col_a:

    st.title("Clases")
    st.caption("Para poder usar los Jupyter Notebooks, primero se debe dar click al botón \"Copiar en Drive\".")
    st.markdown(f"""
     [Clase No. 1:](https://colab.research.google.com/github/frncscp/PyUniban/blob/main/Clase_1.ipynb) cadenas y números, funciones predeterminadas, operadores aritméticos y fundamentos de sintaxis. 

     [Clase No. 2:](https://colab.research.google.com/github/frncscp/PyUniban/blob/main/Clase_2.ipynb) manipulación de cadenas, f-strings e introducción a los métodos. 
     
     [Clase No. 3:](https://colab.research.google.com/github/frncscp/PyUniban/blob/main/Clase_3.ipynb) estructuras de control de flujo, listas y operadores lógicos.

     [Clase No. 4:](https://colab.research.google.com/github/frncscp/PyUniban/blob/main/Clase_4.ipynb) listas por comprensión, creación de funciones, diccionarios y tuplas.
     
     """)
    

with col_b:
    st.latex(r'\sigma(z) = \frac{1} {1 + e^{-z}}')
    st.code(line_numbers = True,
            body = """
from decimal import Decimal
from math import e 

def sigmoid(w, x, b): #pesos, entradas, sesgos
    assert len(w) == len(x) == len(b), 'Unequal input sizes.'
    z = 0
    for weight, entrance, bias in zip(w, x, b):
        z+= weight*entrance-bias
    result = 1/Decimal(1+(e**-z))
    return result

result = sigmoid([1, 2, -2], [4, 1, 2], [2, 1, 7])
print(result)
""")
    
st.divider()

st.markdown("""
## Recursos en línea:

[StackOverflow](https://stackoverflow.com): encuentra soluciones a errores que puedan aparecer en tu código.

[Python desde cero](https://www.youtube.com/playlist?list=PLyvsggKtwbLW1j0d5yaCkRF9Axpdlhsxz): serie de videos en español que profundizan los fundamentos de Python.

[Microsoft Learn - Primeros pasos con Python](https://learn.microsoft.com/es-es/training/paths/beginner-python/): curso gratis de Microsoft para aprender Python.
""")
