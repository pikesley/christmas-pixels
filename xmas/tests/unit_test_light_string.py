from lib.light_string import LightString

COUNT = 50


class TestLightString:
    """Test the LightString class."""

    def setup_method(self):
        """Do some pre-test setup."""
        self.lights = LightString(COUNT)  # pylint: disable=W0201

    def test_light_one(self):  #
        """Test it Lights One Pixel."""
        self.lights.light_one('red', 8)

        # pylint: disable=E1101
        self.lights.pixels.__setitem__.assert_called_once_with(
            8, [0, 255, 0]
        )

    def test_light_many(self):
        """Test it lights many pixels."""
        data = ['red', 'red', 'green', 'magenta', 'red']
        self.lights.light_many(data)

        # pylint: disable=E1101
        calls = list(map(tuple, self.lights.pixels.__setitem__.call_args_list))
        assert calls == [
            ((0, [0, 255, 0]), {}),
            ((1, [0, 255, 0]), {}),
            ((2, [255, 0, 0]), {}),
            ((3, [0, 255, 255]), {}),
            ((4, [0, 255, 0]), {})
        ]

    def test_light_all(self):
        """Test it lights all the pixels."""
        self.lights.light_all('blue')
        self.lights.pixels.fill.assert_called_once_with([0, 0, 255])
