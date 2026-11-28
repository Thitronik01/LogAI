# Architecture

Status: first draft. Only the scaffold exists so far, that is the command-line entry point and the tooling around it. The pipeline below is the design for the first-scan milestone. Each section says what is implemented.

## Shape

One command-line program. It reads log exports from disk and writes a report to disk. There is no server, no database, no background process and no network access ([ADR 0001](adr/0001-offline-at-runtime.md)).

## Pipeline (planned)

```
log export -> intake -> parser -> pseudonymisation -> catalog match -> policy -> aggregation -> report
```

| Stage | Package | Responsibility |
| --- | --- | --- |
| Intake | `ingest` | Accept a file. Enforce limits on file size, line length, line count and run time. Decode. |
| Parser | `parsers` | Turn one physical line into one normalised event or one counted rejection. One module per log format. |
| Pseudonymisation | `privacy` | Replace the source identifier by a keyed hash as soon as the line is parsed. |
| Catalog match | `catalog` | Assign the destination host to a catalogued service, or to none. |
| Policy | `policy` | Attach the organisation's own status: sanctioned, unsanctioned or unlisted. |
| Aggregation | `analysis`, `privacy` | Per service: evidence level, number of events, time range, bytes, number of distinct sources. Optionally per group, with a minimum group size. |
| Report | `report` | Write `findings.json`, `findings.csv` and a self-contained `report.html`. |

## Invariants

These hold across all stages. Reviews check them first.

1. **No network.** Enforced in tests and at lint time (ADR 0001). Implemented.
2. **Limits before interpretation.** A file, a line or a run that exceeds its limit is stopped before its content is interpreted. Exceeding the file size, line count or time limit aborts the run without writing a report, because a partial report would look complete.
3. **Rejected lines are counted.** A line that cannot be read is counted with its reason and shown in the report. It is never dropped silently.
4. **Only numbers and times cross from a log into the output.** Service names and host patterns come from the catalog, group names from the operator's mapping file. No string taken from a log line is written to a report or to an error message. Error messages name the line number and the reason.
5. **Output is encoded regardless.** HTML is rendered with autoescaping. CSV cells are protected against formula injection.
6. **Source identifiers are pseudonymised as they are read and never written to disk** ([ADR 0004](adr/0004-pseudonymisation-and-minimum-group-size.md)).
7. **Determinism.** The same input with the same catalog yields a byte-identical `findings.json`. The only timestamp in a report is its declared run time.

## What exists today

| Path | Content |
| --- | --- |
| `src/logai_scan/names.py` | The project's names, defined once. A test rejects any other occurrence in the source tree. |
| `src/logai_scan/cli.py` | The command with `--version` and `--help`. |
| `tests/conftest.py` | The network guard for the test session. |
| `scripts/validate_catalog.py` | Placeholder for catalog validation. It reports that nothing was validated and fails as soon as a catalog directory exists. |
| `.github/workflows/ci.yml` | Lint, type check, tests, catalog validation, dependency audit, SBOM. |

## Dependencies

There are no runtime dependencies yet. The first-scan milestone is expected to add three: Jinja2 for HTML with autoescaping, a JSON Schema validator for the catalog and the policy file, and a YAML parser that is used through its safe loader only. Each is introduced in the pull request that first uses it, with its purpose and the alternative that was considered.

Aggregation starts on the standard library. The parsers read line by line in Python in order to enforce limits and count rejections, so a data-frame library would not speed up the slowest stage. Whether one is added later is decided on measurements and recorded as an ADR.

## Report (planned)

- `findings.json` is the machine-readable result and the reference for determinism.
- `findings.csv` is the same result for spreadsheets.
- `report.html` is one self-contained file: no external references, no scripts.

The report's texts are kept apart from its template, so that further languages can be added without touching the template. German comes first. Keys in JSON and CSV are English.

The visual design will be taken from `brand/templates/report/` once it exists.
