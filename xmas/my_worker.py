from rq.worker import Worker
from random import random

class Counter:
    def __init__(self):
        self.count = random()

    def increment(self):
        print(self.count)
        self.count += 1
        print(self.count)

c = Counter()

class MyWorker(Worker):
    def perform_job(self, *args, **kwargs):
        result = super().perform_job(*args, **kwargs)
        c.increment()
        print(c.__dict__)
        print(id(c))
        return result

# rq worker --url redis://redis --worker-class 'my_worker.MyWorker'
# python queue-feeder.py
