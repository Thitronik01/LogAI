# 0002: Catalog as YAML with a schema

- Status: Proposed
- Date: 2026-11-27

## Context

Which hosts belong to which AI service is the knowledge the whole tool rests on. A wrong entry makes a report state something untrue about an organisation. This knowledge changes often, should be open to contributions, and has to be checkable by a person without special tooling.

## Decision

- **One YAML file per service** in `catalog/services/`, validated against a JSON Schema in `catalog/schema/service.schema.json`.
- **A service is a product, not a provider.** A provider's chat application and its API are separate entries, because approval and terms, for example the use of data for training, differ between them.
- **An endpoint** consists of a host pattern, a match type (`exact` or `suffix`), a kind (`web`, `api`, `auth` or `cdn`), at least one source in the provider's own documentation and the date on which that source was checked. An endpoint without such a source is not entered.
- **Legal information** (the provider's seat, hosting regions, use of data for training, availability of a data processing agreement) is given per entry, each item with its source. `unknown` is a valid value. So is `varies`, where the answer depends on the plan, which logs cannot show.
- **Review status.** Every entry is `unreviewed` or `reviewed`. Entries start as `unreviewed`, and reports mark findings that rest on them.
- **Matching** compares host names label by label. `exact` matches the host itself; `suffix` matches the host and everything below it. The most specific pattern wins. A pattern belongs to exactly one service. A suffix pattern that is itself a public suffix, such as `com` or `github.io`, is rejected by validation. The public suffix list ships with the tool.
- **YAML is read with a safe loader only.**
- **The schema that ships inside the tool is the one that counts at runtime.** A catalog cannot bring its own.

## Consequences

- A change to one service is a small, readable diff in one file.
- The tool needs a YAML parser and a JSON Schema validator. They are added with the first-scan milestone.
- YAML guesses types: a date-like value becomes a date, `no` becomes false. The schema's types catch such surprises, and the loader will keep date-like values as text.
- Patterns are host names only. A service that shares its hosts with unrelated products cannot be expressed and is left out, see [detection limits](../detection-limits.md).
- A tampered catalog file is not detected until the catalog is signed, which is not part of the current work.

## Alternatives considered

- **JSON.** No comments, and noisier to write by hand.
- **TOML.** Awkward for lists of nested records.
- **One large file.** More merge conflicts, harder reviews.
- **A database file.** Not reviewable in a pull request.
- **Regular expressions as patterns.** Powerful, but hard to review, a classic source of patterns that match too much, and a risk of excessive run time on hostile input.
