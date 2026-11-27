# Startauftrag für Codex

Diesen Text als erste Nachricht in Codex einfügen, im frisch angelegten Repo.

---

Lies zuerst `AGENTS.md` und `docs/REPO_STRUCTURE.md`. Halte dich an beide. Du schreibst ausschließlich in `brand/`.

Wir starten LogAI: ein offenes Kommandozeilen-Werkzeug, das Log-Exporte lokal auswertet und zeigt, welche KI-Dienste aus einem Netz erreicht wurden. Du baust das Corporate Design und alle Assets als einzelne Dateien. Den Code schreibt Claude Code parallel; eure Schnittstelle sind `brand/tokens/tokens.json` und der Berichtsentwurf in `brand/templates/report/`.

Arbeite in zwei Meilensteinen. **Nach Meilenstein 1 hältst du an und wartest auf meine Auswahl.**

## Meilenstein 1: drei Richtungen zur Auswahl

Ein Pull Request `design/brand-directions`.

Entwickle drei klar unterschiedliche Gestaltungsrichtungen. Jede besteht aus:

- Bildmarke als SVG, die auch bei 16 Pixeln und einfarbig erkennbar bleibt und ohne den Namen funktioniert
- Wortmarke "LogAI" als SVG, Text in Pfade umgewandelt
- Farbpalette für hellen und dunklen Modus, mit geprüften Kontrastwerten
- Schriftvorschlag: eine Textschrift und eine Festbreitenschrift, beide frei lizenziert
- drei Beispiel-Icons im späteren Stil
- einem Satz, warum die Richtung zu "Beleg statt Behauptung, ruhig und genau, offen" passt

Ablage unter `brand/directions/a/`, `b/`, `c/`. Dazu `brand/preview/index.html`: eine eigenständige Seite, die alle drei Richtungen nebeneinander zeigt, hell und dunkel, in den Größen 16, 32, 64 und 256 Pixel. Die Seite lädt nichts aus dem Netz.

Beschreibe im Pull Request je Richtung in drei Sätzen Idee, Stärke und Schwäche, und nenne deine Empfehlung.

## Meilenstein 2: Ausarbeitung der gewählten Richtung

Ein Pull Request `design/brand-foundation`, nachdem ich gewählt habe.

**Logo** in `brand/logo/`
- `logai-mark`, `logai-wordmark`, `logai-logo` (Kombination), jeweils `-light`, `-dark`, `-mono`
- Schutzraum und Mindestgröße im Leitfaden dokumentiert

**Favicon** in `brand/favicon/`
- `favicon.svg` sowie Rasterexporte in 16, 32, 180 und 512 Pixeln

**Icons** in `brand/icons/`, eine Datei je Icon, 24er Raster, einheitliche Strichstärke, `currentColor`
- Quellen: `source-dns`, `source-proxy`, `source-firewall`, `source-file`
- Beweisstufen: `evidence-hint`, `evidence-connection`, `evidence-volume`; durch Form unterscheidbar, nicht nur durch Farbe
- Richtlinienstatus: `status-sanctioned`, `status-unsanctioned`, `status-unlisted`
- Sonstige: `catalog`, `service`, `report`, `export`, `pseudonymized`, `offline`, `limit`, `review-pending`

**Tokens** in `brand/tokens/`
- `tokens.json` als Quelle: Farben (hell, dunkel, semantisch für Beweisstufen und Status), Schriftfamilien und Größenskala, Abstände, Radien, Linienstärken
- `tokens.css` mit denselben Werten als Custom Properties

**Schriften** in `brand/fonts/`
- `woff2`-Dateien mit Lizenztext. Kannst du sie nicht beschaffen, nenne Schrift, Version und Bezugsquelle in `brand/TODO.md`.

**Vorschaubilder** in `brand/social/`
- GitHub-Vorschau 1280×640 und Link-Vorschau 1200×630, als SVG und PNG

**Berichtsentwurf** in `brand/templates/report/`
- `report.html` und `report.css`, statisch, mit erfundenen Beispieldaten und `.test`-Domains
- Abschnitte: Zusammenfassung, Befunde je Dienst mit Beweisstufe und Status, Erkennungsgrenzen, Katalogstand, Eingabestatistik
- Lesbar am Bildschirm in hell und dunkel, sauber druckbar auf A4, ohne JavaScript
- Der Abschnitt "Erkennungsgrenzen" ist gleichwertig gestaltet, nicht als Kleingedrucktes

**Leitfaden**
- `brand/README.md`: Markenkern, Logo-Regeln mit Beispielen für richtig und falsch, Farben, Typografie, Icon-Regeln, Tonalität der Texte (sachlich, keine Alarmwörter)
- `brand/TRADEMARK.md`: Name und Logo sind nicht Teil der Apache-Lizenz; was Dritte dürfen und was nicht
- `brand/snippets/readme-header.md`: Kopfbereich für das README mit Logo für hellen und dunklen Modus

**Übersicht**
- `brand/preview/index.html` aktualisieren: alle finalen Assets, Tokens als Farbfelder, Icons mit Namen, Link zum Berichtsentwurf

## Nicht Teil dieses Auftrags

Weboberfläche, Dashboard, Landingpage, Animationen, Präsentationsvorlagen, Merchandise. Notiere Ideen in `brand/TODO.md`.

## Am Ende jedes Meilensteins

Schreib mir kurz: was fertig ist, was fehlt und warum, welche fremden Bestandteile mit welcher Lizenz enthalten sind und welche Entscheidung du von mir brauchst.
