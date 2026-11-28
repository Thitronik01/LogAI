## What and why

<!-- One topic per pull request. Link the issue if there is one. -->

## How to review

<!-- Where to start reading and what to try out. -->

## Security-critical areas

Tick what this pull request touches. A ticked box asks for a review by someone with security experience.

- [ ] Parsers
- [ ] File intake (limits on size, lines and time)
- [ ] Pseudonymisation or aggregation
- [ ] Report output (HTML, CSV, JSON)
- [ ] Catalog loading or matching
- [ ] None of these

## New dependencies

<!-- For each new library: its purpose and the alternative you considered. Standard library first. Write "none" if there are none. -->

## AI tools involved

<!-- Required. Name every AI tool that contributed (for example Claude Code, Codex, Copilot) and what it did. Write "none" if no AI tool was involved. -->

## Checklist

- [ ] Tests cover the change; parsers also have property tests
- [ ] `uv run ruff format --check .`, `uv run ruff check .`, `uv run pyright` and `uv run pytest` pass
- [ ] This pull request contains no real log data; all test data is synthetic
- [ ] Documentation is updated; architecture decisions have an ADR
- [ ] Commits follow Conventional Commits and carry a sign-off
