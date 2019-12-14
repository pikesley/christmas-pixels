from pydantic import BaseModel  # pylint: disable=E0611


class Colour(BaseModel):
    """Model for a colour."""

    colour: str
