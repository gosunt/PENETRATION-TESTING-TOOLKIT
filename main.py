import argparse
from modules import (
    port_scanner, brute_forcer, web_vulnerability_scanner,
    exploit_detector, waf_detector, obfuscator, payload_generator,
    bypass_techniques, fuzzing_engine, rce_detector, 
    fingerprinting, session_manager, report_generator
)

def main():
    parser = argparse.ArgumentParser(description="Advanced Pentest Toolkit")
    parser.add_argument("--scan", help="Run port scan", action="store_true")
    parser.add_argument("--brute", help="Run brute force attack", action="store_true")
    parser.add_argument("--web", help="Run web vulnerability scan", action="store_true")
    parser.add_argument("--fingerprint", help="Run fingerprinting module", action="store_true")
    parser.add_argument("--report", help="Generate report from logs", action="store_true")
    parser.add_argument("--resume", help="Resume previous session", action="store_true")
    args = parser.parse_args()

    if args.scan:
        port_scanner.run()
    if args.brute:
        brute_forcer.run()
    if args.web:
        web_vulnerability_scanner.run()
    if args.fingerprint:
        fingerprinting.run()
    if args.resume:
        session_manager.load_session()
    if args.report:
        report_generator.generate()

if __name__ == "__main__":
    main()
