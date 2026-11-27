# Startauftrag für Claude Code

Diesen Text als erste Nachricht in Claude Code einfügen, im frisch angelegten Repo.

---

Lies zuerst `CLAUDE.md` und `docs/REPO_STRUCTURE.md`. Halte dich an beide.

Wir starten LogAI: ein offenes Kommandozeilen-Werkzeug, das Log-Exporte lokal auswertet und zeigt, welche KI-Dienste aus einem Netz erreicht wurden. Das ist ein Nebenprojekt mit begrenzter Zeit. Halte den Umfang klein und die Qualität hoch.

**Bevor du Code schreibst:** Zeig mir einen Plan für die zwei Meilensteine unten, mit deinen offenen Fragen und den Abhängigkeiten, die du einführen willst. Warte auf mein OK.

## Meilenstein 0: Gerüst

Ein Pull Request `feat/scaffold`.

- `pyproject.toml` mit `uv`, `src`-Layout, Paket `logai_scan`, Distribution `logai-scan`, CLI-Befehl `logai`.
- Ruff, Pyright (strikt), Pytest, Hypothesis, pre-commit.
- Tests laufen mit gesperrten Sockets, damit Netzwerkzugriff sofort auffällt.
- GitHub Actions `ci.yml`: Lint, Typen, Tests auf Python 3.12 und 3.13, Katalog-Validierung, `pip-audit`, SBOM im CycloneDX-Format als Artefakt.
- Root-Dateien: `README.md` (englisch, mit deutschem Abschnitt), `NOTICE`, `CONTRIBUTING.md` mit DCO, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CHANGELOG.md`, `.editorconfig`, `.gitignore`, `.gitattributes`.
- `.github/`: Issue-Vorlagen (bug, catalog-entry, parser-request), PR-Vorlage mit Feld "beteiligte KI-Werkzeuge", `CODEOWNERS`, `dependabot.yml`.
- `docs/`: `architecture.md`, `detection-limits.md`, `evidence-levels.md`, `privacy.md`, `threat-model.md` als knappe erste Fassungen.
- ADRs: 0001 offline zur Laufzeit, 0002 Katalog als YAML mit Schema, 0003 Beweisstufen, 0004 Pseudonymisierung und Mindestgruppengröße.
- Leeres `brand/` nicht anlegen; das macht Codex.

Im README steht ehrlich, was das Werkzeug nicht erkennt: Privatkonto oder Firmenkonto, übertragene Inhalte, KI in freigegebener Software, lokale Modelle, Geräte außerhalb des Netzes.

## Meilenstein 1: erste durchgehende Strecke

Ein Pull Request `feat/first-scan`. Ziel ist dieser Aufruf:

```
logai scan beispiel.csv --format generic-csv --catalog catalog/ --policy policy.yaml --out bericht/
```

Er schreibt `findings.json`, `findings.csv` und `report.html`.

**Einlesen**
- Zwei Formate: `generic-csv` (Spalten per Option zuordenbar: Zeit, Quelle, Ziel-Host, Bytes gesendet, Bytes empfangen, Ereignistyp) und `squid` (natives access.log).
- Grenzen für Dateigröße, Zeilenlänge und Zeilenzahl, konfigurierbar, mit klarer Fehlermeldung.
- Fehlerhafte Zeilen zählen und im Bericht ausweisen, nicht stillschweigend verwerfen.

**Katalog**
- `catalog/schema/service.schema.json` und eine YAML-Datei je Dienst.
- Felder mindestens: `id`, `name`, `provider`, `category`, `endpoints[]` mit `pattern`, `match` (`exact` oder `suffix`), `kind` (`web`, `api`, `auth`, `cdn`), `sources[]`, `verified_at`; dazu `legal` (Sitz des Anbieters, Hosting-Regionen, Trainingsnutzung, Auftragsverarbeitung verfügbar) jeweils mit Quelle und dem Wert `unknown` als zulässiger Angabe; `review.status` (`unreviewed` oder `reviewed`).
- Lege 15 Dienste als Startbestand an. Für jeden Endpunkt brauchst du eine nachprüfbare Quelle aus der Dokumentation des Anbieters. Hast du keine, trägst du den Endpunkt nicht ein. Alle Einträge starten als `unreviewed`; ich prüfe sie selbst.
- Abgleich über registrierbare Domain und Suffix, mit einer mitgelieferten Public-Suffix-Liste. Nichts nachladen.

**Befunde**
- Je Dienst: Beweisstufe (`hint`, `connection`, `volume`), Anzahl Ereignisse, Zeitraum, Bytes gesendet und empfangen falls vorhanden, Anzahl unterschiedlicher pseudonymisierter Quellen, Status laut Richtlinie (`sanctioned`, `unsanctioned`, `unlisted`).
- DNS-Ereignisse ergeben höchstens `hint`. Bytes ergeben `volume` nur, wenn die Quelle sie liefert.

**Datenschutz**
- Quellkennungen sofort beim Einlesen mit HMAC-SHA256 pseudonymisieren. Der Schlüssel wird je Lauf zufällig erzeugt und nicht gespeichert.
- Standardausgabe enthält keine einzelne Quelle. Optionale Auswertung nach Gruppen über eine Zuordnungsdatei (Netzbereich zu Gruppenname), mit Mindestgruppengröße 5 als Voreinstellung; kleinere Gruppen werden zusammengefasst.

**Bericht**
- `report.html` als eine eigenständige Datei ohne externe Verweise. Vorerst schlicht; das Design kommt später aus `brand/templates/report/`.
- Abschnitte: Zusammenfassung, Befunde je Dienst mit Beweisstufe, Erkennungsgrenzen, Katalogstand, Eingabestatistik inklusive verworfener Zeilen.
- Gleiche Eingabe und gleicher Katalog ergeben byte-gleiche `findings.json`.

**Tests**
- Synthetische Fixtures für beide Formate, darunter bösartige Fälle: überlange Zeilen, Steuerzeichen, Formel-Präfixe, HTML in Hostnamen, kaputte Kodierung.
- Property-Tests für die Parser: kein Absturz, keine Ausgabe ohne Kodierung.
- Golden-Test für `findings.json` und einen Snapshot für `report.html`.

## Nicht Teil dieses Auftrags

Weitere Logformate, Signatur des Katalogs, Agenten-Inventar, Weboberfläche, Datenbank, Container-Images, Mandantenfähigkeit. Notiere Ideen dazu als Issues, baue sie nicht.

## Am Ende jedes Meilensteins

Schreib mir kurz: was fertig ist, was du bewusst weggelassen hast, wo ich als Mensch prüfen muss (besonders Parser, Pseudonymisierung, Katalogeinträge) und welche Entscheidung du von mir brauchst.
