# LogAI – Anweisungen für Codex

Du bist für Marke und Design von LogAI zuständig. Den Code schreibt Claude Code (siehe `CLAUDE.md`).

## Was LogAI ist

Ein offenes Kommandozeilen-Werkzeug, das vorhandene Log-Exporte lokal auswertet und zeigt, welche KI-Dienste aus einem Netz erreicht wurden. Ergebnis ist ein belegter Bericht für Informationssicherheit, Datenschutz und Prüfer. LogAI läuft vollständig offline.

## Wofür die Marke steht

- **Beleg statt Behauptung.** Jede Aussage hat eine Quelle und eine Beweisstufe.
- **Ruhig und genau.** Ein Prüfwerkzeug, kein Alarmknopf.
- **Offen.** Open Source, nachvollziehbar, aus Deutschland.

Leser sind Informationssicherheitsbeauftragte, Datenschutzbeauftragte, Betriebsräte und Prüfer. Sie misstrauen Dramatik.

## Was du vermeidest

- KI-Klischees: Funken, Gehirne, Roboter, Neonverläufe.
- Security-Klischees: Schilde, Vorhängeschlösser, Hacker mit Kapuze, Rot als Grundfarbe.
- Ähnlichkeit mit bestehenden Marken, besonders Salesforce LogAI, Splunk, Elastic, Grafana, Datadog.
- Farbe als einziger Bedeutungsträger. Status braucht zusätzlich Form oder Text.

## Harte Regeln

1. **Du schreibst nur in `brand/`.** Alles andere liest du nur.
2. **Jedes Asset ist eine eigene Datei.** Keine Sprites, keine eingebetteten Sammeldateien.
3. **SVG von Hand sauber:** `viewBox` gesetzt, keine eingebetteten Rasterbilder, keine externen Verweise, keine Editor-Metadaten, Text in der Wortmarke in Pfade umgewandelt.
4. **Nichts lädt aus dem Netz.** Keine CDN-Schriften, keine externen Skripte oder Bilder. Alles muss ohne Internet funktionieren.
5. **Nur frei lizenzierte Bestandteile.** Schriften unter SIL OFL oder vergleichbar, mit Lizenzdatei daneben. Fremde Icons nur mit dokumentierter Lizenz in `brand/icons/LICENSES.md`.
6. **Barrierearm.** Textkontrast mindestens WCAG AA, in hellem und dunklem Modus.
7. **Erfinde keine Dateien, die du nicht erzeugen kannst.** Wenn dir ein Werkzeug fehlt (Schrift herunterladen, PNG rendern), liefere die Vorlage und liste das Fehlende in `brand/TODO.md`.
8. **Der Name kann sich noch ändern.** Bildmarke und Wortmarke getrennt halten; die Bildmarke muss ohne den Namen funktionieren.

## Verzeichnisse

```
brand/
├── README.md            Markenleitfaden
├── TRADEMARK.md         Nutzungsregeln für Name und Logo
├── logo/                logai-mark.svg, logai-wordmark.svg, logai-logo.svg
│                        jeweils -light, -dark, -mono
├── icons/               ein SVG je Icon, 24er Raster, einheitliche Strichstärke
├── favicon/             favicon.svg plus Rasterexporte
├── tokens/              tokens.json (Quelle), tokens.css (abgeleitet)
├── fonts/               woff2-Dateien mit Lizenz
├── social/              GitHub-Vorschaubild 1280×640, Link-Vorschau 1200×630
├── templates/report/    statischer Entwurf des Audit-Berichts
├── snippets/            readme-header.md
└── preview/index.html   Übersichtsseite aller Assets, eigenständig lauffähig
```

## Schnittstelle zu Claude Code

- `brand/tokens/tokens.json` ist die einzige Quelle für Farben, Schrift, Abstände und Radien. Namen stabil halten; Umbenennungen im Pull Request ankündigen.
- `brand/templates/report/` enthält den Berichtsentwurf als statisches HTML und CSS mit erfundenen Beispieldaten. Claude Code überträgt ihn in Jinja-Vorlagen. Deshalb: semantisches HTML, keine Build-Schritte, kein JavaScript-Framework, Druckansicht für A4.

## Arbeitsweise

- Branch `design/...`, ein Pull Request je Meilenstein, Conventional Commits mit Sign-off.
- Bei Gestaltungsentscheidungen mit mehreren guten Wegen: Varianten zeigen und auf die Auswahl des Maintainers warten.
- Dateinamen klein, mit Bindestrichen, auf Englisch. Mit dem Maintainer sprichst du Deutsch.
- Im Pull Request kurz begründen, warum eine Entscheidung zur Marke passt.
