"""Taller evaluable"""

# pylint: disable=broad-exception-raised
# pylint: disable=import-error

from .mapreduce import run_mapreduce_job # type: ignore

#
# Columns:
# total_bill, tip, sex, smoker, day, time, size
#

#
# SELECT *, tip/total_bill as tip_rate
# FROM tips;
#
def mapper_query_1(sequence):
    """Mapper"""
    result = []
    for index, (_, row) in enumerate(sequence): #sequence es una tupla (nombreArchivo, valoreslineas). No interesa el nombre del archivo
        if index == 0:
            result.append((index, row.strip() + ",tip_rate")) #agregar una nueva variable en la cabecera y conservar indice
        else:
            row_values = row.strip().split(",") #borrar espacios en los extremos y y separa la línea en una lista usando la coma como delimitador
            total_bill = float(row_values[0])
            tip = float(row_values[1])
            tip_rate = tip / total_bill
            result.append((index, row.strip() + "," + str(tip_rate)))# conserva indice, borra espacios y agrega nuevo valor
    return result


def reducer_query_1(sequence):
    """Reducer"""
    return sequence

#
# SELECT *
# FROM tips
# WHERE time = 'Dinner';
#
def mapper_query_2(sequence):
    """Mapper"""
    result = []
    for index, (_, row) in enumerate(sequence):
        if index == 0:
            result.append((index, row.strip()))
        else:
            row_values = row.strip().split(",")
            if row_values[5] == "Dinner":
                result.append((index, row.strip()))# si se cumple la condición para ese campo emito, es decir, genero la tupla
    return result


def reducer_query_2(sequence):
    """Reducer"""
    return sequence


#
# SELECT *
# FROM tips
# WHERE time = 'Dinner' AND tip > 5.00;
#
def mapper_query_3(sequence):
    """Mapper"""
    result = []
    for index, (_, row) in enumerate(sequence):
        if index == 0:
            result.append((index, row.strip()))
        else:
            row_values = row.strip().split(",")
            if row_values[5] == "Dinner" and float(row_values[1]) > 5.00:
                result.append((index, row.strip()))
    return result


def reducer_query_3(sequence):
    """Reducer"""
    return sequence


#
# SELECT *
# FROM tips
# WHERE size >= 5 OR total_bill > 45;
#
def mapper_query_4(sequence):
    """Mapper"""
    result = []
    for index, (_, row) in enumerate(sequence):
        if index == 0:
            result.append((index, row.strip()))
        else:
            row_values = row.strip().split(",")
            if int(row_values[6]) >= 5 or float(row_values[0]) > 45:
                result.append((index, row.strip()))
    return result


def reducer_query_4(sequence):
    """Reducer"""
    return sequence



#
# SELECT sex, count(*)
# FROM tips
# GROUP BY sex;
#
def mapper_query_5(sequence):
    """Mapper"""
    result = []
    for index, (_, row) in enumerate(sequence):
        if index == 0:
            continue
        row_values = row.strip().split(",")
        result.append((row_values[2], 1)) #lista de tuplas con (sexo, 1)
    return result


def reducer_query_5(sequence): 
    """Reducer""" # aquí ya viene la sequence ordenada, es decir, primero female y despues male con tuplas (female,1).....(male,1)
    counter = dict()
    for key, value in sequence:
        if key not in counter:
            counter[key] = 0
        counter[key] += value
    return list(counter.items())


#
# ORQUESTADOR:
#
def run():
    """Orquestador"""

    run_mapreduce_job(
        mapper=mapper_query_1,
        reducer=reducer_query_1,
        input_directory="files/input",
        output_directory="files/query_1",
    )

    run_mapreduce_job(
        mapper=mapper_query_2,
        reducer=reducer_query_2,
        input_directory="files/input",
        output_directory="files/query_2",
    )

    run_mapreduce_job(
        mapper=mapper_query_3,
        reducer=reducer_query_3,
        input_directory="files/input",
        output_directory="files/query_3",
    )

    run_mapreduce_job(
        mapper=mapper_query_4,
        reducer=reducer_query_4,
        input_directory="files/input",
        output_directory="files/query_4",
    )

    run_mapreduce_job(
        mapper=mapper_query_5,
        reducer=reducer_query_5,
        input_directory="files/input",
        output_directory="files/query_5",
    )

if __name__ == "__main__":

    run()