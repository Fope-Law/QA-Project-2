from flask import url_for
from flask_testing import TestCase
import requests_mock 

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as mocker:
            mocker.get('http://yinyang_api:2020/yin_yang', text = 'yang')
            mocker.post('http://yinyang_api:2020/get_fortune', text = 'You will be labelled a fool in your time of greatest need...')
            mocker.post('http://yinyang_api:2020/get_gem', text = 'Nephrite')
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Omen: You will be labelled a fool in your time of greatest need... Lucky Gem: Nephrite', response.data)
