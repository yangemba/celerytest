import time
from app import celery_app

# celery -A tasks worker --loglevel=info


@celery_app.task
def add(x, y):
    time.sleep(30)
    return x + y
