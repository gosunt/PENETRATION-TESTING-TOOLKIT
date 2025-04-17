from utils.logger import log
import requests
from bs4 import BeautifulSoup

def run():
    url = input("Enter URL to fingerprint: ")
    response = requests.get(url)
    headers = response.headers
    soup = BeautifulSoup(response.text, 'html.parser')

    server = headers.get("Server", "Unknown")
    powered_by = headers.get("X-Powered-By", "Unknown")
    
    cms = "WordPress" if "wp-content" in response.text else "Unknown"
    log(f"Server: {server}\nX-Powered-By: {powered_by}\nCMS: {cms}")