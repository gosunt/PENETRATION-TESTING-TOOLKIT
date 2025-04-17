import datetime

def log(message):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    entry = f"{timestamp} {message}"
    print(entry)
    with open("reports/generated_reports/latest.log", "a") as f:
        f.write(entry + "\n")
