import random
from celery.decorators import task


@task(name="Sum Two Numbers")
def add(x, y):
    print(x + y)
