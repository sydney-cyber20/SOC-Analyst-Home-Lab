# Windows Sysmon Endpoint Monitoring Lab

## Project Overview

This project demonstrates the setup of a Windows endpoint monitoring lab using **Sysmon** and **Windows Event Viewer**. The goal of the lab is to simulate a basic SOC analyst workflow by collecting endpoint telemetry, generating system activity, and reviewing security-relevant events.

The lab was completed inside a Windows 11 virtual machine named:

```text
Windows-SOC-Lab
```

## Objective

The objective of this project was to:

- Set up a Windows 11 virtual machine for endpoint monitoring.
- Install and configure Sysmon using a custom Sysmon configuration file.
- Generate endpoint activity from the Windows system.
- Confirm that Sysmon logs were being collected successfully.
- Identify and document a Sysmon **Event ID 1: Process Create** event.
- Capture screenshots as evidence for a cybersecurity portfolio.

## Tools Used

- Windows 11 Virtual Machine
- UTM Virtual Machine Manager
- Sysinternals Suite for ARM64
- Sysmon
- Sysmon configuration file
- Windows Event Viewer
- Command Prompt

## Lab Steps Completed

### 1. Windows VM Setup

A Windows 11 virtual machine was created and configured as the endpoint machine for the lab.

The machine was renamed to:

```text
Windows-SOC-Lab
```

This helps make the endpoint easy to identify when reviewing logs and screenshots.

Evidence:

```text
01-windows-vm-running.png
```

### 2. Sysmon Installation

Sysmon was installed from the Sysinternals Suite for ARM64.

The Sysmon configuration file was loaded during installation using Command Prompt with administrator privileges.

Command used:

```cmd
Sysmon64a.exe -accepteula -i "..\sysmonconfig-export.xml"
```

The installation confirmed that:

```text
Sysmon64a installed.
SysmonDrv installed.
SysmonDrv started.
Sysmon64a started.
```

Evidence:

```text
02-sysmon-installed.png
```

### 3. Sysmon Log Verification

After installation, Event Viewer was opened to confirm that Sysmon logs were being collected.

The Sysmon log path used was:

```text
Applications and Services Logs
Microsoft
Windows
Sysmon
Operational
```

Sysmon events appeared successfully under the **Operational** log.

Evidence:

```text
03-sysmon-operational-logs.png
```

### 4. Activity Generation

Basic Windows activity was generated to create new Sysmon events.

Commands used:

```cmd
whoami
hostname
ipconfig
tasklist
```

After refreshing Event Viewer, the number of Sysmon events increased, confirming that Sysmon was actively collecting endpoint activity.

Evidence:

```text
04-process-events-generated.png
```

### 5. Process Create Event Analysis

A Sysmon **Event ID 1: Process Create** event was opened and reviewed in Event Viewer.

The event showed process execution details such as:

```text
Process Create
Image
Process ID
User
Computer
Event ID
Task Category
```

The captured event confirmed that Sysmon was recording process execution activity on the endpoint.

Evidence:

```text
05-event-id-1-process-create.png
```

## Key Sysmon Event IDs Observed

| Event ID | Event Name | Meaning |
|---|---|---|
| 1 | Process Create | A new process was started on the system |
| 4 | Sysmon Service State Changed | Sysmon service started or changed state |
| 13 | Registry Value Set | A registry value was created or modified |
| 22 | DNS Query | A DNS query was made by a process |

## What I Learned

Through this project, I learned how to:

- Set up a Windows endpoint lab environment.
- Install Sysmon on Windows.
- Apply a Sysmon configuration file.
- Navigate Event Viewer.
- Locate Sysmon Operational logs.
- Identify important Sysmon event IDs.
- Understand the importance of process creation logs in SOC investigations.
- Collect screenshot evidence for a cybersecurity portfolio.

## Why This Project Matters

Sysmon is widely used in cybersecurity environments because it provides detailed endpoint telemetry that helps analysts detect suspicious activity.

A SOC analyst can use Sysmon logs to investigate:

- Suspicious process execution
- Malware behavior
- PowerShell abuse
- Registry changes
- Network connections
- DNS queries
- Parent-child process relationships

This project shows practical beginner-level SOC analyst skills in endpoint monitoring and log analysis.

## Screenshots

The following screenshots were captured as evidence:

```text
01-windows-vm-running.png
02-sysmon-installed.png
03-sysmon-operational-logs.png
04-process-events-generated.png
05-event-id-1-process-create.png
```

## Project Status

```text
Completed
```

## Conclusion

This lab successfully demonstrated how to install and configure Sysmon on a Windows endpoint, generate system activity, and review security logs in Event Viewer.

The project provides strong evidence of hands-on SOC analyst skills, including endpoint monitoring, log collection, and process event analysis.
