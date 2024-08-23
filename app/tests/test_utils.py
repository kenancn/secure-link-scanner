import unittest
from utils import filter_urls

class TestUtils(unittest.TestCase):
    def test_filter_urls(self):
        urls = [
            "http://example.com",
            "https://example.org",
            "ftp://example.net",
            "/relative/path"
        ]
        filtered = filter_urls(urls)
        self.assertIn("http://example.com", filtered)
        self.assertIn("https://example.org", filtered)
        self.assertNotIn("ftp://example.net", filtered)
        self.assertNotIn("/relative/path", filtered)

if __name__ == '__main__':
    unittest.main()
