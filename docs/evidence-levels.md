# Evidence levels

Every finding states how strong its evidence is. There are three levels. They describe what the logs show, not how serious something is. The decision is recorded in [ADR 0003](adr/0003-evidence-levels.md).

| Level | What was observed | What it supports | What it does not support |
| --- | --- | --- | --- |
| `hint` | A DNS lookup for a catalogued host, or a connection attempt that the proxy or firewall refused. | A device on the network tried to reach the service. | That the service was reached or used. |
| `connection` | A connection to a catalogued host, identified by its host name (SNI, CONNECT target or URL). | The service's host was reached from the network. | That somebody logged in, what was done, or how much data was moved. |
| `volume` | A connection for which the log source records transferred bytes. | The host was reached, and this number of bytes was recorded. | What the bytes contained. A large number is not a file upload, and a small one is not harmless. |

## Rules

1. DNS events yield at most `hint`.
2. Requests that the proxy or firewall refused yield at most `hint`.
3. `volume` requires bytes from the log source. Nothing is estimated. A direction that the source does not record is reported as not recorded, never as zero.
4. The level of a finding is the highest level among its events. The finding also lists the number of events per level, so that one `volume` event among a thousand hints cannot be mistaken for a thousand.
5. The level says nothing about whether the use was permitted. That comes from the organisation's policy file and is reported separately as `sanctioned`, `unsanctioned` or `unlisted`.

## Wording

Findings speak of "observed connections" and "upload volume". They do not use words that assert an outcome or a judgement that logs cannot support: "leak", "data exfiltration", "violation", or in German "Datenabfluss", "Leak", "Verstoß".
