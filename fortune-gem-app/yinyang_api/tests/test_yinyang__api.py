from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_yin_yang(self):
        with patch('random.choice') as r:
            r.return_value = 'yin'
            response = self.client.get(url_for('yin_yang'))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(b'yin', response.data)

    def test_get_fortune(self):
        with patch('random.choice') as r:
            r.return_value = 'Your shower singing will take you to great heights.'
            response = self.client.post(url_for('get_fortune'), data='yin')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(b'Your shower singing will take you to great heights.', response.data)

    def test_get_gem(self):
        with patch('random.choice') as r:
            r.return_value = 'Onyx'
            response = self.client.post(url_for('get_gem'), data='yin')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(b'Onyx', response.data)
