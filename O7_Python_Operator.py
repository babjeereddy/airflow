from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG(
    dag_id='python_basic_example',
    start_date=datetime(2024, 1, 1),
    schedule='@daily',
    catchup=False,
    tags=['python', 'example'],
) as dag:

    def print_hello():
        print("Hello from PythonOperator!")

    python_task = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello
    )
    