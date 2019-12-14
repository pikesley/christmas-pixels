import json
from unittest.mock import MagicMock

from starlette.testclient import TestClient

from apiserver import APP
from workers.light_worker import light_one, light_all


class TestApiServer:
    """Test the API Server."""

    def setup_method(self):
        """Do some initialisation."""
        self.client = TestClient(APP)  # pylint: disable=W0201
        light_one.delay = MagicMock()
        light_all.delay = MagicMock()

    def test_all(self):
        """Test `/lights/all`."""
        payload = json.dumps({'colour': 'red'})
        response = self.client.post('/lights/all', data=payload)

        assert response.status_code == 200
        assert response.json() == {'colour': 'red'}

    def test_all_with_bad_params(self):
        """Test `/lights/all`."""
        payload = json.dumps({'colour': 'mauve'})
        response = self.client.post('/lights/all', data=payload)

        assert response.status_code == 422
        assert response.json() == {'detail': "Unknown colour 'mauve'"}

    def test_one(self):
        """Test `/lights/single/{index}`."""
        payload = json.dumps({'colour': 'green'})
        response = self.client.post('/lights/single/3', data=payload)

        assert response.status_code == 200
        assert response.json() == {'colour': 'green', 'index': 3}

    def test_one_with_bad_colour(self):
        """Test `/lights/single/{index}`."""
        payload = json.dumps({'colour': 'violet'})
        response = self.client.post('/lights/single/5', data=payload)

        assert response.status_code == 422
        assert response.json() == {'detail': "Unknown colour 'violet'"}

    def test_one_with_bad_index(self):
        """Test `/lights/single/{index}`."""
        payload = json.dumps({'colour': 'yellow'})
        response = self.client.post('/lights/single/99', data=payload)

        assert response.status_code == 422
        assert response.json() == {'detail': 'Invalid index 99'}

    def test_one_with_bad_index_and_bad_colour(self):
        """Test `/lights/single/{index}`."""
        payload = json.dumps({'colour': 'scarlet'})
        response = self.client.post('/lights/single/99', data=payload)

        assert response.status_code == 422
        assert response.json() == {
            'detail': "Invalid index 99, Unknown colour 'scarlet'"
        }
