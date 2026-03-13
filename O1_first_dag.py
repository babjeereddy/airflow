from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    'bash_operator_basic',
    start_date=datetime(2026, 3, 9),
    schedule_interval='@daily',
    catchup=False
) as dag:

    t1 = BashOperator(
        task_id='print_hello',
        bash_command='echo "Hello from BashOperator!"'
    )

    t2 = BashOperator(
        task_id='print_world',
        bash_command='echo "World from BashOperator!"'
    )
    t2 >> t1
    