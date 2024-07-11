'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Objective: This program is designed to retrieve data from PostgreSQL, then convert CSV files into JSON format.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

# Import libraries.
import datetime as dt
import pandas as pd
import psycopg2 as db
import json
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Take data from PostgreSQL.
def queryPostgresql():
    '''
    Retrieve data from the hiblu_faq table in PostgreSQL and save it to a CSV file.

    This function establishes a connection to a PostgreSQL database using psycopg2,
    executes a query to fetch all data from the public.hiblu_faq table,
    and saves it to a CSV file named FAQ_cleaned.csv.
    '''
    conn_string = "dbname='airflow' host='postgres' user='airflow' password='airflow' port='5432'"
    conn = db.connect(conn_string)
    df = pd.read_sql("SELECT * FROM public.hiblu_faq", conn)
    df.to_csv('/opt/airflow/dags/FAQ_cleaned.csv')

# Convert CSV to JSON.
def convertCsvToJson():
    '''
    Convert a CSV file containing FAQ data into JSON format.

    This function reads data from the CSV file FAQ_cleaned.csv, then converts each
    row into a JSON object formatted appropriately for a chatbot (ChatGPT). The result is saved
    to a JSON file named FAQ.json.
    '''
    df = pd.read_csv('/opt/airflow/dags/FAQ_cleaned.csv')

    # Define early message.
    system_message = {"role": "system", "content": "Hi! HiBlu siap menjawab pertanyaanmu!"}

    # Define empty list for JSON.
    json_data = []

    for index, row in df.iterrows():
        # Create array for answer and question.
        messages = [
            system_message,
            {"role": "user", "content": row['Question']},
            {"role": "assistant", "content": row['Answer']}
        ]
        # Append JSON object into list. 
        json_data.append({"messages": messages})

    # Convert JSON object list into string.
    json_output = "\n".join(json.dumps(obj) for obj in json_data)

    # Save output.
    output_path = '/opt/airflow/dags/FAQ.json'
    with open(output_path, 'w') as f:
        f.write(json_output)


default_args = {
    'owner': 'Mavericks',
    'start_date': dt.datetime(2024, 7, 3, 12, 0, 0),
}


with DAG('HIBLU',
         default_args=default_args,
         schedule_interval='0 6 * * *',  # Run daily at 6:00 UTC
         catchup=False,
         concurrency=1,  # Ensure only one instance of the DAG runs at a time
         max_active_runs=1
         ) as dag:

    # Task 1 - Took data from PostgreSQL.
    getData = PythonOperator(
        task_id='QueryPostgreSQL',
        python_callable=queryPostgresql,
    )

    # Task 2 - Convert CSV to JSON.
    convertCsvToJsonTask = PythonOperator(
        task_id='ConvertCsvToJson',
        python_callable=convertCsvToJson,
    )

# Define the workflow sequence.
getData >> convertCsvToJsonTask
