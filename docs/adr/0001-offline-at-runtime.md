# 0001: Offline at runtime

- Status: Proposed
- Date: 2026-11-27

## Context

LogAI processes logs that contain personal data and describe an organisation's network from the inside. Its users are information security and data protection officers who have to justify every tool that touches such data. A tool that can reach the network must be trusted not to send anything. A tool that cannot has nothing to prove.

## Decision

LogAI performs no network access at runtime. Not for updates, not for telemetry, not to look anything up, and not through a dependency.

- Everything the tool needs ships with it: the service catalog, the public suffix list, schemas and report templates.
- Schemas do not reference remote documents.
- **Enforced in tests.** The whole test session runs under a Python audit hook that refuses creating a socket, connecting, sending and every form of name resolution. The hook is installed before the package under test is imported, so access during import is caught as well. Attempts are recorded, so code that swallows the error still fails its test.
- **Enforced at lint time.** Importing the network modules of the standard library or a common HTTP library in the source tree is an error.
- **Reviewed.** Every new dependency is checked for network behaviour before it is added.

## Consequences

- There is no update check. Users learn about a new catalog through a release, and update by installing it or by replacing the catalog files.
- Nothing is looked up while a scan runs: no reverse DNS for logs without host names, no fresh public suffix list. Data shipped with a release ages until the next release, and the report states the date of its catalog.
- The guard works at the level of the Python interpreter. A native extension that opens sockets without going through the interpreter would not be seen. Dependencies with native code therefore get particular attention in review.
- Development tooling is not bound by this decision. Installing dependencies, the dependency audit and the first run of the type checker use the network.

## Alternatives considered

- **Online features behind a switch.** Rejected. "Offline unless enabled" is a weaker statement and harder to audit.
- **Review alone.** Rejected. A dependency update can introduce network access unnoticed; a failing test cannot be overlooked.
- **A pytest plugin that disables sockets.** Not chosen. The audit hooks of the standard library give this protection at a lower level, including name resolution, without a dependency.

## Not decided here

Installing the same hook in the command-line program itself, so that the shipped tool cannot open a socket even if a dependency tried to, is a possible hardening. It needs its own decision, because an audit hook cannot be removed once it is installed.
