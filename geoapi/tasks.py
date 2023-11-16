from celery import shared_task
from .models import Query, QueryResult
import time
import random

@shared_task
def emul_request(query_id):
    time.sleep(random.randint(1, 60))  # Эмуляция длительной задачи
    result = random.choice([True, False])  # Случайный результат
    QueryResult.objects.create(query_id=query_id, result=result)