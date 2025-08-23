"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_12():
     x12=pd.read_csv('files/input/tbl2.tsv',delimiter="\t")
     x12['c5']=x12['c5a'] + ':' + x12['c5b'].astype(str)
     new_df=x12.groupby('c0')['c5'].agg(lambda x: ','.join(map(str, sorted(x))))
     return new_df.reset_index()

