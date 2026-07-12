# Project 09: Incident Response Report Lab

## Project Overview

This project demonstrates a beginner incident response investigation based on repeated failed login attempts against a Windows user account. The lab follows a SOC-style workflow: detection, triage, timeline creation, evidence review, containment recommendations, and final reporting.

The incident scenario is based on brute-force detection activity from earlier Windows Event Viewer and Splunk SIEM labs.

## Objective

The objective of this lab was to:

- Create an incident response scenario.
- Triage a security alert.
- Build an incident timeline.
- Summarize evidence from Windows Security Logs and Splunk.
- Recommend containment and security improvements.
- Create a final incident response report.

## Incident Summary

```text
Incident Title: Multiple Failed Login Attempts Against Local User Account
Incident Type: Brute-force / password guessing attempt
Severity: Medium
Affected System: Windows-SOC-Lab
Affected Account: soc_test
Detection Sources: Windows Security Event Logs and Splunk SIEM
Related Event ID: 4625 - Failed Logon
```

## Tools and Evidence Sources

- Windows Event Viewer
- Windows Security Logs
- Splunk SIEM
- Event ID 4625
- Notes / TextEdit
- Screenshots from Project 05 and Project 06

## Folder Structure

```text
Project-09-Incident-Response-Report-Lab/
├── README.md
├── Notes/
│   ├── incident-scenario.txt
│   ├── alert-triage-notes.txt
│   ├── incident-timeline.txt
│   ├── evidence-summary.txt
│   ├── recommendations-and-containment.txt
│   └── final-incident-response-report.txt
├── Screenshots/
│   ├── 01-project-folder-created.png
│   ├── 02-incident-scenario-created.png
│   ├── 03-alert-triage-notes.png
│   ├── 04-incident-timeline.png
│   ├── 05-evidence-summary.png
│   ├── 06-recommendations-and-containment.png
│   └── 07-final-incident-response-report.png
└── Templates/
```

## Incident Response Workflow

### 1. Incident Scenario Created

An incident scenario was created for repeated failed login attempts against the local Windows account `soc_test`.

Evidence:

```text
02-incident-scenario-created.png
```

### 2. Alert Triage Completed

The alert was reviewed to determine:

- Whether the account was valid.
- Whether the activity was expected.
- Whether multiple failed logons were observed.
- Whether the activity could indicate brute-force behavior.
- Whether Event ID 4624 should be checked for successful logons after failures.

Evidence:

```text
03-alert-triage-notes.png
```

### 3. Incident Timeline Created

A timeline was created showing the order of investigation activities:

1. Audit policy confirmed.
2. Test account confirmed.
3. Failed login attempts generated.
4. Windows Security Logs reviewed.
5. Event ID 4625 identified.
6. Splunk analysis performed.
7. Failed logons counted.
8. Detection logic applied.
9. Incident classified.
10. Recommendations created.

Evidence:

```text
04-incident-timeline.png
```

### 4. Evidence Summary Created

Evidence was summarized from Windows Event Viewer and Splunk.

Key evidence included:

- Logon auditing was enabled.
- The account `soc_test` existed.
- Multiple failed login attempts were generated.
- Event Viewer showed Event ID 4625 failed logons.
- Splunk showed 10 failed logon events for `soc_test`.
- Splunk detection logic identified accounts with 5 or more failed logons.

Evidence:

```text
05-evidence-summary.png
```

### 5. Recommendations and Containment Created

Containment actions and security recommendations were documented.

Containment actions included:

- Confirm whether the activity was expected.
- Review the affected account.
- Temporarily disable the account if suspicious.
- Check whether other accounts were targeted.
- Review the source of failed login attempts.
- Preserve Windows Event Viewer and Splunk evidence.

Evidence:

```text
06-recommendations-and-containment.png
```

### 6. Final Incident Response Report Created

A final report was created to document the incident from start to finish.

The report included:

- Executive summary
- Investigation summary
- Evidence summary
- Key finding
- Impact
- Containment actions
- Recommendations
- Conclusion

Evidence:

```text
07-final-incident-response-report.png
```

## Key Finding

The account `soc_test` experienced repeated failed logon attempts. This pattern may indicate brute-force activity, password guessing, or unauthorized access attempts.

## Impact

No successful unauthorized login was confirmed in this lab. However, repeated failed logons against a valid account can increase the risk of account compromise.

## Risk Level

```text
Medium
```

## Recommendations

Recommended improvements include:

1. Enable account lockout policy.
2. Use strong password requirements.
3. Enable multi-factor authentication where possible.
4. Monitor Event ID 4625.
5. Create SIEM alerts for repeated failed logons.
6. Review user accounts regularly.
7. Disable unused or temporary accounts.
8. Investigate failed logon sources.
9. Preserve logs and evidence during investigations.

## Skills Demonstrated

This project demonstrates:

- Incident response documentation
- Alert triage
- Brute-force investigation
- Windows Security Log interpretation
- Splunk SIEM evidence review
- Incident timeline creation
- Evidence summary writing
- Containment recommendation writing
- SOC-style final reporting
- Security communication and documentation

## Why This Matters

Incident response reporting is an important SOC analyst skill. Analysts must be able to investigate alerts, organize evidence, explain what happened, assess risk, recommend actions, and document findings clearly.

This project shows the ability to move beyond detection and produce professional investigation documentation.

## Project Status

```text
Completed
```

## Conclusion

This lab demonstrated the full beginner SOC incident response process using a brute-force login scenario. The project covered detection, triage, timeline creation, evidence review, containment recommendations, and final reporting.
