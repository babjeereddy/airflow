from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='multi_command_bash_operator_example',
    start_date=datetime(2024, 1, 1),
    schedule='@daily',
    catchup=False,
    tags=['bash', 'example'],
) as dag:

    multi_command_task = BashOperator(
        task_id='multi_command_task',
        bash_command="""
        echo "This is the first command."
        echo "This is the second command."
        echo "This is the third command."
        """
    )

    multi_command_task1 = BashOperator(
        task_id='multi_command_task1',
        bash_command="""
        echo "This is the first command."
        echo "This is the second command."
        echo "This is the third command."
        """
    )

    multi_command_task2 = BashOperator(
        task_id='multi_command_task2',
        bash_command="""
        echo "This is the first command."
        echo "This is the second command."
        echo "This is the third command."
        """
    )
multi_command_task1 >> multi_command_task  
multi_command_task2 >> multi_command_task   