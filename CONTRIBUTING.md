# Contributing

Thank you for considering a contribution. The project is in pre-alpha and maintained in spare time, so please open an issue before you start on anything larger than a small fix. That avoids work on something that will not be merged.

## Scope

LogAI is a command-line tool that analyses log exports offline and writes a report. It is deliberately not a dashboard, a server, a database, an agent on end devices or a browser extension, and it does not block traffic, inspect TLS, compute risk scores or send telemetry. Proposals in those directions will be declined.

## Ground rules

1. **No network access at runtime.** No import that fetches anything. The tests run with sockets blocked.
2. **Logs are hostile input.** Any field may have been written by an attacker. Every import has limits on size, line count and time. No `eval`, no `pickle`, YAML only through `safe_load`.
3. **Encode all output.** HTML is rendered with autoescaping. CSV exports are protected against formula injection.
4. **Data minimisation by default.** Source addresses and user names are pseudonymised as they are read. Output is aggregated per service.
5. **No real logs, anywhere.** Not in the repository, not in issues, not in pull requests. Test data is synthetic and recognisable as such: `.test` host names and the documentation address ranges `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24` and `2001:db8::/32`.
6. **Honest wording.** Code and reports speak of "observed connections" and "upload volume". Findings never use words that claim more than a log can show, such as "leak" or "violation".
7. **Every finding carries an evidence level.** See [docs/evidence-levels.md](docs/evidence-levels.md).
8. **Catalog entries need a source and a date.** Do not guess host names.
9. **Justify new dependencies.** Standard library first. Each new library is named in the pull request with its purpose and the alternative you considered.
10. **`brand/` is maintained separately.** Open an issue for change requests instead of editing it.

## Setup

Install [uv](https://docs.astral.sh/uv/), then:

```
uv sync
uv run pre-commit install
```

Before you push:

```
uv run ruff format .
uv run ruff check .
uv run pyright
uv run pytest
uv run python scripts/validate_catalog.py
```

## Branches, commits and pull requests

- One pull request, one topic. Branches are named `feat/...`, `fix/...` or `docs/...`.
- Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/).
- Every commit carries a sign-off (`git commit -s`), see below.
- Every change in behaviour comes with a test. Parsers additionally get property tests.
- Architecture decisions are recorded as a short ADR in `docs/adr/`.
- Code, comments, commit messages and public documentation are written in English.
- Changes to parsers, file intake, pseudonymisation, report output or catalog matching are security-critical. Mark them in the pull request so that they get a review by someone with security experience.

## Developer Certificate of Origin

Contributions are accepted under the Developer Certificate of Origin. By adding a `Signed-off-by` line to a commit you certify the following for that commit:

```
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.


Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.
```

`git commit -s` adds the line for you, using the name and address from your Git configuration:

```
Signed-off-by: Your Name <you@example.org>
```

Use a name and an address that you are willing to have on public record. Automated dependency updates are exempt from the sign-off.

## AI tools

AI tools may be used. Every pull request states which AI tools were involved and what they did; the pull request template has a field for it. You remain responsible for the contribution, and the sign-off is yours, not the tool's.

## Security

Do not report vulnerabilities in public issues. See [SECURITY.md](SECURITY.md).

## Conduct

This project follows a [code of conduct](CODE_OF_CONDUCT.md).
