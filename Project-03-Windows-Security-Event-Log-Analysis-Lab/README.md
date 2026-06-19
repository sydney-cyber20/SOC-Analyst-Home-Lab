# Windows Security Event Log Analysis Lab

## Project Overview

This project demonstrates basic Windows Security Event Log analysis using a Windows 11 virtual machine. The goal was to simulate a SOC analyst workflow by enabling logon auditing, creating a test user, generating failed and successful logon activity, and reviewing Windows Security events in Event Viewer.

The lab was completed on a Windows virtual machine named:

```text
Windows-SOC-Lab
```

## Objective

The objective of this project was to:

- Open and review Windows Security logs.
- Enable logon auditing for successful and failed logon events.
- Create a local test user account.
- Generate a failed logon event.
- Locate and analyze Windows Security Event ID 4625.
- Locate and analyze Windows Security Event ID 4624.
- Locate and analyze Windows Security Event ID 4720.
- Capture screenshots as evidence for a cybersecurity portfolio.

## Tools Used

- Windows 11 Virtual Machine
- UTM Virtual Machine Manager
- Windows Event Viewer
- Windows Security Logs
- Command Prompt
- Auditpol
- Net User
- Runas

## Lab Steps Completed

### 1. Opened Windows Security Logs

Event Viewer was opened and the Security log was accessed using:

```text
Event Viewer
→ Windows Logs
→ Security
```

This log contains Windows authentication and account activity events.

Evidence:

```text
01-security-log-opened.png
```

### 2. Enabled Logon Auditing

Logon auditing was enabled for both successful and failed logon attempts.

Command used:

```cmd
auditpol /set /subcategory:"Logon" /success:enable /failure:enable
```

The policy was then verified using:

```cmd
auditpol /get /subcategory:"Logon"
```

The result showed:

```text
Success and Failure
```

Evidence:

```text
02-audit-policy-enabled.png
```

### 3. Created a Test User

A local test user account was created for generating account activity.

Command used:

```cmd
net user soc_test P@ssw0rd123 /add
```

The account was verified using:

```cmd
net user soc_test
```

Evidence:

```text
03-test-user-created.png
```

### 4. Generated a Failed Logon Attempt

A failed logon attempt was generated using the `runas` command with an incorrect password.

Command used:

```cmd
runas /user:soc_test cmd
```

The wrong password was entered intentionally to generate a failed authentication event.

The command returned:

```text
1326: The user name or password is incorrect.
```

Evidence:

```text
04-failed-runas-command.png
```

### 5. Analyzed Failed Logon Event

The Windows Security log was searched for:

```text
Event ID 4625
```

This event represents a failed logon attempt.

Event reviewed:

```text
Event ID: 4625
Task Category: Logon
Keywords: Audit Failure
```

Evidence:

```text
05-failed-logon-event-4625.png
```

### 6. Analyzed Successful Logon Event

The Windows Security log was reviewed for:

```text
Event ID 4624
```

This event represents a successful logon.

Event reviewed:

```text
Event ID: 4624
Task Category: Logon
Keywords: Audit Success
```

Evidence:

```text
06-successful-logon-event-4624.png
```

### 7. Analyzed User Account Creation Event

The Windows Security log was reviewed for:

```text
Event ID 4720
```

This event represents the creation of a new user account.

Event reviewed:

```text
Event ID: 4720
Task Category: User Account Management
Message: A user account was created
```

Evidence:

```text
07-user-account-created-event-4720.png
```

## Key Windows Security Event IDs

| Event ID | Event Name | Meaning |
|---|---|---|
| 4624 | Successful Logon | A user successfully logged on |
| 4625 | Failed Logon | A user failed to log on |
| 4672 | Special Logon | Special privileges were assigned to a logon session |
| 4720 | User Account Created | A new local user account was created |
| 4722 | User Account Enabled | A user account was enabled |
| 4724 | Password Reset Attempt | An attempt was made to reset a password |
| 4728 | User Added to Security Group | A user was added to a security-enabled group |
| 4738 | User Account Changed | A user account was modified |

## What I Learned

Through this project, I learned how to:

- Navigate Windows Event Viewer.
- Access and review Windows Security logs.
- Enable audit policies using `auditpol`.
- Generate authentication events in a lab environment.
- Identify failed logon events using Event ID 4625.
- Identify successful logon events using Event ID 4624.
- Identify user account creation events using Event ID 4720.
- Collect evidence for a SOC analyst portfolio.
- Understand how Windows logs can support security investigations.

## Why This Project Matters

SOC analysts often investigate Windows authentication activity to identify suspicious behavior such as:

- Failed login attempts
- Brute-force activity
- New user account creation
- Privileged logons
- Unusual account changes
- Unauthorized access attempts

This project demonstrates practical beginner-level Windows log analysis skills that are relevant to SOC analyst work.

## Screenshots

The following screenshots were captured as evidence:

```text
01-security-log-opened.png
02-audit-policy-enabled.png
03-test-user-created.png
04-failed-runas-command.png
05-failed-logon-event-4625.png
06-successful-logon-event-4624.png
07-user-account-created-event-4720.png
```

## Project Status

```text
Completed
```

## Conclusion

This lab successfully demonstrated how to enable Windows logon auditing, generate authentication events, and analyze key Windows Security Event IDs in Event Viewer.

The project provides evidence of hands-on SOC analyst skills, including Windows log analysis, account activity investigation, and security event documentation.
