import csv
import json
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def csv_to_json(input_path: str, output_path: str):
    """Reusable CSV to JSON logic"""
    with open(input_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)

    with open(output_path, "w") as json_file:
        json.dump(data, json_file, indent=2)


def create_csv_to_json_dag(
    dag_id: str,
    input_path: str,
    output_path: str,
    start_date: datetime,
    schedule_interval=None,
):
    """DAG factory"""

    with DAG(
        dag_id=dag_id,
        start_date=start_date,
        schedule_interval=schedule_interval,
        catchup=False,
        tags=["csv", "json"],
    ) as dag:

        PythonOperator(
            task_id="convert_csv_to_json",
            python_callable=csv_to_json,
            op_kwargs={
                "input_path": input_path,
                "output_path": output_path,
            },
        )

    return dag
