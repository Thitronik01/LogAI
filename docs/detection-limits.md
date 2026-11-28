# Detection limits

What logs can show and what they cannot. A report is only as strong as the logs it was given. This page belongs next to every finding, and the report repeats it in a section of its own.

## What a log shows

Depending on its source, a log line records that a device asked for a name (DNS), that a connection to a host was requested or established (proxy, firewall), and sometimes how many bytes were moved. Nothing more.

## About the use itself

- **Private or company account.** Both reach the same hosts. A log cannot tell them apart.
- **Content.** No prompts, no files, no answers. At most the number of bytes.
- **Who or what acted.** A connection can come from a person typing a prompt, from a browser tab left open, from an application that calls an API, from a widget embedded in an unrelated website, or from a browser that preloads a link.
- **Success.** A request is not a completed conversation. A request that the proxy or firewall refused shows an attempt and is reported as a `hint`.

## What stays invisible

- **AI inside approved software.** An assistant built into an office suite or another approved product talks to that product's hosts.
- **Local models.** A model on a workstation or an internal server causes no connection to an AI service.
- **Devices outside the network.** Phones on mobile data, home offices without VPN, private devices.
- **Traffic that bypasses the logged systems.** Encrypted DNS to an external resolver does not appear in the local DNS log. VPNs, tunnels and anonymising proxies hide the destination.
- **Services that are not in the catalog.** New services appear constantly. A service that is not listed is not found.
- **Endpoints that are not in the catalog.** Entries rest on what providers document. Undocumented hosts are missing, and providers change their hosts.
- **Hosts shared with unrelated products.** Some services are reached through host names that also serve other things, such as content delivery networks or generic cloud endpoints. Such hosts cannot be assigned to a service and are left out.
- **Logs without host names.** A log that records only destination IP addresses cannot be assigned to services. Addresses of cloud providers are shared and change.

## About the numbers

- **Sources are not people.** Address translation, changing leases, shared machines, terminal servers and several devices per person all distort the count of distinct sources.
- **Events are not uses.** DNS caching hides repeated lookups. One page view can produce dozens of proxy lines. A single long-lived connection may be one line.
- **Bytes depend on the source.** They are reported only if the log source records them, and they mean what that source counts. A source may record one direction only. Squid's native access log, for example, records the bytes delivered to the client and no upload volume. A direction that is not recorded is reported as not recorded, never as zero.
- **The time range is that of the export.** A gap in the export is a gap in the report. Times are as correct as the clock and time zone of the system that wrote the log.
- **Rejected lines contribute nothing.** Lines that could not be read are counted and shown, but whatever they recorded is missing from the findings.

## About manipulation

- **Events can be planted.** Anyone on the network can cause a DNS lookup or a connection attempt for any name. An event is not proof of intent. This is one reason why DNS alone never yields more than a `hint`.
- **No finding is not proof of no use.** Everything listed under "What stays invisible" applies.
