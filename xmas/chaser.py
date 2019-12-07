import json
import random
import threading
import time

import requests

COUNT = 50
# LIGHTSHOST = 'xmas.local'
LIGHTSHOST = 'localhost'


def illuminate(colour, interval):
    """Continually light a randomly-chosen pixels with a weighted interval."""
    while True:
        index = random.randint(0, COUNT - 1)
        data = json.dumps({'colour': colour})
        requests.post(f'http://{LIGHTSHOST}:5000/single/{index}', data=data)
        time.sleep(random.random() * interval)


COLOURS = {
    'green': 1,
    'red':   2,
    'white': 10,
    'off':   5
}


if __name__ == '__main__':
    requests.post(f'http://{LIGHTSHOST}:5000/fill/green')
    time.sleep(5)

    THREADS = []

    for name, seconds in COLOURS.items():
        THREADS.append(
            threading.Thread(target=illuminate, args=(name, seconds)))

    for thread in THREADS:
        thread.start()
