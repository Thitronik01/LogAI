# LogAI – Anweisungen für Claude Code

Du arbeitest am Code von LogAI. Für Marke und Design ist Codex zuständig (siehe `AGENTS.md`).

## Was LogAI ist

Ein offenes Kommandozeilen-Werkzeug, das vorhandene Log-Exporte (DNS, Proxy, Firewall) lokal auswertet und zeigt, welche KI-Dienste aus einem Netz erreicht wurden. Ergebnis ist ein belegter Bericht für Informationssicherheit, Datenschutz und Prüfer.

LogAI läuft vollständig offline, schreibt keine Personenprofile und behauptet nichts, was Logs nicht belegen.

## Was LogAI nicht ist

Kein Dashboard, kein Server, keine Datenbank, kein Agent auf Endgeräten, keine Browser-Erweiterung, kein Blockieren, keine TLS-Inspektion, keine lernende Risikobewertung, keine Telemetrie. Schlage nichts davon vor, solange es nicht ausdrücklich beauftragt ist.

## Harte Regeln

1. **Kein Netzwerk zur Laufzeit.** Kein Import, der beim Start etwas nachlädt. Tests laufen mit gesperrten Sockets.
2. **Logs sind feindliche Eingaben.** Jedes Feld kann vom Angreifer stammen. Größen-, Zeilen- und Zeitgrenzen bei jedem Import. Kein `eval`, kein `pickle`, YAML nur mit `safe_load`.
3. **Ausgaben kodieren.** HTML mit Autoescape. CSV-Exporte gegen Formel-Injektion schützen (führende `=`, `+`, `-`, `@`, Tab, Wagenrücklauf).
4. **Datenminimierung als Voreinstellung.** Quell-IP und Nutzerkennung werden beim Einlesen pseudonymisiert. Standardausgabe ist je Dienst aggregiert. Auswertung nach Gruppen nur mit Mindestgruppengröße.
5. **Keine echten Logs im Repo.** Testdaten sind synthetisch und als solche erkennbar (`.test`-Domains, dokumentierte Beispiel-IP-Bereiche).
6. **Ehrliche Sprache.** Der Code und der Bericht sprechen von "beobachteten Verbindungen" und "Upload-Volumen". Die Wörter "Datenabfluss", "Leak" oder "Verstoß" kommen in Befunden nicht vor.
7. **Jeder Befund trägt eine Beweisstufe:** `hint` (DNS-Auflösung), `connection` (Verbindung mit SNI oder URL), `volume` (übertragene Bytes). Details in `docs/evidence-levels.md`.
8. **Katalogeinträge brauchen Quelle und Datum.** Erfinde keine Domains. Ein Eintrag ohne nachprüfbare Quelle bekommt `review.status: unreviewed` und wird im Bericht so gekennzeichnet.
9. **Neue Abhängigkeiten begründen.** Jede zusätzliche Bibliothek steht mit Zweck und Alternative im Pull Request. Standardbibliothek zuerst.
10. **`brand/` nicht verändern.** Du liest dort Tokens und den Berichtsentwurf. Änderungswünsche gehen als Issue an Codex.

## Technik

- Python 3.12+, `uv`, `src`-Layout, Paketname `logai_scan`, Distribution `logai-scan`, CLI-Befehl `logai`.
- Den Projektnamen nie verstreut hartkodieren: eine Konstante, ein Ort. Der Name kann sich noch ändern.
- Polars für Auswertung, Jinja2 für Berichte, `jsonschema` für den Katalog, `argparse` für die CLI.
- Ruff für Format und Lint, Pyright im strikten Modus, Pytest, Hypothesis für Parser.
- Deterministisch: gleiche Eingabe, gleicher Katalogstand, gleicher Bericht. Keine Zeitstempel im Bericht außer dem ausgewiesenen Laufzeitpunkt.

## Arbeitsweise

- Zeig vor größeren Änderungen einen Plan und warte auf Freigabe.
- Ein Pull Request, ein Thema. Branch `feat/...`, `fix/...` oder `docs/...`.
- Conventional Commits mit Sign-off (`git commit -s`).
- Zu jeder Verhaltensänderung gehört ein Test. Parser bekommen zusätzlich Property-Tests.
- Architekturentscheidungen als kurze ADR in `docs/adr/`.
- Code, Kommentare, Commits und öffentliche Doku auf Englisch. Mit dem Maintainer sprichst du Deutsch.
- Wenn etwas unklar ist oder eine Regel einer Aufgabe widerspricht: nachfragen statt raten.

## Befehle

```
uv sync                      Abhängigkeiten installieren
uv run ruff format .         formatieren
uv run ruff check .          Lint
uv run pyright               Typprüfung
uv run pytest                Tests
uv run python scripts/validate_catalog.py
```

## Sicherheitskritische Stellen

Parser, Dateiannahme, Pseudonymisierung, Berichtsausgabe und später die Signaturprüfung des Katalogs. Änderungen dort im Pull Request ausdrücklich markieren, damit ein Mensch mit Security-Erfahrung sie prüft.
