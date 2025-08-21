#!/usr/bin/env python3
import requests
import sys
import re
from bs4 import BeautifulSoup

# ANSI colors
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

BASE_URL = "https://gtfobins.github.io/gtfobins/"

def extract_binaries(file_path):
    """
    Parse ls -ldb output lines and extract the binary names.
    Example input line:
    -rwsr-xr-x 1 root root 40152 Apr  9  2022 /usr/bin/passwd
    Output: passwd
    """
    binaries = set()
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            match = re.search(r"\s(/[^ ]+)$", line)
            if match:
                binaries.add(match.group(1).split("/")[-1])  # just the basename
    return sorted(binaries)

def check_gtfobins(binary):
    """
    Check GTFOBins for entries related to the binary.
    Returns (has_suid, sections, url)
    """
    url = BASE_URL + binary + "/"
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 404:
            return None, [], url
        soup = BeautifulSoup(resp.text, "html.parser")
        headers = soup.find_all("h2")
        sections = [h.get_text(strip=True) for h in headers]
        has_suid = any("SUID" in h for h in sections)
        return has_suid, sections, url
    except Exception as e:
        return f"Error: {e}", [], url

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    binaries = extract_binaries(input_file)

    print(f"[*] Checking {len(binaries)} binaries against GTFOBins...\n")
    for binary in binaries:
        result, sections, url = check_gtfobins(binary)
        if result is True:
            print(f"{RED}[+]{RESET} {binary} -> SUID FOUND ({url})")
        elif result is False:
            if sections:
                print(f"{YELLOW}[-]{RESET} {binary} -> No SUID entry, found: {', '.join(sections)} ({url})")
            else:
                print(f"{YELLOW}[-]{RESET} {binary} -> Found on GTFOBins but no recognizable sections ({url})")
        elif result is None:
            print(f"[ ] {binary} -> Not found on GTFOBins ({url})")
        else:
            print(f"[!] {binary} -> {result}")

if __name__ == "__main__":
    main()
