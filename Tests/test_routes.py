import unittest
import json
from app import app


class TestServer(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.app = app.test_client()
        self.assertEqual(app.debug, True)

    def test_route_intervention_get_all(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_route_intervention_save(self):
        response = self.app.post('/add', content_type='application/json', data=json.dumps(
            {
                'client': 'Valentin',
                'description': 'Harny'
            }
        ))
        self.assertEqual(response.status_code, 200)