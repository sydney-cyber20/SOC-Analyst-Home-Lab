import re
from pathlib import Path


project_root = Path(__file__).resolve().parents[1]


input_file = project_root / "Data" / "sample-security-alert.txt"
output_file = project_root / "Output" / "ioc-analysis-report.txt"


text = input_file.read_text(encoding="utf-8")


ip_addresses = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text)


emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", text)


urls = re.findall(r"\b(?:hxxps?|https?)://[^\s]+", text)


domains = re.findall(r"\b(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}\b", text)


def remove_duplicates(items):
    clean_list = []
    for item in items:
        item = item.strip().strip(".,)")
        if item not in clean_list:
            clean_list.append(item)
    return clean_list


ip_addresses = remove_duplicates(ip_addresses)
emails = remove_duplicates(emails)
urls = remove_duplicates(urls)
domains = remove_duplicates(domains)


report = []


report.append("IOC Analysis Report")
report.append("")
report.append("Input File:")
report.append(str(input_file.name))
report.append("")
report.append("IP Addresses Found:")
for ip in ip_addresses:
    report.append(f"- {ip}")


report.append("")
report.append("Email Addresses Found:")
for email in emails:
    report.append(f"- {email}")


report.append("")
report.append("URLs Found:")
for url in urls:
    report.append(f"- {url}")


report.append("")
report.append("Domains Found:")
for domain in domains:
    report.append(f"- {domain}")


report.append("")
report.append("Summary:")
report.append(f"Total IP Addresses: {len(ip_addresses)}")
report.append(f"Total Email Addresses: {len(emails)}")
report.append(f"Total URLs: {len(urls)}")
report.append(f"Total Domains: {len(domains)}")


report.append("")
report.append("Analyst Note:")
report.append("These indicators should be reviewed during a security investigation. Suspicious domains, URLs, IP addresses, and email addresses can be used for threat hunting, phishing analysis, and SOC investigations.")


output_file.write_text("\n".join(report), encoding="utf-8")


print("IOC analysis completed.")
print(f"Report saved to: {output_file}")