import random

from celery.result import AsyncResult
from flask import Flask

from tasks import add, celeryapp

app = Flask(__name__)

@app.route('/')
def hello():
    x = random.randint(1, 500)
    y = random.randint(1, 500)
    result = add.delay(x, y)
    return f'Task add({x}, {y}) submitted. ID is: {result.id}. Check the <a href="result/{result.id}">result</a>.'

@app.route('/result/<task_id>')
def route_result(task_id):
    result = AsyncResult(task_id, app=celeryapp)
    if result.ready():
        return str(result.result)
    else:
        return "Task is still processing."
