import argparse
import sys
from app.scanner import scan_file

def main():
    parser = argparse.ArgumentParser(description="Scan files for hardcoded secrets.")
    parser.add_argument("filenames", nargs="*", help="Files to scan")
    args = parser.parse_args()

    total_findings = []

    # Scan each file passed as an argument
    for filename in args.filenames:
        findings = scan_file(filename)
        total_findings.extend(findings)

    # Output results and set exit code
    if total_findings:
        print("\n[!] CRITICAL: Secrets detected in source code!")
        for finding in total_findings:
            print(f"  -> {finding['file']}:{finding['line']} - [{finding['type']}]")
        
        # Exit with code 1 to block the git commit
        sys.exit(1) 
    else:
        print("[+] No secrets found. Code is clean.")
        sys.exit(0)

if __name__ == "__main__":
    main()