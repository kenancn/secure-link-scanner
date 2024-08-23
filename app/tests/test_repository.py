import unittest
from unittest.mock import patch
from repository import VirusTotalAPI

class TestVirusTotalAPI(unittest.TestCase):

    @patch('repository.requests.post')
    def test_scan_url(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"data": {"id": "test_id"}}

        api = VirusTotalAPI()
        result = api.scan_url('http://example.com')
        self.assertEqual(result, 'test_id')

    @patch('repository.requests.get')
    def test_get_analysis_report(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"data": "test_data"}

        api = VirusTotalAPI()
        result = api.get_analysis_report('test_id')
        self.assertEqual(result, {"data": "test_data"})

if __name__ == '__main__':
    unittest.main()
