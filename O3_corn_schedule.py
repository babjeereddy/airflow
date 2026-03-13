    # Run Every Day at Midnight
    # schedule = "0 0 * * *"
    # ┌ minute (0)
    # │ ┌ hour (0)
    # │ │ ┌ day of month (*)
    # │ │ │ ┌ month (*)
    # │ │ │ │ ┌ day of week (*)
    # │ │ │ │ │
    # * * * * *
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="daily_dag",
    start_date=datetime(2024,1,1),
    schedule="*/5 * * * *",
    catchup=False
) as dag:

    t1 = BashOperator(
        task_id="print_date",
        bash_command='echo "Current date and time: $(date)"'
    )