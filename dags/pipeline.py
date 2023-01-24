from datetime import timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from jobs.data_ingestion import data_ingestion
from jobs.data_cleaning import data_cleaning
from jobs.data_validation import data_validation
from jobs.data_analysis import data_analysis
from utils.redshift_helpers import redshift_connection

# Default args
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 1, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# DAG definition
dag = DAG(
    'data_pipeline',
    default_args=default_args,
    schedule_interval='0 0 * * *',  # run every day at midnight
)

# Tasks definition
ingest_data = PythonOperator(
    task_id='ingest_data',
    python_callable=data_ingestion,
    dag=dag,
)

clean_data = PythonOperator(
    task_id='clean_data',
    python_callable=data_cleaning,
    dag=dag,
    depends_on_past=True,
)

validate_data = PythonOperator(
    task_id='validate_data',
    python_callable=data_validation,
    dag=dag,
    depends_on_past=True,
)

analyze_data = PythonOperator(
    task_id='analyze_data',
    python_callable=data_analysis,
    dag=dag,
    depends_on_past=True,
)

# Tasks ordering
ingest_data >> clean_data >> validate_data >> analyze_data