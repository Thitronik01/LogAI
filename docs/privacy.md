# Privacy

For data protection officers and employee representatives. Status: first draft. It describes the design that the first-scan milestone implements; nothing on this page is implemented yet. The decision is recorded in [ADR 0004](adr/0004-pseudonymisation-and-minimum-group-size.md).

This page is not legal advice. Whether and how an organisation may analyse its logs depends on its own legal situation, including data protection law, employment law and agreements with employee representatives. LogAI cannot answer that question. It is built so that the analysis needs as little personal data as possible.

## What is processed

Log exports contain personal data: source IP addresses, sometimes user names, and the hosts that were contacted. LogAI reads these files from local disk. It sends nothing anywhere and has no telemetry ([ADR 0001](adr/0001-offline-at-runtime.md)).

## What LogAI does with it

- **Pseudonymisation on reading.** Each source identifier, an IP address or a user name, is replaced by a keyed hash (HMAC-SHA256) as soon as its line has been parsed. The key is generated at random for every run, kept in memory only and gone when the run ends.
- **Pseudonyms stay inside.** They serve to count distinct sources. They are not written to any output file. Because every run has a new key, two runs cannot be linked through them.
- **Aggregated output.** By default the output holds one entry per service: evidence level, number of events, time range, bytes and number of distinct sources. No entry describes a single source.
- **Grouping only with a minimum size.** If the operator supplies a mapping from network ranges to group names, results can be broken down by group. Groups with fewer than five observed sources are merged. Five is the default and can be raised.
- **No text from the log reaches the output.** Only counts, byte totals and times. No URLs, no user agents, no host names as they appeared in the log.

## What LogAI does not do

- No listing per person or per device.
- No timeline of an individual's activity.
- No linking of sources across runs.
- No storage beyond the report files it is asked to write.

## What remains with the operator

- **The raw logs.** LogAI neither changes nor deletes them. Whoever holds the logs can still look up individuals with other tools. Pseudonymisation protects the report, not the log.
- **Lawfulness, purpose and retention** of the analysis and of its reports.
- **Involving** the data protection officer and employee representatives where that is required.
- **Sensible groups.** Groups should be defined so that merging is the exception.

## Residual risks

- **Small networks.** "3 distinct sources" says a lot in a network of four people. The count of distinct sources in the default output is not subject to a minimum size.
- **Uniform groups.** A minimum group size hides an individual among others. It does not help when every member of a group did the same thing.
- **Time ranges** can narrow down who was present.
- **During a run** the raw identifiers and the key are in the memory of the process. Pseudonymised data remains personal data.
