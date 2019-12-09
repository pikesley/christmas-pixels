from unittest import TestCase

from lib.light_string import LightString
from lib.light_string import LightStringException

COUNT = 50


class TestLightString:
    """Test the LightString class."""

    def setup_method(self):
        """Do some pre-test setup."""
        self.lights = LightString(COUNT)  # pylint: disable=W0201

    def test_light_one(self):  #
        """Test it Lights One Pixel."""
        self.lights.light_one(8, 'red')
        assert self.lights.pixels[8] == [0, 255, 0]

    def test_light_one_bad_colour(self):
        """Test it throws an exception with a bad colour."""
        with TestCase.assertRaises(self, LightStringException) as context:
            self.lights.light_one(10, 'maroon')

        assert str(context.exception) == "Unknown colour 'maroon'"
        assert self.lights.pixels[10] == (0, 0, 0)

    def test_light_one_bad_index(self):
        """Test it throws an exception with a bad index."""
        with TestCase.assertRaises(self, LightStringException) as context:
            self.lights.light_one(99, 'red')

        assert str(context.exception) == "Invalid index 99"

    def test_light_many(self):
        """Test it lights many pixels."""
        data = ['red', 'red', 'green', 'magenta', 'red']
        self.lights.light_many(data)

        assert self.lights.pixels[0:5] == [
            [0, 255, 0],
            [0, 255, 0],
            [255, 0, 0],
            [0, 255, 255],
            [0, 255, 0]
        ]

    def test_light_many_bad_colour(self):
        """Test it throws an exception with a bad colour."""
        data = ['red', 'red', 'green', 'azure', 'red']
        with TestCase.assertRaises(self, LightStringException) as context:
            self.lights.light_many(data)

        assert str(context.exception) == "Unknown colour 'azure'"
        assert self.lights.pixels[0] == [0, 255, 0]
        assert self.lights.pixels[3] == (0, 0, 0)

    def test_light_many_long_array(self):
        """Test it ignores extra array elements."""
        data = ['blue'] * 55
        self.lights.light_many(data)

        assert self.lights.pixels[COUNT - 1] == [0, 0, 255]

    def test_light_all(self):
        """Test it lights all the pixels."""
        self.lights.light_all('blue')
        self.lights.pixels.fill.assert_called_once_with([0, 0, 255])

    def test_light_all_bad_colour(self):
        """Test it throws an exception with a bad colour."""
        with TestCase.assertRaises(self, LightStringException) as context:
            self.lights.light_all('violet')

        assert str(context.exception) == "Unknown colour 'violet'"
        assert all(x == (0, 0, 0) for x in self.lights.pixels)
