import random
import time

import redis
from flask import Flask

from tasks import add

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    x = random.randint(1, 500)
    y = random.randint(1, 500)
    result = add.delay(x, y)
    return f'Task add({x}, {y}) submitted. ID is: {result.id}'
    return f'request #{count}: Submitted add({x}, {y}). ID is: {result.id}'
