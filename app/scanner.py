import re

# A dictionary of our threat patterns
RULES = {
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "RSA Private Key": r"-----BEGIN RSA PRIVATE KEY-----",
    "Generic API Key": r"(?i)(api_key|apikey|secret)[=:\s]+['\"]([a-zA-Z0-9]{20,})['\"]"
}

def scan_file(filepath):
    """Scans a single file for secrets and returns a list of findings."""
    findings = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line_number, line in enumerate(f, 1):
                for rule_name, pattern in RULES.items():
                    if re.search(pattern, line):
                        findings.append({
                            "file": filepath,
                            "line": line_number,
                            "type": rule_name,
                            "match": line.strip()[:50] # Truncate so we don't print full secrets
                        })
    except UnicodeDecodeError:
        pass # Skip binary files (like images or compiled binaries)
    
    return findings