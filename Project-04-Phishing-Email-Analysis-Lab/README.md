# Phishing Email Analysis Lab

## Project Overview

This project demonstrates a basic phishing email analysis workflow from a SOC analyst perspective. The goal was to review a suspicious email sample, identify phishing indicators, analyze the sender and link, document indicators of compromise, and produce a final analyst conclusion.

The sample used in this lab was safely defanged using:

```text
hxxps
```

This prevents accidental clicking during analysis.

## Objective

The objective of this project was to:

- Review a suspicious email sample.
- Identify phishing indicators.
- Analyze the sender domain.
- Review basic email header details.
- Analyze a suspicious link safely.
- Document indicators of compromise.
- Write a final phishing analysis report.
- Capture screenshots as evidence for a cybersecurity portfolio.

## Tools Used

- macOS Notes
- TextEdit / Plain text notes
- Screenshot tool
- Manual phishing analysis process

## Lab Files

The project contains the following folders:

```text
Project-04-Phishing-Email-Analysis-Lab/
├── README.md
├── Notes/
└── Screenshots/
```

## Sample Email

The suspicious email pretended to be from PayPal and claimed that the user’s account would be suspended unless they verified their details immediately.

Sample sender:

```text
PayPal Security <support@paypa1-security.example.com>
```

Sample subject:

```text
Urgent: Your account will be suspended today
```

Suspicious link:

```text
hxxps://paypa1-security.example.com/login/verify-account
```

Evidence:

```text
01-sample-phishing-email.png
```

## Email Header Review

The email header details were reviewed to identify suspicious sender information.

Key observations:

- The sender domain was not the official PayPal domain.
- The domain used `paypa1` instead of `paypal`.
- The number `1` was used to imitate the letter `l`.
- The sender was impersonating PayPal Security.
- The subject line used urgency to pressure the recipient.

Evidence:

```text
02-email-header-review.png
```

## Suspicious Link Analysis

The suspicious URL was reviewed safely in a defanged format.

Observed link:

```text
hxxps://paypa1-security.example.com/login/verify-account
```

Key observations:

- The link does not use the official `paypal.com` domain.
- The domain attempts to imitate PayPal.
- The link contains a fake verification path.
- The email pressures the user to click quickly.
- The URL was defanged using `hxxps` to prevent accidental clicking.

Evidence:

```text
03-suspicious-link-analysis.png
```

## Phishing Indicators Identified

The email contained several common phishing indicators:

1. Fake sender domain.
2. Brand impersonation.
3. Urgent language.
4. Generic greeting.
5. Suspicious verification link.
6. Threat of account suspension.
7. Attempt to steal login credentials.

Evidence:

```text
04-phishing-indicators-identified.png
```

## Final Analysis Report

A final analyst report was created to summarize the case, indicators of compromise, risk level, and recommended SOC response.

Final conclusion:

```text
This email is a phishing attempt designed to steal user login credentials.
```

Evidence:

```text
05-final-analysis-report.png
```

## Indicators of Compromise

| Type | Indicator |
|---|---|
| Sender | support@paypa1-security.example.com |
| Domain | paypa1-security.example.com |
| URL | hxxps://paypa1-security.example.com/login/verify-account |
| Brand Impersonated | PayPal |

## Risk Level

```text
High
```

## Recommended SOC Action

Recommended actions:

- Do not click the link.
- Do not enter credentials.
- Report the email to the security team.
- Block the suspicious domain if seen in a real environment.
- Search for similar messages in user mailboxes.
- Educate users about brand impersonation and urgent phishing messages.

## Skills Demonstrated

This project demonstrates:

- Phishing email analysis
- Social engineering detection
- Suspicious sender identification
- Domain impersonation analysis
- Safe URL defanging
- IOC documentation
- SOC analyst reporting
- Evidence collection for a cybersecurity portfolio

## Screenshots

The following screenshots were captured as evidence:

```text
01-sample-phishing-email.png
02-email-header-review.png
03-suspicious-link-analysis.png
04-phishing-indicators-identified.png
05-final-analysis-report.png
```

## Project Status

```text
Completed
```

## Conclusion

This lab successfully demonstrated how to analyze a phishing email sample, identify suspicious indicators, document IOCs, and write a clear SOC analyst conclusion.

The project provides evidence of beginner-level phishing analysis skills that are useful for entry-level cybersecurity and SOC analyst roles.
