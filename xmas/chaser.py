import json
import random
import threading
import time

import requests

COUNT = 50
# LIGHTSHOST = 'xmas.local'
LIGHTSHOST = 'localhost'
LOCK = threading.Lock()


def dot(colour, interval):
    """Continually light a randomly-chosen pixels with a weighted interval."""
    while True:
        index = random.randint(0, COUNT - 1)
        payload = json.dumps({'colour': colour, 'index': index})
        requests.post(
            f'http://{LIGHTSHOST}:5000/lights/single', data=payload)
        time.sleep(random.random() * interval)


DOTTERS = {
    'green': 1,
    'red':   2,
    'white': 10,
    'off':   5
}

if __name__ == '__main__':
    PAYLOAD = json.dumps({'colour': 'green'})
    requests.post(f'http://{LIGHTSHOST}:5000/lights/all', data=PAYLOAD)
    time.sleep(5)

    THREADS = []

    for name, seconds in DOTTERS.items():
        THREADS.append(
            threading.Thread(target=dot, args=(name, seconds)))

    for thread in THREADS:
        thread.start()
