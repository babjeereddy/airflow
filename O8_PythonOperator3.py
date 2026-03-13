from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def greet(first_name, last_name, greeting="Hello"):
    message = f"{greeting}, {first_name} {last_name}!"
    print(message)
    return message

with DAG(
    dag_id='python_args_example',
    start_date=datetime(2024, 1, 1),
    schedule='@daily',
    catchup=False,
) as dag:

    # Using op_args (positional arguments - as LIST)
    task_greet = PythonOperator(
        task_id='greet_user',
        python_callable=greet,
        op_args=['John', 'Doe',"Welcome"],  # ← Positional: first_name='John', last_name='Doe'
    )