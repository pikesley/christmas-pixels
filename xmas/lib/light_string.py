import platform

if 'arm' in platform.platform():  # nocov
    from neopixel import NeoPixel
    import board

else:
    from mock import MagicMock


class LightString:
    """Wrapper around the neopixel string."""

    def __init__(self, length):
        """Constructor."""
        self.length = length
        if 'arm' in platform.platform():
            self.pixels = NeoPixel(board.D18, self.length)  # nocov
        else:
            self.pixels = MagicMock()

    def light_one(self, colour, index):
        """Light up a single pixel."""
        self.pixels[index] = self.lookup(colour)

    def light_many(self, colours):
        """Apply an array of GRB colours to the pixels."""
        for index, colour in enumerate(colours):
            self.pixels[index] = self.lookup(colour)

    def light_all(self, colour):
        """Light up all the pixels."""
        self.pixels.fill(self.lookup(colour))

    def lookup(self, colour):
        """Lookup and gamma-correct the colour."""
        colours = {
            "green": [255, 0, 0],
            "yellow": [255, 255, 0],
            "red": [0, 255, 0],
            "magenta": [0, 255, 255],
            "blue": [0, 0, 255],
            "cyan": [255, 0, 255],
            "off": [0, 0, 0],
            "white": [255, 255, 255]
        }

        return colours[colour]
