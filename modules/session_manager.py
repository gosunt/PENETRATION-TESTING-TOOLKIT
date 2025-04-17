import json

def save_session(data, filename="session.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_session(filename="session.json"):
    try:
        with open(filename) as f:
            session = json.load(f)
            print("[+] Session loaded:\n", json.dumps(session, indent=2))
    except FileNotFoundError:
        print("[-] No saved session found.")
