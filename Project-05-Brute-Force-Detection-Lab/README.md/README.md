# Project 05: Brute Force Detection Lab

## Project Overview

This project demonstrates how repeated failed login attempts can be detected using Windows Security Event Logs. The lab simulates a basic brute-force or password-guessing scenario against a local Windows user account and shows how a SOC analyst can identify the activity using Event Viewer and Event ID 4625.

## Objective

The objective of this lab was to:

- Confirm that Windows logon auditing was enabled.
- Confirm that a local test user account existed.
- Generate multiple failed login attempts using an incorrect password.
- Use Windows Event Viewer to filter Security logs.
- Identify repeated failed logon events using Event ID 4625.
- Review the failed logon event details.
- Document the findings in a SOC-style analysis report.

## Tools Used

- Windows Virtual Machine
- Administrator Command Prompt
- Windows Event Viewer
- Windows Security Logs
- auditpol
- runas command
- Local Windows user account

## Lab Environment

The lab was performed on a Windows virtual machine named:

```text
Windows-SOC-Lab
```

The test account used in the lab was:

```text
soc_test
```

## Steps Performed

### 1. Confirmed Logon Auditing

The following command was used to confirm that logon auditing was enabled:

```cmd
auditpol /get /subcategory:"Logon"
```

The result showed:

```text
Success and Failure
```

This confirmed that Windows was configured to record both successful and failed logon events.

Evidence:

```text
01-audit-policy-enabled.png
```

### 2. Confirmed Test User Account

The following command was used to confirm that the test user existed:

```cmd
net user soc_test
```

The command showed that the account was active and available for testing.

Evidence:

```text
02-test-user-confirmed.png
```

### 3. Generated Failed Login Attempts

Multiple failed login attempts were generated using the `runas` command:

```cmd
runas /user:soc_test cmd
```

A wrong password was entered several times to simulate repeated failed login attempts.

Evidence:

```text
03-failed-login-attempts-generated.png
```

### 4. Filtered Security Logs for Event ID 4625

Windows Event Viewer was opened and the Security log was filtered for:

```text
4625
```

Event ID 4625 represents a failed logon attempt.

Evidence:

```text
04-security-log-filter-4625.png
```

### 5. Detected Multiple Failed Logons

The filtered Security log showed multiple failed logon events. This pattern can indicate password guessing, brute-force activity, or unauthorized access attempts.

Evidence:

```text
05-multiple-failed-logons-detected.png
```

### 6. Reviewed Event 4625 Details

One failed logon event was opened and reviewed. The event showed:

```text
Event ID: 4625
Task Category: Logon
Keywords: Audit Failure
Account Name: soc_test
Failure Reason: Unknown user name or bad password
Computer: Windows-SOC-Lab
```

Evidence:

```text
06-event-4625-details.png
```

### 7. Created Analysis Report

A final brute-force detection analysis report was created to summarize the activity, evidence, risk level, and SOC analyst recommendation.

Evidence:

```text
07-brute-force-analysis-report.png
```

## Key Event ID

| Event ID | Meaning |
|---|---|
| 4625 | Failed logon attempt |

## Why This Matters

Multiple failed logon attempts against the same account can indicate:

- Password guessing
- Brute-force attack
- Unauthorized access attempt
- Account takeover attempt
- Misconfigured service or saved credentials

In a real SOC environment, repeated Event ID 4625 logs should be investigated to determine whether the activity is expected or suspicious.

## Risk Level

```text
Medium
```

## SOC Analyst Recommendation

Recommended actions:

- Investigate the source of the failed logons.
- Confirm whether the activity was expected.
- Check if other accounts were targeted.
- Monitor for repeated authentication failures.
- Review account lockout policy.
- Consider multi-factor authentication.
- Escalate if the activity appears suspicious or repeated.

## Skills Demonstrated

This project demonstrates:

- Windows Security Log analysis
- Event Viewer investigation
- Event ID 4625 identification
- Failed logon analysis
- Brute-force detection logic
- SOC analyst documentation
- Evidence collection
- Incident reporting

## Screenshots

The following screenshots were captured as evidence:

```text
01-audit-policy-enabled.png
02-test-user-confirmed.png
03-failed-login-attempts-generated.png
04-security-log-filter-4625.png
05-multiple-failed-logons-detected.png
06-event-4625-details.png
07-brute-force-analysis-report.png
```

## Project Status

```text
Completed
```

## Conclusion

This lab successfully demonstrated how repeated failed login attempts can be generated, detected, and analyzed using Windows Security Event Logs. The project shows beginner SOC analyst skills in authentication log analysis, brute-force detection, evidence gathering, and security reporting.
