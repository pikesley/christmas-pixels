from redis import Redis
from rq import Queue

q = Queue(connection=Redis('redis'))

q.enqueue(print, 'qoop')

p = Queue(connection=Redis('redis'))

p.enqueue(print, 'poop')

