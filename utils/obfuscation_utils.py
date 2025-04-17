# obfuscation_utils.py
import base64

def encode_payload(payload):
    return base64.b64encode(payload.encode()).decode()
