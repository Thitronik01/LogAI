# Changelog

All notable changes to this project are documented in this file. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project intends to follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html) from its first release.

## [Unreleased]

### Added

- Project scaffold: package `logai_scan`, distribution `logai-scan`, command `logai` with `--version` and `--help`.
- Tooling: uv, Ruff, Pyright in strict mode, Pytest, Hypothesis, pre-commit.
- Test suite that runs with network access blocked, including name resolution.
- Continuous integration: lint, type check, tests on Python 3.12 and 3.13 under Linux and Windows, catalog validation, dependency audit and a CycloneDX SBOM.
- Community files: contribution guide with DCO, security policy, code of conduct, issue and pull request templates.
- First drafts of the architecture, detection limits, evidence levels, privacy and threat model documents.
- Architecture decision records 0001 to 0004.
