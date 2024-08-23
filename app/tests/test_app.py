# app.py test
import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'G\xc3\xbcvenli Link Uygulamas\xc4\xb1', result.data)

    def test_post_url(self):
        result = self.app.post('/', data={'url': 'http://example.com'})
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Tarama Sonu\xc3\xa7lar\xc4\xb1:', result.data)

if __name__ == '__main__':
    unittest.main()
