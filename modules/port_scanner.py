# port_scanner.py
import socket
from utils.logger import log

def run():
    target = input("Enter target IP: ")
    for port in range(1, 1025):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                log(f"[+] Port {port} is open")
            sock.close()
        except Exception as e:
            log(f"Error scanning port {port}: {e}")