from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()

rabbitmq_cluster_username = os.environ["RABBITMQ_CLUSTER_USERNAME"]
rabbitmq_cluster_password = os.environ["RABBITMQ_CLUSTER_PASSWORD"]
rabbitmq_domain = "localhost"
port = 5672

broker_url = f"pyamqp://{rabbitmq_cluster_username}:{rabbitmq_cluster_password}@{rabbitmq_domain}:{port}//"

class Config:
    broker_url = broker_url


app = Celery("tasks")
app.config_from_object(Config)


@app.task
def work() -> None:
    return "done"