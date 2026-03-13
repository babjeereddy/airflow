from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def task1():
    print("Extract data")

def task2():
    print("Transform data")

def task3():
    print("Load data")

with DAG(
    dag_id="dependency_example",
    start_date=datetime(2024,1,1),
    schedule_interval=None,
    catchup=False
) as dag:

    extract = PythonOperator(
        task_id="extract",
        python_callable=task1
    )

    transform = PythonOperator(
        task_id="transform",
        python_callable=task2
    )

    load = PythonOperator(
        task_id="load",
        python_callable=task3
    )

    extract >> transform >> load