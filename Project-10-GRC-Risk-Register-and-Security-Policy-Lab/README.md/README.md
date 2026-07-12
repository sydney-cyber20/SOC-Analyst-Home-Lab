# Project 10: GRC Risk Register and Security Policy Lab

## Project Overview

This project demonstrates beginner Governance, Risk, and Compliance (GRC) skills. The lab focused on identifying cybersecurity risks, documenting those risks in a risk register, rating their severity, recommending security controls, and creating basic security policies for a small lab organization.

## Objective

The objective of this project was to:

- Create a GRC risk scenario.
- Identify important business and security assets.
- Document cybersecurity risks.
- Rate risks by likelihood and severity.
- Recommend security controls.
- Create basic security policies.
- Create a final GRC summary report.

## Company Scenario

```text
Company Name: Sydney Cyber Lab
```

Sydney Cyber Lab is a small organization that uses Windows endpoints, local user accounts, email, internet access, Windows Event Viewer, Splunk SIEM, and security logs.

The organization wants to improve cybersecurity governance, risk management, and compliance.

## Assets Reviewed

The following assets were reviewed:

1. Windows endpoints
2. User accounts
3. Administrator accounts
4. Email accounts
5. Security logs
6. Network traffic
7. Business data

## Main Risks Identified

The following cybersecurity risks were identified:

1. Weak passwords
2. Repeated failed login attempts
3. Phishing emails
4. Unused or disabled accounts not reviewed
5. Lack of MFA
6. Poor log monitoring
7. Unauthorized access

## Folder Structure

```text
Project-10-GRC-Risk-Register-and-Security-Policy-Lab/
├── README.md
├── Notes/
│   ├── grc-risk-scenario.txt
│   ├── cybersecurity-risk-register.txt
│   └── final-grc-summary-report.txt
├── Screenshots/
│   ├── 01-project-folder-created.png
│   ├── 02-grc-risk-scenario.png
│   ├── 03-cybersecurity-risk-register.png
│   ├── 04-password-security-policy.png
│   ├── 05-access-control-policy.png
│   ├── 06-log-monitoring-policy.png
│   └── 07-final-grc-summary-report.png
├── Policies/
│   ├── password-security-policy.txt
│   ├── access-control-policy.txt
│   └── log-monitoring-policy.txt
└── Templates/
```

## Risk Register Summary

| Risk | Asset Affected | Likelihood | Severity | Recommended Control |
|---|---|---|---|---|
| Weak passwords | User accounts | High | High | Use strong password rules and enable MFA |
| Repeated failed login attempts | Windows endpoints and user accounts | Medium | Medium | Enable account lockout and monitor Event ID 4625 |
| Phishing emails | Email accounts and users | High | High | Train users to identify and report phishing |
| Unused accounts not reviewed | User accounts | Medium | Medium | Review and disable unused accounts |
| Lack of MFA | User and administrator accounts | High | High | Enable MFA for important accounts |
| Poor log monitoring | Security logs and endpoints | Medium | High | Monitor Windows logs and SIEM alerts |
| Unauthorized access | Business data and systems | Medium | High | Apply least privilege and review permissions |

## Policies Created

### 1. Password Security Policy

A password policy was created to reduce the risk of weak or stolen passwords.

Main controls included:

- Minimum password length.
- Password complexity.
- No password sharing.
- Default password changes.
- MFA for important accounts.
- Account lockout after repeated failed attempts.
- Monitoring Event ID 4625.

Evidence:

```text
04-password-security-policy.png
```

### 2. Access Control Policy

An access control policy was created to ensure that only authorized users have access to systems, accounts, data, and security tools.

Main controls included:

- Least privilege access.
- Unique user accounts.
- Limited administrator access.
- Regular account reviews.
- Disabling unused or temporary accounts.
- Monitoring failed and successful logons.

Evidence:

```text
05-access-control-policy.png
```

### 3. Log Monitoring Policy

A log monitoring policy was created to ensure that security logs are collected, reviewed, and monitored.

Important Event IDs included:

```text
Event ID 4625 - Failed Logon
Event ID 4624 - Successful Logon
Event ID 4720 - User Account Created
Event ID 4672 - Special Logon
```

Main controls included:

- Reviewing failed login attempts.
- Investigating repeated failed logons.
- Checking successful logons after repeated failures.
- Reviewing new account creation.
- Monitoring administrator activity.
- Preserving evidence during investigations.

Evidence:

```text
06-log-monitoring-policy.png
```

## Recommended Controls

The project recommended the following security controls:

1. Use strong password requirements.
2. Enable multi-factor authentication where possible.
3. Enable account lockout policy.
4. Monitor Event ID 4625 for repeated failed logons.
5. Review user accounts and group memberships regularly.
6. Disable unused or temporary accounts.
7. Monitor Windows Security Logs and SIEM alerts.
8. Train users to identify phishing emails.
9. Apply least privilege access.
10. Document security incidents and preserve evidence.

## GRC Value

This project shows how cybersecurity governance, risk management, and compliance help reduce business risk.

It demonstrates how a risk register and security policies support:

- Better security decision-making
- Accountability
- Risk reduction
- Compliance readiness
- Incident prevention
- Stronger internal controls

## Skills Demonstrated

This project demonstrates:

- GRC documentation
- Risk identification
- Risk register creation
- Severity rating
- Control recommendation
- Password policy writing
- Access control policy writing
- Log monitoring policy writing
- Security governance basics
- Compliance-style documentation
- Security report writing

## Roles Supported

This project supports beginner roles such as:

- Junior GRC Analyst
- Cybersecurity Analyst
- Risk Analyst
- Compliance Assistant
- IT Governance Support
- SOC Analyst with documentation responsibilities

## Project Status

```text
Completed
```

## Conclusion

This lab demonstrated beginner GRC skills by identifying cybersecurity risks, documenting them in a risk register, rating their severity, recommending controls, and creating basic security policies. The project shows an understanding of how governance, risk management, and compliance support cybersecurity operations.
