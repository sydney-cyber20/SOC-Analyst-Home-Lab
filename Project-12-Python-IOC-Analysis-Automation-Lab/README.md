# Project 12: Python IOC Analysis Automation Lab

## Project Overview

This project demonstrates beginner cybersecurity automation using Python. The lab focused on creating a Python script that reads a security alert text file, extracts possible indicators of compromise (IOCs), and saves the results into an IOC analysis report.

This project shows how Python can help SOC analysts and cybersecurity analysts work faster by automating repetitive analysis tasks.

## Objective

The objective of this project was to:

- Create a cybersecurity automation scenario.
- Build a sample security alert text file.
- Write a Python IOC extraction script.
- Extract IP addresses, domains, URLs, and email addresses.
- Save extracted indicators into an output report.
- Document the automation process with screenshots and notes.

## Company Scenario

```text
Company Name: Sydney Cyber Lab
Project Type: Python IOC Analysis Automation
Risk Level: Low
```

Sydney Cyber Lab receives security indicators from phishing emails, cloud audit logs, endpoint alerts, and suspicious network traffic. The SOC team wants a simple Python script that can read a text file, identify possible indicators of compromise, and save the results into an output report.

## Indicators of Compromise Reviewed

The script extracted the following IOC types:

1. IP addresses
2. Domains
3. URLs
4. Email addresses

## Folder Structure

```text
Project-12-Python-IOC-Analysis-Automation-Lab/
├── README.md
├── Data/
│   └── sample-security-alert.txt
├── Notes/
│   └── python-ioc-analysis-scenario.txt
├── Screenshots/
│   ├── 01-project-folder-created.png
│   ├── 02-python-ioc-analysis-scenario.png
│   ├── 03-sample-security-alert-file.png
│   ├── 04-python-ioc-extractor-script.png
│   ├── 05-python-script-executed.png
│   └── 06-ioc-analysis-output-report.png
├── Scripts/
│   └── ioc_extractor.py
└── Output/
    └── ioc-analysis-report.txt
```

## Sample Security Alert File

A sample security alert file was created:

```text
sample-security-alert.txt
```

The file included suspicious indicators such as:

- Suspicious email sender
- Suspicious phishing URL
- Suspicious domain
- Source IP address
- Cloud login source IP
- Additional suspicious URL
- Additional email address

Evidence:

```text
03-sample-security-alert-file.png
```

## Python Script Created

The Python script was created as:

```text
ioc_extractor.py
```

The script used Python regular expressions to extract:

- IP addresses
- Email addresses
- URLs
- Domains

The script also removed duplicate results and saved the output into a report.

Evidence:

```text
04-python-ioc-extractor-script.png
```

## Script Execution

The script was executed from Terminal using:

```bash
python3 Scripts/ioc_extractor.py
```

Successful output:

```text
IOC analysis completed.
Report saved to: Output/ioc-analysis-report.txt
```

Evidence:

```text
05-python-script-executed.png
```

## IOC Analysis Output Report

The script created the following output file:

```text
ioc-analysis-report.txt
```

The output report included:

- IP addresses found
- Email addresses found
- URLs found
- Domains found
- Total count of each IOC type
- Analyst note

Evidence:

```text
06-ioc-analysis-output-report.png
```

## Example IOCs Extracted

Examples of indicators extracted from the sample file included:

### IP Addresses

```text
185.199.108.1
102.45.12.8
```

### Email Addresses

```text
support@paypa1-security.example.com
admin-alerts@unknown-example.org
```

### URLs

```text
hxxps://paypa1-security.example.com/login/verify-account
hxxp://malicious-update.example.net/download
```

### Domains

```text
paypa1-security.example.com
malicious-update.example.net
unknown-example.org
```

## Why This Matters

SOC analysts often review security alerts, phishing emails, logs, and incident reports manually. Python automation can help analysts extract useful indicators from large amounts of text faster and more consistently.

This type of automation supports:

- Threat hunting
- Phishing investigation
- Alert enrichment
- IOC collection
- Incident response
- Security reporting

## Skills Demonstrated

This project demonstrates:

- Python scripting basics
- Regular expression usage
- File reading and writing
- IOC extraction
- Basic security automation
- Threat intelligence support
- SOC analyst workflow support
- Output report generation
- Cybersecurity documentation

## Roles Supported

This project supports beginner roles such as:

- SOC Analyst
- Cybersecurity Analyst
- Threat Intelligence Assistant
- Security Automation Assistant
- Junior Detection Analyst
- Junior Incident Response Analyst

## Project Status

```text
Completed
```

## Conclusion

This lab demonstrated how Python can be used to automate basic IOC extraction from a security alert text file. The project showed how to identify IP addresses, domains, URLs, and email addresses, then save the results into a simple IOC analysis report. This project supports beginner cybersecurity automation and SOC analyst skills.
