"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd

def pregunta_01():
    # Carga de datos desde el archivo
    filename = "files/input/clusters_report.txt"
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Excluir encabezados iniciales
    data_lines = lines[4:]

    # Preparar lista para almacenar datos procesados
    processed_data = []
    temp_row = []  # Para almacenar datos temporalmente
    is_first_line = True  # Identificar si es la primera línea de un registro

    for line in data_lines:
        line = line.strip()  # Eliminar espacios en blanco al inicio y fin
        words = line.split()  # Dividir la línea en palabras

        if words and is_first_line:  # Si es la primera línea de un registro
            temp_row = [
                int(words[0]),  # Número de cluster
                int(words[1]),  # Cantidad de palabras clave
                float(words[2].replace(',', '.')),  # Porcentaje de palabras clave
                " ".join(words[4:]),  # Fragmento inicial de palabras clave
            ]
            is_first_line = False
        elif words:  # Si no es la primera línea pero hay contenido
            temp_row[-1] += " " + " ".join(words)  # Concatenar palabras clave
        else:  # Línea vacía indica el final de un registro
            # Finalizar procesamiento de palabras clave
            temp_row[-1] = temp_row[-1].replace('.', '')
            processed_data.append(temp_row)  # Agregar registro completo
            temp_row = []  # Reiniciar registro temporal
            is_first_line = True

    # Crear DataFrame a partir de los datos procesados
    columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']
    return pd.DataFrame(processed_data, columns=columns)

    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.

    """
  
if __name__ == "__main__":
  print(pregunta_01())
