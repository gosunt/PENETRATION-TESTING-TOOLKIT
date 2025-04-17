# waf_detector.py
import requests
from utils.logger import log

def run():
    url = input("Enter URL to check WAF: ")
    waf_signatures = ["cloudflare", "sucuri", "akamai", "aws"]
    r = requests.get(url)
    headers = str(r.headers).lower()
    for sig in waf_signatures:
        if sig in headers:
            log(f"[!] WAF detected: {sig}")
            return
    log("[-] No WAF detected")