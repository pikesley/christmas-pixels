from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel  # pylint: disable=E0611

from lib.light_string import LightString
from lib.light_string import LightStringException


class Colour(BaseModel):
    """Model for a basic colour."""

    colour: str


class IndexedColour(BaseModel):
    """Model for a colour with an index."""

    index: int
    colour: str


app = FastAPI()  # pylint: disable=C0103
app.lights = LightString(50)


@app.post('/lights/all')
async def set_all(payload: Colour):
    """Set all the lights to one colour."""
    try:
        app.lights.light_all(payload.colour)
    except LightStringException as exc:
        raise HTTPException(status_code=422, detail=str(exc))

    return {"colour": payload.colour}


@app.post('/lights/single')
async def set_one(payload: IndexedColour):
    """Set a single light to a colour."""
    try:
        app.lights.light_one(payload.index, payload.colour)
    except LightStringException as exc:
        raise HTTPException(status_code=422, detail=str(exc))

    return {"index": payload.index, "colour": payload.colour}
