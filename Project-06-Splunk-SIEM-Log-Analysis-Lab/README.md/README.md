# Project 06: Splunk SIEM Log Analysis Lab

## Project Overview

This project demonstrates how Splunk can be used as a SIEM-style tool to ingest, search, and analyze Windows security event data. The lab used a CSV file containing Windows logon events and focused on identifying failed logon activity and detecting a possible brute-force pattern.

## Objective

The objective of this lab was to:

- Create a sample Windows security event dataset.
- Upload the dataset into Splunk.
- Confirm that Splunk successfully ingested the events.
- Search for failed logon events.
- Use SPL to count failed logons by account.
- Create a simple brute-force detection search.
- Document the results in a SOC-style analysis report.

## Tools Used

- Splunk Enterprise
- Chrome browser
- macOS TextEdit / Notes
- CSV log data
- SPL search commands

## Lab Folder Structure

```text
Project-06-Splunk-SIEM-Log-Analysis-Lab/
├── README.md
├── Data/
├── Notes/
└── Screenshots/
```

## Data Source

The dataset used in this lab was a CSV file named:

```text
windows-security-events.csv
```

The dataset contained Windows logon events including:

- Event ID 4625: Failed Logon
- Event ID 4624: Successful Logon
- Account name
- Computer name
- Source host
- Logon type
- Failure reason
- Status

Evidence:

```text
02-sample-log-file-created.png
```

## Data Ingestion

The CSV file was uploaded into Splunk using the **Add Data** feature.

The data was ingested with:

```text
sourcetype=csv
```

Splunk successfully displayed 12 events from the uploaded file.

Evidence:

```text
03-splunk-home-screen.png
04-data-upload-started.png
05-events-ingested-in-splunk.png
```

## Search 1: Failed Logon Events

The following SPL search was used to identify failed logon events:

```spl
index=* sourcetype=csv Failed
```

This search returned 10 failed logon events.

Evidence:

```text
06-search-event-id-4625.png
```

## Search 2: Count Failed Logons by Account

The following SPL search was used to count failed logons by account name:

```spl
index=* sourcetype=csv Failed
| stats count by account_name
```

Result:

```text
account_name   count
soc_test       10
```

Evidence:

```text
07-stats-count-by-account.png
```

## Search 3: Brute Force Detection Logic

The following SPL search was used to detect accounts with 5 or more failed logon events:

```spl
index=* sourcetype=csv Failed
| stats count by account_name
| where count >= 5
```

Result:

```text
account_name   count
soc_test       10
```

This result shows that the account `soc_test` matched the brute-force detection logic.

Evidence:

```text
08-brute-force-pattern-detected.png
```

## Key Finding

The account `soc_test` had 10 failed logon attempts. Multiple failed logons against the same account can indicate:

- Password guessing
- Brute-force activity
- Unauthorized access attempt
- Account takeover attempt
- Misconfigured saved credentials

## Risk Level

```text
Medium
```

## SOC Analyst Recommendation

Recommended actions:

- Investigate the source of the failed logons.
- Confirm whether the activity was expected.
- Check whether other accounts were targeted.
- Review account lockout policy.
- Consider multi-factor authentication.
- Monitor for repeated authentication failures.
- Escalate if the pattern continues or appears suspicious.

## Final Analysis Report

A final SOC-style report was created to summarize the case, searches, findings, risk level, and recommendations.

Evidence:

```text
09-final-splunk-analysis-report.png
```

## Screenshots

The following screenshots were captured as evidence:

```text
01-project-folder-created.png
02-sample-log-file-created.png
03-splunk-home-screen.png
04-data-upload-started.png
05-events-ingested-in-splunk.png
06-search-event-id-4625.png
07-stats-count-by-account.png
08-brute-force-pattern-detected.png
09-final-splunk-analysis-report.png
```

## Skills Demonstrated

This project demonstrates:

- Splunk data ingestion
- SIEM-style log analysis
- SPL search basics
- Failed logon investigation
- Event ID 4625 analysis
- Brute-force detection logic
- Statistics using `stats count by account_name`
- SOC analyst reporting
- Evidence collection and documentation

## Project Status

```text
Completed
```

## Conclusion

This lab successfully demonstrated how Splunk can be used to ingest security logs, search failed logon events, count suspicious activity by account, and identify a brute-force pattern using SPL. This project strengthens beginner SOC analyst skills by showing practical SIEM log analysis and incident documentation.
