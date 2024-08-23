import time
from repository import VirusTotalAPI
from utils import filter_urls

class URLScannerService:
    def __init__(self):
        self.api = VirusTotalAPI()

    def scan_url(self, url):
        filtered_urls = filter_urls([url])
        if not filtered_urls:
            return "Geçersiz URL"
        url = filtered_urls[0]
        analysis_id = self.api.scan_url(url)
        time.sleep(0.7)

        if analysis_id:
            scan_data = self.get_analysis_report_with_retry(analysis_id)
            if isinstance(scan_data, dict) and "data" in scan_data:
                return scan_data
            return "Tarama sonuçları alınamadı"
        return "URL taranamadı"

    def get_analysis_report_with_retry(self, analysis_id, max_retries=11, delay=2):
        """
        Tarama raporunu almak için tekrar deneme fonksiyonu. Queue'nun bitmesini bekler. Raporu completed durumunda alır. Ortalama 15-30 saniye arası sürüyor.
        max_retries: Maksimum deneme sayısı.
        delay: Bir sonraki deneme öncesinde bekleme süresi (saniye).
        """
        for _ in range(max_retries):
            scan_data = self.api.get_analysis_report(analysis_id)
            status = scan_data.get('data', {}).get('attributes', {}).get('status')
            if status != 'queued':
                return scan_data
            time.sleep(delay)  # "queued" durumundaysa delay kadar bekle.

        # Eğer tüm denemeler başarısız olursa son tarama sonucunu döndürün
        return scan_data
