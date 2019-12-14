from fastapi import FastAPI
from fastapi import HTTPException

from lib.conf import CONF
from models.colour import Colour
from workers.light_worker import light_one, light_all


APP = FastAPI()


@APP.post('/lights/all')
async def set_all(payload: Colour):
    """Set all the lights to one colour."""
    colour = payload.colour

    if colour in CONF['colours']:
        light_all.delay(colour)
        return {"colour": colour}

    else:
        message = f"Unknown colour '{colour}'"
        raise HTTPException(status_code=422, detail=message)


@APP.post('/lights/single/{index}')
async def set_one(payload: Colour, index: int):
    """Set a single light to a colour."""
    colour = payload.colour

    errors = []

    if not index < CONF['lights-count']:
        errors.append(f"Invalid index {index}")

    if colour not in CONF['colours']:
        errors.append(f"Unknown colour '{colour}'")

    if not errors:
        light_one.delay(index, colour)
        return {"index": index, "colour": colour}

    else:
        raise HTTPException(status_code=422, detail=', '.join(errors))
