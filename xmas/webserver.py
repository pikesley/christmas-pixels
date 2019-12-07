import json

from flask import Flask
from flask import request
from flask import Response

from lib.light_string import LightString

COUNT = 50
APP = Flask(__name__)
APP.lights = LightString(COUNT)


@APP.route('/fill/<colour>', methods=['PATCH', 'POST'])
def fill(colour):
    """Fill all the pixels with one colour."""
    try:
        APP.lights.light_all(colour)
        return Response(
            json.dumps({'colour': colour}),
            status=200,
            mimetype='application/json'
        )
    except KeyError:
        APP.lights.light_all('off')
        return Response(
            json.dumps({'colour': None}),
            status=400,
            mimetype='application/json'
        )


@APP.route('/array', methods=['PATCH', 'POST'])
def array():
    """Apply an array of GRB colours to the pixels."""
    colours = json.loads(request.data.decode('utf-8'))['colours']
    APP.lights.light_many(colours)
    return Response(
        json.dumps({'success': True}),
        status=200,
        mimetype='application/json'
    )


@APP.route('/single/<index>', methods=['PATCH', 'POST'])
def single(index):
    """Light up a single pixel."""
    colour = json.loads(request.data.decode('utf-8'))['colour']
    APP.lights.light_one(colour, int(index))
    return Response(
        json.dumps({'success': True}), status=200, mimetype='application/json'
    )


if __name__ == "__main__":
    APP.run(host='0.0.0.0')
