# Project 07: Windows User and Group Management Lab

## Project Overview

This project demonstrates basic Windows local user and group management from an IT Support, IAM, and security operations perspective. The lab focused on creating local user accounts, creating a local security group, adding a user to the group, resetting a password, disabling a temporary account, and verifying the final user and group configuration.

## Objective

The objective of this lab was to:

- Create local Windows user accounts.
- Create a local security group.
- Add a user to a security group.
- Reset a temporary user account password.
- Disable a temporary user account.
- Verify user account status and group membership.
- Document the process as evidence for a cybersecurity portfolio.

## Tools Used

- Windows Virtual Machine
- Administrator Command Prompt
- PowerShell
- Windows local user management commands
- Screenshot tool
- TextEdit / Notes

## Lab Environment

The lab was performed on a Windows virtual machine named:

```text
Windows-SOC-Lab
```

## Accounts and Group Used

Local users created:

```text
analyst_user
temp_contractor
```

Local security group created:

```text
SOC_Team
```

## Steps Performed

### 1. Opened Administrator Command Prompt

An Administrator Command Prompt was opened to perform local user and group management tasks.

Evidence:

```text
02-admin-command-prompt-open.png
```

### 2. Created Local Users

The following commands were used to create two local users:

```cmd
net user analyst_user P@ssw0rd123! /add
net user temp_contractor TempP@ss123! /add
```

Evidence:

```text
03-users-created.png
```

### 3. Created Local Security Group

The following command was used to create a local security group:

```cmd
net localgroup SOC_Team /add
```

Evidence:

```text
04-security-group-created.png
```

### 4. Added User to Security Group

The following command was used to add `analyst_user` to the `SOC_Team` group:

```cmd
net localgroup SOC_Team analyst_user /add
```

The group membership was confirmed using:

```cmd
net localgroup SOC_Team
```

Evidence:

```text
05-user-added-to-group.png
```

### 5. Reset Temporary User Password

The following command was used to reset the `temp_contractor` account password:

```cmd
net user temp_contractor NewTempP@ss456!
```

Evidence:

```text
06-password-reset-performed.png
```

### 6. Disabled Temporary User Account

The following command was used to disable the `temp_contractor` account:

```cmd
net user temp_contractor /active:no
```

The account status was confirmed using:

```cmd
net user temp_contractor
```

The result showed:

```text
Account active: No
```

Evidence:

```text
07-user-account-disabled.png
```

### 7. Verified Users and Group Membership

PowerShell was used to verify group membership and user account status:

```powershell
Get-LocalGroupMember SOC_Team
Get-LocalUser analyst_user,temp_contractor | Select Name,Enabled
```

The output confirmed:

```text
analyst_user was a member of SOC_Team
analyst_user was enabled
temp_contractor was disabled
```

Evidence:

```text
08-users-and-groups-confirmed.png
```

### 8. Created User Management Analysis Report

A final report was created to summarize the lab activity, commands used, verification steps, key findings, and recommendations.

Evidence:

```text
09-user-management-analysis-report.png
```

## Key Findings

1. `analyst_user` was successfully created.
2. `temp_contractor` was successfully created.
3. `SOC_Team` was successfully created as a local security group.
4. `analyst_user` was added to the `SOC_Team` group.
5. `temp_contractor` password was reset.
6. `temp_contractor` was disabled.
7. Final verification confirmed correct user and group status.

## Why This Matters

User and group management is important for:

- Identity and access management
- Access control
- User onboarding
- User offboarding
- Least privilege
- Account lifecycle management
- IT support operations
- SOC investigations involving user accounts

Unused, temporary, or contractor accounts should be disabled when no longer needed to reduce the risk of unauthorized access.

## Risk Level

```text
Low
```

## SOC / IT Support Recommendation

Recommended actions:

- Follow the principle of least privilege.
- Give users only the access they need.
- Review group memberships regularly.
- Disable temporary accounts when they are no longer required.
- Document all user account changes.
- Monitor account creation and modification events in Windows Security Logs.

## Skills Demonstrated

This project demonstrates:

- Windows local user creation
- Windows local group creation
- Group membership management
- Password reset
- Account disabling
- PowerShell verification
- Access control basics
- Identity and access management basics
- IT Support documentation
- SOC analyst evidence collection

## Screenshots

The following screenshots were captured as evidence:

```text
01-user-management-folder-created.png
02-admin-command-prompt-open.png
03-users-created.png
04-security-group-created.png
05-user-added-to-group.png
06-password-reset-performed.png
07-user-account-disabled.png
08-users-and-groups-confirmed.png
09-user-management-analysis-report.png
```

## Project Status

```text
Completed
```

## Conclusion

This lab successfully demonstrated beginner Windows user and group management skills. The project shows the ability to create users, manage security groups, reset passwords, disable accounts, verify access status, and document user account changes. These are useful skills for IT Support, Service Desk, SOC Analyst, IAM, and junior cybersecurity roles.
