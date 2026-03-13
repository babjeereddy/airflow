from airflow import DAG
from airflow.operators.email import EmailOperator
from datetime import datetime

with DAG(
    dag_id="email_operator_example",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    send_email = EmailOperator(
        task_id="send_email_task",
        to="babjee@gmail.com",
        subject="Airflow Email Test",
        html_content="<h3>Hello!</h3><p>This email is sent from Airflow DAG.</p>"
    )

    send_email