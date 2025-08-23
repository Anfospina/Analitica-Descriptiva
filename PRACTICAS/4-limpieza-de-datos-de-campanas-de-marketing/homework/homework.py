"""
Escriba el codigo que ejecute la accion solicitada.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import zipfile
import os

def clean_campaign_data():
    input_dir='files/input/'
    output_dir='files/output/'
    os.makedirs(output_dir, exist_ok=True)
    
    data=[]
    
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.csv.zip'):
            with zipfile.ZipFile(input_dir+file_name, 'r') as z:
                for csv_file in z.namelist():
                    with z.open(csv_file) as f:
                        df=pd.read_csv(f)
                        if 'client_id' in df.columns:
                            data.append(df)


    data_frame=pd.concat(data)

    
    #Client.csv
    data_frame['job']=data_frame['job'].str.replace('.','').str.replace('-','_')
    data_frame['education']=data_frame['education'].str.replace('.','_').replace('unknown','pd.NA')
    data_frame['credit_default']=data_frame['credit_default'].apply(lambda x: 1 if x=='yes' else 0)
    data_frame['mortgage']=data_frame['mortgage'].apply(lambda x: 1 if x=='yes' else 0)
    data_frame[['client_id','age','job','marital','education','credit_default','mortgage']].to_csv(output_dir+'client.csv', index=False)
    
    #Campaign.csv
    data_frame['previous_outcome']=data_frame['previous_outcome'].apply(lambda x: 1 if x=='success' else 0)
    data_frame['campaign_outcome']=data_frame['campaign_outcome'].apply(lambda x: 1 if x=='yes' else 0)
    data_frame['last_contact_date'] = data_frame.apply(lambda row: pd.to_datetime(f"2022-{row['month']}-{row['day']}"), axis=1)
    data_frame[['client_id','number_contacts','contact_duration','previous_campaign_contacts','previous_outcome','campaign_outcome','last_contact_date']].to_csv(output_dir+'campaign.csv', index=False)              
    
    
    #economics.csv
    data_frame[['client_id','cons_price_idx','euribor_three_months']].to_csv(output_dir+'economics.csv', index=False)
    
    """
    En esta tarea se le pide que limpie los datos de una campaña de
    marketing realizada por un banco, la cual tiene como fin la
    recolección de datos de clientes para ofrecerls un préstamo.

    La información recolectada se encuentra en la carpeta
    files/input/ en varios archivos csv.zip comprimidos para ahorrar
    espacio en disco.

    Usted debe procesar directamente los archivos comprimidos (sin
    descomprimirlos). Se desea partir la data en tres archivos csv
    (sin comprimir): client.csv, campaign.csv y economics.csv.
    Cada archivo debe tener las columnas indicadas.

    Los tres archivos generados se almacenarán en la carpeta files/output/.

    client.csv:
    - client_id
    - age
    - job: se debe cambiar el "." por "" y el "-" por "_"
    - marital
    - education: se debe cambiar "." por "_" y "unknown" por pd.NA
    - credit_default: convertir a "yes" a 1 y cualquier otro valor a 0
    - mortgage: convertir a "yes" a 1 y cualquier otro valor a 0

    campaign.csv:
    - client_id
    - number_contacts
    - contact_duration
    - previous_campaign_contacts
    - previous_outcome: cmabiar "success" por 1, y cualquier otro valor a 0
    - campaign_outcome: cambiar "yes" por 1 y cualquier otro valor a 0
    - last_contact_date: crear un valor con el formato "YYYY-MM-DD",
        combinando los campos "day" y "month" con el año 2022.

    economics.csv:
    - client_id
    - cons_price_idx
    - euribor_three_months



    """

if __name__ == "__main__":
    clean_campaign_data()
