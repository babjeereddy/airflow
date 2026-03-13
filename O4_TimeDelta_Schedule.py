# Timedelta provides fixed-interval scheduling (not calendar-aware).

# ============================================
# TIMEDELTA SCHEDULE EXAMPLES
# ============================================

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# ──────────────────────────────────────
# Every 30 Seconds (Airflow 2.x)
# ──────────────────────────────────────
with DAG(
        dag_id="timedelta_30_seconds",
        schedule_interval=timedelta(seconds=30),
        start_date=datetime(2024, 1, 1),
        catchup=False,
        max_active_runs=1
) as dag:
    t1 = BashOperator(
        task_id="print_30s",
        bash_command='echo "Running every 30 seconds at $(date) "'
    )

with DAG(
        dag_id="timedelta_1_hr",
        schedule_interval=timedelta(hours=1),
        start_date=datetime(2026,3,12),
        catchup=True        
) as dag:
    t1 = BashOperator(
        task_id="print_1hr",
        bash_command='echo "Running every 1 hour at $(date) "'
    )
    

# # ──────────────────────────────────────
# # Every 5 Minutes
# # ──────────────────────────────────────
# dag_5min = DAG(
#     dag_id="timedelta_5_minutes",
#     schedule_interval=timedelta(minutes=5),
#     start_date=datetime(2024, 1, 1),
#     catchup=False
# )

# # ──────────────────────────────────────
# # Every 45 Minutes
# # ──────────────────────────────────────
# dag_45min = DAG(
#     dag_id="timedelta_45_minutes",
#     schedule_interval=timedelta(minutes=45),
#     start_date=datetime(2024, 1, 1),
#     catchup=False
# )

# # ──────────────────────────────────────
# # Every 90 Minutes (1.5 Hours)
# # ──────────────────────────────────────
# dag_90min = DAG(
#     dag_id="timedelta_90_minutes",
#     schedule_interval=timedelta(minutes=90),
#     start_date=datetime(2024, 1, 1),
#     catchup=False
# )

# # ──────────────────────────────────────
# # Every 2 Hours
# # ──────────────────────────────────────
# dag_2h = DAG(
#     dag_id="timedelta_2_hours",
#     schedule_interval=timedelta(hours=2),
#     start_date=datetime(2024, 1, 1),
#     catchup=False
# )

# # ──────────────────────────────────────
# # Every 6 Hours
# # ──────────────────────────────────────
# dag_6h = DAG(
#     dag_id="timedelta_6_hours",
#     schedule_interval=timedelta(hours=6),
#     start_date=datetime(2024, 1, 1),
#     catchup=False
# )

# # ──────────────────────────────────────
# # Every 18 Hours
# # ──────────────────────────────────────
# dag_18h = DAG(
#     dag_id="timedelta_18_hours",
#     schedule_interval=timedelta(hours=18),
#     start_date=datetime(2024, 1, 1),
#     catchup=False
# )

# # ──────────────────────────────────────
# # Every 2 Days
# # ──────────────────────────────────────
# dag_2days = DAG(
#     dag_id="timedelta_2_days",
#     schedule_interval=timedelta(days=2),
#     start_date=datetime(2024, 1, 1),
#     catchup=False
# )

# # ──────────────────────────────────────
# # Every 3.5 Days
# # ──────────────────────────────────────
# dag_3_5days = DAG(
#     dag_id="timedelta_3_5_days",
#     schedule_interval=timedelta(days=3, hours=12),
#     start_date=datetime(2024, 1, 1),
#     catchup=False
# )

# # ──────────────────────────────────────
# # Every 1 Week
# # ──────────────────────────────────────
# dag_1week = DAG(
#     dag_id="timedelta_1_week",
#     schedule_interval=timedelta(weeks=1),
#     start_date=datetime(2024, 1, 1),
#     catchup=False
# )

# # ──────────────────────────────────────
# # Every 2 Weeks (Bi-weekly)
# # ──────────────────────────────────────
# dag_2weeks = DAG(
#     dag_id="timedelta_2_weeks",
#     schedule_interval=timedelta(weeks=2),
#     start_date=datetime(2024, 1, 1),
#     catchup=False
# )

# # ──────────────────────────────────────
# # Complex: 1 day, 6 hours, 30 minutes
# # ──────────────────────────────────────
# dag_complex = DAG(
#     dag_id="timedelta_complex",
#     schedule_interval=timedelta(days=1, hours=6, minutes=30),
#     start_date=datetime(2024, 1, 1),
#     catchup=False
# )