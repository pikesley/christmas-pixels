import os

from celery import Celery

from lib.light_string import LightString

REDIS_HOST = 'localhost'
if os.getenv('REDIS_HOST'):
    REDIS_HOST = os.getenv('REDIS_HOST')  # nocov


APP = Celery('light_worker', broker=f"redis://{REDIS_HOST}")
LIGHTS = LightString()


@APP.task
def light_all(colour):
    """Proxy for LightString method."""
    LIGHTS.light_all(colour)  # nocov


@APP.task
def light_one(index, colour):
    """Proxy for LightString method."""
    LIGHTS.light_one(index, colour)  # nocov

# https://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html
