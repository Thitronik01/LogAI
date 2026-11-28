# 0004: Pseudonymisation and minimum group size

- Status: Proposed
- Date: 2026-11-27

## Context

Logs name the device, and often the person, behind every request. The purpose of LogAI is to show which services are reached from a network, not who reaches them. A tool that could be turned into a means of watching individuals would rightly be rejected by data protection officers and employee representatives. At the same time, a count of distinct sources is useful: one device that polls an API is something else than two hundred people using a chat application.

## Decision

### Pseudonymisation

1. Each source identifier, an IP address or a user name, is replaced by HMAC-SHA256 of its normalised form as soon as its line has been parsed.
2. The key is 32 random bytes from the operating system, generated for every run. It is never written anywhere and is gone when the run ends.
3. Pseudonyms are used to count distinct sources. They are never written to an output file.
4. IP addresses are brought into a canonical form before hashing, so that one address in two spellings counts once.

### Default output

The default output holds one entry per service. No entry describes a single source, and there is no option that produces output per source.

### Groups

5. Grouping is optional and requires a mapping file from network ranges to group names, supplied by the operator.
6. The size of a group is the number of distinct sources observed for it in the log. It is not the size of its network range.
7. The minimum group size is 5 by default and can be raised.
8. Groups below the minimum are merged into one remainder group.
9. If the remainder group is itself below the minimum, the smallest of the other groups is merged into it, repeatedly, until the remainder reaches the minimum. Otherwise the figures of the remainder could be computed by subtracting the shown groups from the totals.
10. If no arrangement reaches the minimum, there is no breakdown by group, and the report says why.
11. Sources that match no range form a group of their own, to which the same rules apply.

## Consequences

- Pseudonyms cannot be compared across runs. This is intended: nothing can be accumulated about a source over time.
- Because pseudonyms never reach the output, the random key does not disturb determinism. The same input and catalog yield a byte-identical `findings.json`.
- Counts of distinct sources are approximate with respect to people, see [detection limits](../detection-limits.md).
- A minimum group size hides an individual among others. It does not protect against the conclusion that every member of a group did the same thing.
- The count of distinct sources in the default output is not subject to a minimum. In a very small network it can point to individuals. This is documented in [docs/privacy.md](../privacy.md).
- While a run lasts, the raw identifiers and the key are in the memory of the process.

## Alternatives considered

- **A plain hash without a key.** Rejected. The space of IPv4 addresses is small enough to hash completely, so a plain hash can be reversed by trying every address.
- **A stored key.** Rejected. It would make sources linkable across runs, which is the first step towards a profile.
- **Dropping source identifiers entirely.** Rejected. Distinct sources could no longer be counted.
- **Network range size as group size.** Rejected. A large range with two active devices would pass the threshold.
- **Suppressing small groups without merging.** Rejected. Their events would disappear from the breakdown, and their figures could still be computed from the totals.
- **Adding random noise to counts.** Rejected. It breaks determinism and is hard to explain to the report's readers.
