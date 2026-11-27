# LogAI – Repo-Struktur und Zuständigkeiten

Stand: 27. November 2026. Dieses Dokument legt fest, was wo liegt und wer es anfasst.

## Leitentscheidungen

| Thema | Entscheidung | Begründung |
| --- | --- | --- |
| Erstes Produkt | Kommandozeilen-Werkzeug `logai scan`, das Log-Exporte lokal auswertet und einen Bericht schreibt | Audit zuerst, kein Dashboard, keine Datenbank, kein Server |
| Sprache | Python 3.12+, verwaltet mit `uv` | Ein Toolchain, wenige Abhängigkeiten |
| Laufzeit | Kein Netzwerkzugriff, nie | Kern des Versprechens; wird im Test erzwungen |
| Katalog | Eine YAML-Datei je KI-Dienst, geprüft gegen ein JSON-Schema | Reviewbar per Pull Request, offline nutzbar |
| Bericht | Eigenständige HTML-Datei plus JSON und CSV | Offline lesbar, druckbar, maschinenlesbar |
| Lizenz Code | Apache-2.0 | Partner und Hersteller können es einsetzen |
| Lizenz Katalog | CC BY-SA 4.0 (offene Entscheidung, siehe unten) | Ableitungen bleiben offen |
| Marke | Name und Logo sind nicht Teil der Code-Lizenz | Schutz der Marke trotz offenem Code |
| Sprache im Repo | Code, Kommentare, Commits und öffentliche Doku auf Englisch; README zweisprachig | Internationale Beiträge möglich |

## Verzeichnisbaum

```
logai/
├── README.md                     Claude Code
├── LICENSE                       Apache-2.0
├── NOTICE                        Claude Code
├── CLAUDE.md                     Daueranweisung für Claude Code
├── AGENTS.md                     Daueranweisung für Codex
├── CONTRIBUTING.md               Claude Code (inkl. DCO-Sign-off)
├── SECURITY.md                   Claude Code (Meldeweg für Schwachstellen)
├── CODE_OF_CONDUCT.md            Claude Code
├── CHANGELOG.md                  Claude Code
├── pyproject.toml                Claude Code
├── uv.lock                       Claude Code
├── .editorconfig  .gitignore  .gitattributes  .pre-commit-config.yaml
│
├── .github/
│   ├── workflows/
│   │   ├── ci.yml                Lint, Typen, Tests, Katalog-Validierung, pip-audit, SBOM
│   │   └── release.yml           später: signierte Releases
│   ├── ISSUE_TEMPLATE/           bug, catalog-entry, parser-request
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── CODEOWNERS
│   └── dependabot.yml
│
├── src/logai_scan/               Claude Code
│   ├── cli.py                    Einstiegspunkt `logai`
│   ├── ingest/                   Dateiannahme, Größen- und Entpack-Grenzen
│   ├── parsers/                  ein Modul je Logquelle + base.py + registry.py
│   ├── model/                    Ereignis, Befund, Beweisstufe
│   ├── privacy/                  Pseudonymisierung, Aggregation, Mindestgruppengröße
│   ├── catalog/                  Laden, Schema-Prüfung, Abgleich
│   ├── policy/                   Freigabeliste des Kunden
│   ├── analysis/                 Aggregation mit Polars
│   └── report/
│       ├── render.py
│       └── templates/            Jinja-Vorlagen; Design kommt aus brand/
│
├── catalog/                      Claude Code legt Struktur an, Inhalte brauchen menschliches Review
│   ├── schema/service.schema.json
│   ├── services/                 eine YAML-Datei je Dienst
│   ├── LICENSE                   Datenlizenz
│   └── README.md                 Regeln für Einträge und Quellen
│
├── brand/                        Codex, ausschließlich
│   ├── README.md                 Markenleitfaden
│   ├── TRADEMARK.md              Nutzungsregeln für Name und Logo
│   ├── logo/                     Bildmarke, Wortmarke, Kombination; hell, dunkel, einfarbig
│   ├── icons/                    eine SVG-Datei je Icon
│   ├── favicon/
│   ├── tokens/                   tokens.json (Quelle) und tokens.css (abgeleitet)
│   ├── fonts/                    selbst gehostete Schriften mit Lizenzdateien
│   ├── social/                   Vorschaubilder für GitHub und Links
│   ├── templates/report/         statischer Entwurf des Audit-Berichts (HTML und CSS)
│   └── preview/index.html        Übersichtsseite aller Assets
│
├── docs/                         Claude Code
│   ├── REPO_STRUCTURE.md         dieses Dokument
│   ├── architecture.md
│   ├── detection-limits.md       was Logs zeigen und was nicht
│   ├── evidence-levels.md        Hinweis, Beleg, Volumen
│   ├── privacy.md                für Datenschutz und Betriebsrat
│   ├── threat-model.md
│   ├── adr/                      Architekturentscheidungen, nummeriert
│   └── kickoff/                  die beiden Startaufträge
│
├── tests/                        Claude Code
│   ├── unit/
│   ├── property/                 Hypothesis-Tests für Parser
│   ├── golden/                   erwartete Berichte
│   └── fixtures/                 nur synthetische Logs
│
└── scripts/                      Hilfsskripte, z. B. Katalog prüfen
```

## Wer fasst was an

| Bereich | Claude Code | Codex |
| --- | --- | --- |
| `src/`, `tests/`, `catalog/`, `docs/`, `.github/`, Root-Dateien | schreibt | liest nur |
| `brand/` | liest nur | schreibt |
| `src/logai_scan/report/templates/` | schreibt, übernimmt den Entwurf aus `brand/templates/report/` | liest nur |
| `README.md` | schreibt | liefert Kopfbereich als `brand/snippets/readme-header.md` |

Die Schnittstelle zwischen beiden sind zwei Dinge: `brand/tokens/tokens.json` und der statische Berichtsentwurf in `brand/templates/report/`.

## Arbeitsweise

- `main` ist geschützt. Jede Änderung kommt per Pull Request, der Maintainer gibt frei.
- Branches: `feat/...`, `fix/...`, `docs/...` für Claude Code, `design/...` für Codex.
- Commits nach Conventional Commits, mit DCO-Sign-off.
- Im Pull Request steht, welcher Agent beteiligt war. Das ist Teil der Transparenz gegenüber Nutzern und Förderern.

## Offene Entscheidungen

1. **Name.** Salesforce betreibt eine Open-Source-Bibliothek namens LogAI für Log-Analyse; der PyPI-Name `logai` ist vergeben. Deshalb heißt das Python-Paket hier vorläufig `logai-scan`. Vor dem ersten öffentlichen Release: Namenskonflikt und Markenlage prüfen.
2. **Datenlizenz des Katalogs.** CC BY-SA 4.0 hält Ableitungen offen. Ein kuratierter Zusatzkatalog müsste getrennt vom Repo gepflegt werden.
