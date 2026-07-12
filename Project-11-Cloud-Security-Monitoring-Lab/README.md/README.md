# Project 11: Cloud Security Monitoring Lab

## Project Overview

This project demonstrates beginner cloud security monitoring skills using a simulated cloud audit log file. The lab focused on reviewing cloud activity, identifying suspicious events, creating detection rules, and documenting findings in a cloud security monitoring report.

This project was completed using a simulated cloud platform, so no paid AWS, Azure, or Google Cloud account was required.

## Objective

The objective of this project was to:

- Create a cloud security monitoring scenario.
- Build a simulated cloud audit log file.
- Review cloud login and administrative activity.
- Identify suspicious cloud security events.
- Create basic cloud detection rules.
- Document cloud log analysis notes.
- Create a final cloud security monitoring report.

## Company Scenario

```text
Company Name: Sydney Cyber Lab
Environment: Simulated Cloud Platform
Risk Level: Medium
```

Sydney Cyber Lab uses cloud services to store business data, manage users, and allow remote access to company systems. The organization wants to monitor cloud activity for suspicious logins, privilege changes, failed access attempts, access key creation, and unusual administrative actions.

## Cloud Assets Reviewed

The following cloud assets were considered:

1. Cloud user accounts
2. Administrator accounts
3. Cloud storage
4. Audit logs
5. Login activity
6. Access keys
7. Security groups
8. Business data

## Main Security Concerns

The main security concerns reviewed in this lab were:

1. Failed cloud login attempts
2. Successful login after multiple failures
3. Administrator privilege changes
4. New user creation
5. Access key creation
6. Public storage exposure
7. Unusual login location
8. Unauthorized access to cloud data

## Folder Structure

```text
Project-11-Cloud-Security-Monitoring-Lab/
├── README.md
├── Data/
│   └── cloud-audit-logs.csv
├── Notes/
│   ├── cloud-security-scenario.txt
│   ├── cloud-log-analysis-notes.txt
│   └── cloud-security-monitoring-report.txt
├── Screenshots/
│   ├── 01-project-folder-created.png
│   ├── 02-cloud-security-scenario.png
│   ├── 03-simulated-cloud-audit-log.png
│   ├── 04-cloud-detection-rules.png
│   ├── 05-cloud-log-analysis-notes.png
│   └── 06-cloud-security-monitoring-report.png
└── Detections/
    └── cloud-detection-rules.txt
```

## Simulated Cloud Audit Log

A simulated cloud audit log file was created:

```text
cloud-audit-logs.csv
```

The log file contained events such as:

- Failed login attempts
- Successful login
- New user creation
- Administrator policy attachment
- Access key creation
- Storage permission change
- Unknown user login attempts

Evidence:

```text
03-simulated-cloud-audit-log.png
```

## Detection Rules Created

The following cloud security detection rules were documented:

### 1. Multiple Failed Cloud Login Attempts

Trigger when the same user has 5 or more failed login attempts.

Risk:

```text
Possible brute-force attack or password guessing
```

Severity:

```text
Medium
```

### 2. Successful Login After Multiple Failures

Trigger when a successful login happens after multiple failed login attempts for the same user.

Risk:

```text
Possible successful account compromise
```

Severity:

```text
High
```

### 3. Administrator Policy Attached

Trigger when administrator privileges are added to a user account.

Risk:

```text
Privilege escalation or unauthorized admin access
```

Severity:

```text
High
```

### 4. New Access Key Created

Trigger when a new access key is created.

Risk:

```text
Access keys can be abused for unauthorized cloud access
```

Severity:

```text
Medium
```

### 5. Cloud Storage Made Public

Trigger when cloud storage permissions are changed to public.

Risk:

```text
Sensitive business data may be exposed publicly
```

Severity:

```text
High
```

### 6. Unknown User Login Attempts

Trigger when login attempts are made using an unknown or invalid username.

Risk:

```text
Account enumeration or unauthorized access attempt
```

Severity:

```text
Medium
```

Evidence:

```text
04-cloud-detection-rules.png
```

## Key Findings

### Finding 1: Multiple Failed Login Attempts

User `john.user` had 5 failed login attempts from source IP `102.45.12.8`.

Severity:

```text
Medium
```

### Finding 2: Successful Login After Failures

User `john.user` successfully logged in after multiple failed attempts.

Severity:

```text
High
```

### Finding 3: New User Created

User `admin.user` created a new cloud user account named `temp.cloud`.

Severity:

```text
Medium
```

### Finding 4: Administrator Policy Attached

User `admin.user` attached administrator privileges to `temp.cloud`.

Severity:

```text
High
```

### Finding 5: Access Key Created

User `temp.cloud` created a new access key.

Severity:

```text
Medium
```

### Finding 6: Cloud Storage Made Public

User `temp.cloud` changed cloud storage bucket permissions to public.

Severity:

```text
High
```

### Finding 7: Unknown User Login Attempts

User `unknown.user` attempted login from source IP `185.199.108.1` and location `Unknown`.

Severity:

```text
Medium
```

## Risk Assessment

The most serious risks identified were:

1. Successful login after multiple failed attempts
2. Administrator privilege assignment
3. Public cloud storage permission change

These activities may indicate account compromise, privilege escalation, or public exposure of sensitive cloud data.

## Recommended Actions

Recommended security actions included:

1. Investigate `john.user` login activity.
2. Confirm whether `temp.cloud` was authorized.
3. Review administrator policy changes.
4. Rotate or disable suspicious access keys.
5. Change public cloud storage permissions back to private.
6. Review unknown user login attempts.
7. Enable MFA for all cloud users.
8. Create alerts for failed logins, privilege changes, access key creation, and public storage changes.
9. Review cloud audit logs regularly.
10. Preserve evidence for incident response.

## Skills Demonstrated

This project demonstrates:

- Cloud security monitoring basics
- Cloud audit log review
- Suspicious login analysis
- Failed login detection
- Privilege escalation detection
- Access key risk awareness
- Public storage exposure analysis
- Detection rule writing
- Cloud security reporting
- SOC-style investigation documentation

## Roles Supported

This project supports beginner roles such as:

- Junior Cloud Security Analyst
- SOC Analyst
- Cybersecurity Analyst
- Security Monitoring Analyst
- Cloud Support Analyst
- Junior Incident Response Analyst

## Project Status

```text
Completed
```

## Conclusion

This lab demonstrated how cloud audit logs can be reviewed to identify suspicious cloud security activity. The findings showed possible brute-force activity, account compromise, privilege escalation, access key risk, and public data exposure. The project also demonstrated how to create detection rules and document findings in a cloud security monitoring report.
