from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='linux_commands_bash_operator_example',
    start_date=datetime(2024, 1, 1),
    schedule='@daily',
    catchup=False,
    tags=['bash', 'example'],
) as dag:

    linux_commands_task = BashOperator(
        task_id='linux_commands_task',
        bash_command="""
            echo "Current Date and Time:"
            date
            echo "Current Working Directory:"
            pwd
            echo "List of Files in Current Directory:"
            ls -l
            echo "Disk Usage:"
            df -h
            echo "Memory Usage:"
            free -h
            """
        )   
