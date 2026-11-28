# Threat model

Status: first draft. It names what is defended, against whom, and which defences exist. Most defences belong to the first-scan milestone and are marked as planned.

## What is protected

1. **The identities in the logs.** Source addresses and user names.
2. **The truth of the report.** People act on it.
3. **The machine and the person** that run the tool and open the report.
4. **The promise of being offline.**

## A. Someone who can write into the logs

Everyone on the monitored network decides what ends up in the logs: an employee, a guest device, malware, or a website that an employee visits. Host names, URLs and user names in a log are attacker-controlled.

| Attack | Defence | State |
| --- | --- | --- |
| A huge file, an endless line or an enormous number of lines exhausts memory or time. | Limits on file size, line length, line count and run time; lines are processed one at a time. | Planned |
| Malformed or undecodable lines crash the parser. | A parser returns an event or a counted rejection for every line; property tests feed it arbitrary input. | Planned |
| Markup in a host name runs as script when the report is opened. | No string from a log reaches the report; autoescaping; the report contains no scripts and a content security policy that forbids them. | Planned |
| A field that starts with `=`, `+`, `-` or `@` runs as a formula in a spreadsheet. | CSV cells are neutralised; no string from a log reaches the CSV. | Planned |
| Control sequences in a line manipulate the operator's terminal. | Error messages name the line number and the reason, never the content. | Planned |
| Planted lookups for a service cast suspicion on a network segment. | DNS yields at most `hint`; findings are worded as observations; the report states the limits. | Planned |

## B. Someone who supplies a catalog or a policy file

| Attack | Defence | State |
| --- | --- | --- |
| YAML that constructs objects or expands to enormous size. | Safe loader only, enforced at lint time; size limits. | Lint rule in place, rest planned |
| A pattern as broad as a public suffix turns ordinary traffic into findings. | Validation rejects such patterns. | Planned |
| An entry with invented endpoints. | Every endpoint needs a source and a date; entries start as unreviewed and are marked as such in reports; a person reviews them. | Process in place |
| A tampered catalog is distributed. | Signing the catalog. | Not yet planned |

## C. The supply chain

| Attack | Defence | State |
| --- | --- | --- |
| A vulnerable or malicious dependency. | Few dependencies, standard library first; a lockfile with hashes; an audit against known vulnerabilities on every change and weekly; an SBOM per build. | In place |
| A dependency that contacts the network. | The test session blocks sockets and name resolution; network imports are a lint error; review of every new dependency. | In place |
| A compromised GitHub Action. | Actions are pinned to commits; the workflow token is read-only; credentials are not persisted. | In place |

## D. The operator

The tool could be used to watch individuals instead of auditing the use of services.

| Risk | Defence | State |
| --- | --- | --- |
| Reports that single out a person or a device. | Pseudonymisation on reading; output aggregated per service; grouping only with a minimum group size; no option for output per source. | Planned |

The limit of this defence: the operator holds the raw logs and can analyse them with other tools.

## Out of scope

- A compromised machine on which the tool runs.
- Users who avoid being logged. See [detection limits](detection-limits.md).
- The correctness of the logs. A tampered log yields a tampered report.
- What happens to a report after it has been written.
