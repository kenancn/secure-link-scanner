

def filter_urls(urls):
    return list({url for url in urls if url.startswith('http')})
