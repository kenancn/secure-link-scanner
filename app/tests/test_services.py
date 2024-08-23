import unittest
from unittest.mock import patch
from services import URLScannerService

class TestURLScannerService(unittest.TestCase):

    @patch('services.VirusTotalAPI')
    def test_scan_url_success(self, mock_api):
        mock_api.return_value.scan_url.return_value = 'test_id'
        mock_api.return_value.get_analysis_report.return_value = {'data': {'attributes': {'status': 'completed'}}}

        service = URLScannerService()
        result = service.scan_url('http://example.com')
        self.assertIn('data', result)

    @patch('services.VirusTotalAPI')
    def test_scan_url_failed(self, mock_api):
        mock_api.return_value.scan_url.return_value = None

        service = URLScannerService()
        result = service.scan_url('http://example.com')
        self.assertEqual(result, "URL taranamadı")

if __name__ == '__main__':
    unittest.main()
