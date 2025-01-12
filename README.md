# Ssrf-Automation-Tool
Creating an automated tool for the SSRF process involves integrating multiple functionalities like gathering URLs, replacing parameter values with payloads, and monitoring the requests. Below is a Python script to automate these steps.

Ssrf Automation Tool

Answer in chat instead
Features of the Tool
URL Gathering: Uses waybackurls and gau to collect URLs.
SSRF Filtering: Filters URLs with potential SSRF parameters using gf.
Payload Injection: Replaces parameter values with a Burp Collaborator payload using qsreplace.
Fuzzing: Automates URL fuzzing with ffuf.
Requirements
Install required tools: waybackurls, gau, gf, qsreplace, ffuf.
Set up a Burp Collaborator payload.
Run the script and follow the prompts to perform the automated SSRF process!****
