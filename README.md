<picture>
  <source media="(prefers-color-scheme: dark)" srcset="brand/logo/logai-logo-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="brand/logo/logai-logo-light.svg">
  <img src="brand/logo/logai-logo-light.svg" alt="LogAI" width="238" height="72">
</picture>

# LogAI

Local analysis of DNS, proxy and firewall exports for evidence of AI service activity.

LogAI is an open-source command-line tool. It analyses existing log exports from DNS resolvers, proxies and firewalls on the machine where it runs, and shows which AI services were reached from a network. The result is a report in which every statement is backed by the logs, written for information security officers, data protection officers and auditors.

> **Status: pre-alpha.** This repository holds the project scaffold. There is no scan command yet; the first end-to-end scan is the next milestone.

[Deutsche Kurzfassung](#deutsch)

## Principles

- **Offline.** The tool never accesses the network. The test suite runs with sockets blocked to enforce that ([ADR 0001](docs/adr/0001-offline-at-runtime.md)).
- **Evidence instead of claims.** Every finding carries an evidence level, `hint`, `connection` or `volume`, that says what the logs actually show ([evidence levels](docs/evidence-levels.md)).
- **No personal profiles.** Source addresses and user names are pseudonymised as they are read, and the output is aggregated per service ([privacy](docs/privacy.md)).
- **Logs are hostile input.** Any field in a log may have been written by an attacker ([threat model](docs/threat-model.md)).

## What LogAI cannot detect

Logs show that a connection took place. They do not show what it meant. LogAI cannot tell you:

- **Whether a private or a company account was used.** Both reach the same hosts.
- **What was transmitted.** No prompts, no files, no content. At most the number of bytes, and only if the log source records it.
- **AI inside approved software.** An assistant built into an office suite or another approved product talks to that product's hosts and cannot be told apart from the product's ordinary traffic.
- **Local models.** A model running on a workstation or an internal server causes no connection to an AI service.
- **Devices outside the network.** Phones on mobile data, home offices without VPN and everything else that does not pass the logged resolver, proxy or firewall stay invisible.

LogAI also knows only the services in its catalog. A service that is not listed is not found. The full list of limits is in [docs/detection-limits.md](docs/detection-limits.md).

## What LogAI is not

Not a dashboard, a server, a database, an agent on end devices or a browser extension. It does not block anything, does not inspect TLS, does not compute risk scores and sends no telemetry.

## Development

Requires [uv](https://docs.astral.sh/uv/). Python 3.12 or newer is installed by uv if it is missing.

```
uv sync                                     install dependencies
uv run pre-commit install                   enable the checks on commit and push
uv run ruff format .                        format
uv run ruff check .                         lint
uv run pyright                              type check
uv run pytest                               tests, with network access blocked
uv run python scripts/validate_catalog.py   validate the catalog
```

How to contribute: [CONTRIBUTING.md](CONTRIBUTING.md). How to report a vulnerability: [SECURITY.md](SECURITY.md).

## Documentation

- [Architecture](docs/architecture.md)
- [Detection limits](docs/detection-limits.md)
- [Evidence levels](docs/evidence-levels.md)
- [Privacy](docs/privacy.md)
- [Threat model](docs/threat-model.md)
- [Architecture decisions](docs/adr/README.md)
- [Repository layout and responsibilities](docs/REPO_STRUCTURE.md) (German)
- Instructions for coding agents: [CLAUDE.md](CLAUDE.md) and [AGENTS.md](AGENTS.md) (German)

## Licence and name

Code: Apache-2.0, see [LICENSE](LICENSE) and [NOTICE](NOTICE). The project name and logo are not covered by the code licence; see [brand/TRADEMARK.md](brand/TRADEMARK.md).

The name is provisional; see the open decisions in [docs/REPO_STRUCTURE.md](docs/REPO_STRUCTURE.md).

## Deutsch

LogAI ist ein offenes Kommandozeilen-Werkzeug. Es wertet vorhandene Log-Exporte von DNS-Resolvern, Proxys und Firewalls lokal aus und zeigt, welche KI-Dienste aus einem Netz erreicht wurden. Das Ergebnis ist ein Bericht, in dem jede Aussage durch die Logs belegt ist, geschrieben für Informationssicherheit, Datenschutz und Prüfer.

**Stand: Pre-Alpha.** Dieses Repository enthält das Projektgerüst. Einen Scan-Befehl gibt es noch nicht; die erste durchgehende Auswertung ist der nächste Meilenstein.

### Grundsätze

- **Offline.** Das Werkzeug greift nie auf das Netz zu. Die Tests laufen mit gesperrten Sockets.
- **Beleg statt Behauptung.** Jeder Befund trägt eine Beweisstufe (`hint`, `connection`, `volume`), die sagt, was die Logs tatsächlich zeigen.
- **Keine Personenprofile.** Quelladressen und Nutzerkennungen werden beim Einlesen pseudonymisiert, die Ausgabe ist je Dienst zusammengefasst.
- **Logs sind feindliche Eingaben.** Jedes Feld eines Logs kann von einem Angreifer stammen.

### Was LogAI nicht erkennt

Logs zeigen, dass eine Verbindung stattgefunden hat. Sie zeigen nicht, was sie bedeutet. LogAI kann nicht sagen:

- **ob ein Privatkonto oder ein Firmenkonto benutzt wurde.** Beide erreichen dieselben Hosts.
- **was übertragen wurde.** Keine Eingaben, keine Dateien, keine Inhalte. Höchstens die Zahl der Bytes, und nur wenn die Logquelle sie aufzeichnet.
- **KI in freigegebener Software.** Ein Assistent in einem Office-Paket oder einem anderen freigegebenen Produkt spricht mit den Hosts dieses Produkts und ist vom gewöhnlichen Verkehr des Produkts nicht zu unterscheiden.
- **lokale Modelle.** Ein Modell auf einem Arbeitsplatzrechner oder einem internen Server erzeugt keine Verbindung zu einem KI-Dienst.
- **Geräte außerhalb des Netzes.** Telefone im Mobilfunknetz, Heimarbeitsplätze ohne VPN und alles andere, das nicht über den protokollierten Resolver, Proxy oder die Firewall läuft, bleiben unsichtbar.

LogAI kennt außerdem nur die Dienste in seinem Katalog. Ein Dienst, der dort fehlt, wird nicht gefunden. Die vollständige Liste der Grenzen steht in [docs/detection-limits.md](docs/detection-limits.md) (englisch).
