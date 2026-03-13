from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def get_current_time():
    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current time: {now}")
    return now  # ← Automatically pushed to XCom as 'return_value'

with DAG('python_return_example', start_date=datetime(2024,1,1),
         schedule='@daily', catchup=False) as dag:

    task_time = PythonOperator(
        task_id='get_time',
        python_callable=get_current_time,
    )