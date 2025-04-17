import os
from datetime import datetime

def generate():
    html = """
    <html><head><title>Scan Report</title></head><body>
    <h1>Scan Report - {date}</h1>
    <p>This is an auto-generated report.</p>
    </body></html>
    """.format(date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    with open("reports/generated_reports/report.html", "w") as f:
        f.write(html)
    print("[+] HTML report generated at reports/generated_reports/report.html")