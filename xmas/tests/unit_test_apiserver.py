import json

from starlette.testclient import TestClient

from apiserver import app


class TestApiServer:
    """Test the API Server."""

    def setup_method(self):
        """Do some initialisation."""
        self.client = TestClient(app)  # pylint: disable=W0201

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
        """Test `/lights/single`."""
        payload = json.dumps({'colour': 'green', 'index': 3})
        response = self.client.post('/lights/single', data=payload)
        assert response.status_code == 200
        assert response.json() == {'colour': 'green', 'index': 3}

    def test_one_with_bad_colour(self):
        """Test `/lights/single`."""
        payload = json.dumps({'colour': 'violet', 'index': 5})
        response = self.client.post('/lights/single', data=payload)
        assert response.status_code == 422
        assert response.json() == {'detail': "Unknown colour 'violet'"}

    def test_one_with_bad_index(self):
        """Test `/lights/single`."""
        payload = json.dumps({'colour': 'yellow', 'index': 99})
        response = self.client.post('/lights/single', data=payload)
        assert response.status_code == 422
        assert response.json() == {'detail': 'Invalid index 99'}

    def test_one_with_bad_index_and_bad_colour(self):
        """Test `/lights/single`."""
        payload = json.dumps({'colour': 'grey', 'index': 99})
        response = self.client.post('/lights/single', data=payload)
        assert response.status_code == 422
        assert response.json() == {'detail': "Unknown colour 'grey'"}
        # this should be richer
