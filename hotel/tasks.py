import random
from celery.decorators import task


@task(name="add_two_numbers")
def add(x, y):
    print(f'x: {x}, y: {y}')
    return x + y
