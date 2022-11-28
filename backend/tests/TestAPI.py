import unittest
from os import getenv

import requests

test_url = getenv('API_URL') or 'http://localhost:5000'


class TestAPI(unittest.TestCase):
    def test_get_valid(self):
        res = requests.get(f'{test_url}/article/1')
        self.assertEqual(res.status_code, 200)

        data: dict = res.json()

        self.assertIsInstance(data, dict)

        self.assertIn('title', data.keys())
        self.assertIn('subtitle', data.keys())
        self.assertIn('content', data.keys())
        self.assertIn('headerImg', data.keys())
        self.assertIn('published', data.keys())

        self.assertIsInstance(data['published'], int)

        self.assertIsNotNone(data['title'])

    def test_get_large_number(self):
        res = requests.get(f'{test_url}/article/100000')
        self.assertEqual(res.status_code, 404)

    def test_get_negative_number(self):
        res = requests.get(f'{test_url}/article/-11')
        self.assertEqual(res.status_code, 404)

    def test_articles_is_list(self):
        res = requests.get(f'{test_url}/article/')
        self.assertEqual(res.status_code, 200)

        data = res.json()

        self.assertIsInstance(data, list)