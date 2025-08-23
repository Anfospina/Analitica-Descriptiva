"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_02():
    x2 = pd.read_csv("files/input/tbl0.tsv",delimiter="\t")
    x2_c=len(x2.columns)
    return x2_c
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """