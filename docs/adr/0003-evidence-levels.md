# 0003: Evidence levels

- Status: Proposed
- Date: 2026-11-27

## Context

A DNS lookup, an established connection and a connection with a recorded byte count are very different pieces of evidence. A report that presents them alike invites conclusions the logs do not support. The readers of a report, among them auditors and employee representatives, need to see at a glance how far each statement goes.

## Decision

Every finding carries one of three evidence levels: `hint`, `connection` or `volume`. Their meaning is described in [docs/evidence-levels.md](../evidence-levels.md). The rules:

1. **DNS events yield at most `hint`.** A lookup shows that a name was asked for, not that anything was reached.
2. **Refused requests yield at most `hint`.** A request that the proxy or firewall rejected, for example a Squid line with `TCP_DENIED` or a 407 response, shows an attempt. The service was not reached through that request, so it is not a `connection`.
3. **`volume` requires bytes from the log source.** Nothing is estimated or derived.
4. **Missing is not zero.** A byte count that the source does not record is reported as not recorded. Squid's native access log records the bytes delivered to the client only; for such a source there is no upload volume, and the report says so instead of showing zero.
5. **The level of a finding is the highest level among its events.** The finding also states the number of events per level.
6. **`volume` means that bytes are documented, not that there were many.** There is no threshold.
7. **Levels are not judgements.** Whether a service is approved comes from the policy file and is reported separately.
8. **Wording follows the evidence.** Findings speak of observed connections and upload volume and avoid words that assert an outcome.

## Consequences

- Networks with an authenticating proxy produce a refused request before many successful ones. Those count as hints and do not inflate the number of connections.
- A finding at `volume` may rest on a single event. The count per level keeps that visible.
- Every parser has to state which kind of event a line is and which byte counts its format provides. A format that cannot say is limited to what it can show.

## Alternatives considered

- **A numeric risk score.** Rejected. It suggests a judgement that the data cannot carry, and it invites tuning.
- **Two levels (seen, not seen).** Rejected. It puts a DNS lookup on a level with a recorded transfer.
- **Treating refused requests as connections.** Rejected. The log itself says that the request did not get through.
- **A fourth level for refused requests.** Not chosen. In terms of evidence, an attempt that was refused shows the same as a lookup: something tried.
