"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_08(): 
     x8=pd.read_csv("files/input/tbl0.tsv",delimiter="\t")
     new_column=x8['c0']+x8['c2']
     x8['suma']=new_column
     return x8
    

