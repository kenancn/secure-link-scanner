import requests
import os
from dotenv import load_dotenv

load_dotenv()

class VirusTotalAPI:
    API_URL = os.getenv('API_URL')
    API_KEY = os.getenv('VIRUSTOTAL_API_KEY')
    
    def __init__(self):
        self.headers = {
            "x-apikey": self.API_KEY,
            "content-type": "application/x-www-form-urlencoded",
            "accept": "application/json"
        }

    def scan_url(self, url): 
        # Verilen URL için VirusTotal taraması başlatılır.
        response = requests.post(f"{self.API_URL}/urls", data={"url": url}, headers=self.headers)
        if response.status_code == 200:
            return response.json()["data"]["id"]
        return None

    def get_analysis_report(self, analysis_id):
        response = requests.get(f"{self.API_URL}/analyses/{analysis_id}", headers=self.headers)
        if response.status_code == 200:
            return response.json()
        return None
