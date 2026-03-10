import requests
from datetime import datetime

# Advanced SQL error signatures for professional detection
SQL_ERRORS = [
    "you have an error in your sql syntax",
    "mysql_fetch_array()",
    "is_numeric() expects parameter",
    "unclosed quotation mark after the character string",
    "quoted string not properly terminated",
    "postgresql query failed",
    "oracle error",
    "sqlite3.OperationalError",
    "java.sql.SQLException"
]

# Multiple payloads for unique vulnerability testing
PAYLOADS = ["'", "''", "';--", "\"", "\") OR 1=1--", "admin'--"]

def run_advanced_scan():
    print("="*60)
    print("   ADVANCED SQL VULNERABILITY SCANNER v2.0")
    print("="*60)
    
    # Taking direct user input
    target_url = input("\n[?] Enter Target URL (e.g., http://site.com/php?id=): ")
    
    if not target_url:
        print("[X] ERROR: No URL provided. Exiting...")
        return

    log_filename = "scan_report.txt"
    with open(log_filename, "a") as report:
        report.write(f"\n\n--- Scan Started: {datetime.now()} ---\n")
        report.write(f"Target: {target_url}\n")

        print(f"\n[*] Starting scan on: {target_url}")
        print("[*] Testing multiple payloads... please wait.\n")

        vulnerability_found = False

        for payload in PAYLOADS:
            test_url = f"{target_url}{payload}"
            try:
                # Sending request with a 10-second timeout
                response = requests.get(test_url, timeout=10)
                content = response.text.lower()
                
                for error in SQL_ERRORS:
                    if error in content:
                        result = f"[!!!] VULNERABLE: Payload '{payload}' triggered error: '{error}'"
                        print(result)
                        report.write(result + "\n")
                        vulnerability_found = True
                        break # Move to next payload after finding an error
                
            except Exception as e:
                error_msg = f"[X] CONNECTION ERROR for {payload}: {e}"
                print(error_msg)
                report.write(error_msg + "\n")

        if not vulnerability_found:
            safe_msg = "[+] RESULT: No common SQL vulnerabilities detected."
            print(safe_msg)
            report.write(safe_msg + "\n")
        
        print(f"\n[#] Scan Complete. Results saved in: {log_filename}")

if __name__ == "__main__":
    run_advanced_scan()
