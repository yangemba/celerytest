from celery import Celery

celery_app = Celery('tasks', backend='redis://localhost', broker='amqp://localhost')

