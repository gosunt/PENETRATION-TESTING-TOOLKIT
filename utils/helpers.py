# helpers.py
def sanitize_url(url):
    return url if url.startswith("http") else "http://" + url
