# ============================================
# PRESET SCHEDULES - All Examples
# ============================================

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# ──────────────────────────────────────
# 1. @once - Run Only Once
# ──────────────────────────────────────
dag_once = DAG(
    dag_id="schedule_once",
    schedule_interval="@once",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["schedule-demo"]
)

task_once = BashOperator(
    task_id="run_once",
    bash_command='echo "This runs only one time!"',
    dag=dag_once
)

# ──────────────────────────────────────
# 2. @hourly - Every Hour
# ──────────────────────────────────────
dag_hourly = DAG(
    dag_id="schedule_hourly",
    schedule_interval="@hourly",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["schedule-demo"]
)

task_hourly = BashOperator(
    task_id="hourly_task",
    bash_command='echo "Running hourly at $(date)"',
    dag=dag_hourly
)

# # ──────────────────────────────────────
# # 3. @daily - Every Day at Midnight
# # ──────────────────────────────────────
# dag_daily = DAG(
#     dag_id="schedule_daily",
#     schedule_interval="@daily",
#     start_date=datetime(2024, 1, 1),
#     catchup=False,
#     tags=["schedule-demo"]
# )



# task_daily = BashOperator(
#     task_id="daily_etl",
#     bash_command='echo "Weekly report for week ending $(date)"',
#     dag=dag_daily
# )

# # ──────────────────────────────────────
# # 4. @weekly - Every Sunday at Midnight
# # ──────────────────────────────────────
# dag_weekly = DAG(
#     dag_id="schedule_weekly",
#     schedule_interval="@weekly",
#     start_date=datetime(2024, 1, 1),
#     catchup=False,
#     tags=["schedule-demo"]
# )

# task_weekly = BashOperator(
#     task_id="weekly_report",
#     bash_command='echo "Weekly report for week ending $(date)"',
#     dag=dag_weekly
# )

# # ──────────────────────────────────────
# # 5. @monthly - 1st of Every Month
# # ──────────────────────────────────────
# dag_monthly = DAG(
#     dag_id="schedule_monthly",
#     schedule_interval="@monthly",
#     start_date=datetime(2024, 1, 1),
#     catchup=False,
#     tags=["schedule-demo"]
# )

# task_monthly = BashOperator(
#     task_id="monthly_billing",
#     bash_command='echo "Monthly billing run"',
#     dag=dag_monthly
# )

# # ──────────────────────────────────────
# # 6. @quarterly - Every 3 Months
# # ──────────────────────────────────────
# dag_quarterly = DAG(
#     dag_id="schedule_quarterly",
#     schedule_interval="@quarterly",
#     start_date=datetime(2024, 1, 1),
#     catchup=False,
#     tags=["schedule-demo"]
# )

# task_quarterly = BashOperator(
#     task_id="quarterly_review",
#     bash_command='echo "Quarterly business review"',
#     dag=dag_quarterly
# )

# # ──────────────────────────────────────
# # 7. @yearly - January 1st
# # ──────────────────────────────────────
# dag_yearly = DAG(
#     dag_id="schedule_yearly",
#     schedule_interval="@yearly",
#     start_date=datetime(2024, 1, 1),
#     catchup=False,
#     tags=["schedule-demo"]
# )

# task_yearly = BashOperator(
#     task_id="yearly_audit",
#     bash_command='echo "Annual data audit"',
#     dag=dag_yearly
# )

# # ──────────────────────────────────────
# # 8. None - Manual Trigger Only
# # ──────────────────────────────────────
# dag_manual = DAG(
#     dag_id="schedule_manual",
#     schedule_interval=None,
#     start_date=datetime(2024, 1, 1),
#     catchup=False,
#     tags=["schedule-demo"]
# )

# task_manual = BashOperator(
#     task_id="manual_task",
#     bash_command='echo "Manually triggered!"',
#     dag=dag_manual
# )

# # ──────────────────────────────────────
# # 9. @continuous - Runs Continuously
# # ──────────────────────────────────────
dag_continuous = DAG(
    dag_id="schedule_continuous",
    schedule="@continuous",      
    start_date=datetime(2024, 1, 1),
    catchup=False,
    max_active_runs=1,           
    tags=["schedule-demo"]
)

task_continuous = BashOperator(
    task_id="continuous_monitoring",
    bash_command='echo "Continuous monitoring check at $(date)"',
    dag=dag_continuous
)