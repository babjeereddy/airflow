from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from datetime import datetime

with DAG(
    dag_id="snowflake_query_example",
    start_date=datetime(2024,1,1),
    schedule_interval=None,
    catchup=False
) as dag:

    run_query = SnowflakeOperator(
        task_id="run_snowflake_query",
        snowflake_conn_id="snowflake",
        sql="create database my_database;"
    )