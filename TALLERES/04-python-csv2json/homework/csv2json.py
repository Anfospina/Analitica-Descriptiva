
import csv #libreria para leer y escribir
import json
"""Script para convertir un archivo CSV a JSON"""

from nicegui import ui


def convert_csv_2_json(input_file):
    """Converts a CSV file to a JSON file"""

    output_file = input_file.replace(".csv", ".json")
    data = []

    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f) #objeto iterable que genera un diccionario por cada fila del archivo CSV
        for row in reader:
            data.append(row) #lista de diccionarios

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f) #Convierte el objeto data (que es una lista de diccionarios) a formato JSON y lo escribe en el archivo abierto (f)

    ui.notify("The file was transformed successfully!")


def app():
    """Main function to run the app"""

    ui.label("CSV to JSON Converter").classes("text-4xl font-bold")
    ui.label("")

    filename = ui.input(
        label="CSV file to convert:",
        placeholder="filename",
    )

    ui.label("")

    ui.label("")
    ui.button("Convert", on_click=lambda: convert_csv_2_json(filename.value))
    ui.run()


app()