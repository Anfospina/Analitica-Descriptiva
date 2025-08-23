"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_11():
     x11 = pd.read_csv("files/input/tbl1.tsv",delimiter="\t")
     x11=x11.groupby('c0')['c4'].agg(lambda x: ','.join(map(str, sorted(x))))
     new_df = x11.reset_index() #creacion de un nuevo dataframe
     return new_df