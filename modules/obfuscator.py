# obfuscator.py
from utils.obfuscation_utils import encode_payload

def run():
    payload = input("Enter payload to obfuscate: ")
    print("Encoded (Base64):", encode_payload(payload))
