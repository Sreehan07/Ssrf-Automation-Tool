# Ssrf-Automation-Tool
Creating an automated tool for the SSRF process involves integrating multiple functionalities like gathering URLs, replacing parameter values with payloads, and monitoring the requests. Below is a Python script to automate these steps.

Ssrf Automation Tool

# Features of the Tool
URL Gathering: Uses waybackurls and gau to collect URLs.
SSRF Filtering: Filters URLs with potential SSRF parameters using gf.
#Payload Injection: 
Replaces parameter values with a Burp Collaborator payload using qsreplace.
#Fuzzing: 
Automates URL fuzzing with ffuf.
# Requirements
#Install required tools: 
waybackurls, gau, gf, qsreplace, ffuf.
Set up a Burp Collaborator payload.
Run the script and follow the prompts to perform the automated SSRF process!****

# Prompts While Running the Tool
#When prompted for the target domain:

Input the target domain in the format: example.com.
Example: Enter the target domain (e.g., example.com):
During the tool's execution:

#The script will display updates such as:
[+] Gathering URLs with waybackurls...
[+] Gathering URLs with gau...
[+] Combining and deduplicating URLs...
[+] Filtering URLs for SSRF candidates...
[+] Injecting payload into SSRF candidates...
[+] Fuzzing URLs with ffuf...
These are informative messages to track progress.
#After completion:

The script will output: [+] Process complete. Results saved in: ssrf_results
You can find all intermediate and final results in the ssrf_results directory.
Expected Output Files
waybackurls.txt: URLs gathered using waybackurls.
gau_urls.txt: URLs gathered using gau.
combined_urls.txt: Combined and deduplicated URLs.
ssrf_candidates.txt: URLs with potential SSRF parameters identified by gf.
ssrf_payloads.txt: URLs with injected payloads using qsreplace.
fuzz_results.txt: Results of fuzzing using ffuf.
# Prerequisites
Install required tools (waybackurls, gau, gf, qsreplace, ffuf).
Ensure the Burp Collaborator payload is configured correctly in the BURP_COLLABORATOR_PAYLOAD variable.
Verify that the output directory (ssrf_results) exi
