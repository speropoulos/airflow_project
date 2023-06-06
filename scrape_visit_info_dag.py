from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from visit_info_etl import run_visit_info_etl
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 5, 28),
    'schedule_interval': '0 0 * * *',
    'email': ['speropoulos@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}
dag = DAG('batch_processing_dag', start_date=datetime(2023, 5, 28), schedule_interval='0 0 * * *') 


dag = DAG(
    'visit_info_dag',
    default_args=default_args,
    description='Scrape visit info from work crm',
)

run_etl = PythonOperator(
    task_id='complete_visit_info',
    python_callable=run_visit_info_etl,
    dag=dag,
)

run_etl


