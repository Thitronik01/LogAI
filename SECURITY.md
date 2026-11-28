# Security policy

## Reporting a vulnerability

Please report vulnerabilities privately through GitHub: open the repository's **Security** tab and choose **Report a vulnerability**, or use this link:

<https://github.com/Thitronik01/LogAI/security/advisories/new>

Do not open a public issue and do not include real log data in a report. A synthetic input that reproduces the problem is ideal.

The project is maintained in spare time. Reports are read and answered as soon as possible; there is no guaranteed response time. Fixes are coordinated with the reporter before details are published, and reporters are credited unless they prefer otherwise.

## What counts

LogAI reads data that an attacker may have written and produces documents that people trust. Reports about the following are especially welcome:

- A crafted log, catalog or policy file that crashes the tool, makes it hang or makes it consume unbounded memory or disk space.
- Log content that reaches a report unencoded: script or markup in the HTML report, formulas in the CSV export, control sequences on the terminal.
- A way to recover source addresses or user names from any output, or any output that contains them in the first place.
- Any network access at runtime.
- Log content that makes a report state something the logs do not support.

## Supported versions

There is no release yet. Fixes are made on `main`.
