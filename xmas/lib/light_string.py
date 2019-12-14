import platform

from lib.conf import CONF
from lib.logger import LOGGER

if 'arm' in platform.platform():  # nocov
    from neopixel import NeoPixel
    import board


class LightString:
    """Wrapper around the neopixel string."""

    def __init__(self):
        """Construct."""
        self.length = CONF['lights-count']
        if 'arm' in platform.platform():
            self.pixels = NeoPixel(board.D18, self.length)  # nocov
        else:
            self.pixels = FakePixel(self.length)

    def light_one(self, index, colour):
        """Light up a single pixel."""
        self.pixels[index] = self.lookup(colour)

    def light_many(self, colours):
        """Apply an array of GRB colours to the pixels."""
        for index, colour in enumerate(colours):
            if index < self.length:
                self.light_one(index, colour)

    def light_all(self, colour):
        """Light up all the pixels."""
        self.pixels.fill(self.lookup(colour))

    def chase(self, lead_colour, chase_colour):
        """Chase a colour up the string."""
        for index in range(len(self.pixels)):
            self.light_one(min(self.length, index), lead_colour)
            self.light_one(max(0, index - 1), chase_colour)

    def lookup(self, colour):
        """Lookup the colour."""
        return CONF['colours'][colour]


class FakePixel(list):
    """Fake NeoPixels for testing."""

    def __init__(self, length):  # pylint: disable=W0231
        """Construct."""
        self.length = length
        for _ in range(self.length):
            self.append((0, 0, 0))

    def __setitem__(self, index, value):
        """Override [i] = foo."""
        LOGGER.info("Setting LED %s to %s", index, value)
        super().__setitem__(index, value)

    def fill(self, colour):
        """Pretend to fill the pixels."""
        LOGGER.info("Filling with %s", colour)
        for index, _ in enumerate(self):
            self[index] = colour
