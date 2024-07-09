from celery import Celery

BROKER_URL = 'redis://redis:6379/0'
BACKEND_URL = 'redis://redis:6379/1'
# BROKER_URL = 'sqla+sqlite:///celery.sqlite'
# BACKEND_URL = 'db+sqlite:///celery.sqlite'
app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL, )


@app.task(name='Add two numbers')
def add(x, y):
    return x + y
