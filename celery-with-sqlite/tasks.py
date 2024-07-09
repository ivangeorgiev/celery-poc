from celery import Celery

BROKER_URL = 'sqla+sqlite:////broker-db/celery.sqlite'
BACKEND_URL = 'db+sqlite:////backend-db/celery.sqlite'
celeryapp = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL, )


@celeryapp.task(name='Add two numbers')
def add(x, y):
    return x + y
