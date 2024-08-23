from flask import Flask, render_template, request, Response, stream_with_context
from services import URLScannerService
from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

app = Flask(__name__)
url_scanner = URLScannerService()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        page_url = request.form.get('url')
        if page_url:
            return Response(stream_with_context(scan_urls(page_url)), content_type='text/html')
    return render_template('index.html')

def scan_urls(page_url):
    yield render_template('index_start.html', checked_url=page_url)

    urls = extract_urls(page_url)

    # URL'leri paralel olarak taramak için ThreadPoolExecutor fonksiyonu kullanılıyor.
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(url_scanner.scan_url, url): url for url in urls}

        for future in as_completed(futures):
            url = futures[future]
            try:
                result = future.result()
            except Exception as exc:
                result = f'Tarama başarısız oldu: {exc}'
            yield render_template('index_row.html', url=url, result=result)

    yield render_template('index_end.html')

def extract_urls(page_url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    }
    response = requests.get(page_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    # set kullanarak benzersiz linkler döndürülüyor. Aynı linkleri taramamak için.
    urls = set([a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('http')])
    return urls

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
