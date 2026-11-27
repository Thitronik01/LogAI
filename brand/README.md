# Randbeleg · LogAI brand guide

A bracket in the margin points to one of two log lines. It expresses the promise of a LogAI report: a reader can follow an observation back to a source. The companion line keeps the mark recognisable at favicon size. The provisional name and the mark are separate assets.

[Asset library](preview/index.html) · [Sample audit report](templates/report/report.html) · [Use of the name and logo](TRADEMARK.md)

## Logo

![The Randbeleg mark and LogAI wordmark](logo/logai-logo-light.svg)

Use `logai-mark` for a compact identifier, `logai-wordmark` where the name stands alone, and `logai-logo` for the horizontal combination. The suffix names the **background** for the light and dark sets. The mono set uses one ink through `currentColor` and defaults to black as a standalone image. Choose the supplied dark asset for an external image on a dark surface.

| Asset | Minimum displayed size | Clear space on each side |
| --- | --- | --- |
| Mark | 16 × 16 CSS px | One quarter of the mark viewport width |
| Wordmark | 56 CSS px wide | One quarter of its displayed height |
| Combination | 96 CSS px wide | One quarter of the square mark in the combination |

Measure clear space from the SVG viewport to nearby text, rules or artwork. At a 32 px mark size, leave 8 px free on each side. The favicon has a fixed canvas with its own margin.

| Use | Correct example | Incorrect example |
| --- | --- | --- |
| Report heading | Render the supplied combination at 119 × 36 px on paper | Stretch the combination into a 119 × 24 px box |
| Dark report | Use `logai-logo-dark.svg` on the charcoal surface | Place the petrol light-mode mark on charcoal |
| Tight spaces | Use the standalone mark at 16 × 16 px | Squeeze the entire wordmark into a 16 px icon |
| Reproduction | Place the supplied one-ink artwork on plain stock | Add a shadow, redraw the bracket or close its opening |

## PNG downloads

The PNG pack includes the nine transparent logos, two surface variants of each of the eighteen icons, four favicons and both social images. Marks are 512 × 512 px, wordmarks are 2801 × 905 px and horizontal combinations are 1428 × 432 px. Icons are 192 × 192 px. The light and dark suffixes or folders identify the intended background. Evidence and policy icons use their respective palette roles. The archive also contains the image sheet and an AI-generated photographic cover study. [Download the PNG pack](exports/logai-randbeleg-png.zip) · [View the image sheet](preview/randbeleg-assets.png)

## Colour and typography

The base palette pairs paper `#FBF9F2`, ink `#292723` and petrol `#145C51`. The dark palette pairs charcoal `#202522`, warm white `#F3F0E7` and mint `#89D1C2`. Text contrast against the main surface is 14.15:1 in light mode and 13.66:1 in dark mode. Accent contrast is 7.44:1 and 8.87:1 respectively. Use the rule colour for decorative dividers. Evidence and policy labels each have a dedicated ink, a shape and a visible name. [Palette and type specimens](preview/index.html#tokens)

Use Source Serif 4 for titles, explanations and body copy. Use Source Code Pro for hostnames, byte counts, source references and token names. The wordmark uses Source Serif 4 outlines at weight 590. Both fonts ship as unmodified Latin WOFF2 subsets from Fontsource 5.3.1. The family names are followed by system fallbacks for glyphs outside those subsets.

| Font | Upstream version | Local licence |
| --- | --- | --- |
| [Source Serif 4](https://www.npmjs.com/package/@fontsource-variable/source-serif-4/v/5.3.1) | 4.004 | [SIL OFL 1.1](fonts/source-serif-4/ofl.txt) |
| [Source Code Pro](https://www.npmjs.com/package/@fontsource/source-code-pro/v/5.3.1) | 1.026 | [SIL OFL 1.1](fonts/source-code-pro/ofl.txt) |

## Icons

Draw on a 24 × 24 grid with a two-unit stroke, square line endings and aligned corners. Leave enough negative space to distinguish each sign in one ink. The evidence series progresses from a point in a bracket to a connection between brackets to a stack of lines. Policy uses a check, a cross and an empty box. The icons are original LogAI drawings. [Individual icon files](preview/index.html#icons)

Pair each semantic icon with its text label. Use an empty alt attribute next to an equivalent visible label. Inline SVG inherits the host text colour through `currentColor`. In an external image the SVG has its own colour context. The sample report uses monochrome images and labels in the corresponding semantic ink.

## Report voice

Name the source, the observed event, the observation window and the limit of the inference. Write “The resolver logged 12 lookups for this hostname.” A DNS event on its own supports a hint. A recorded connection carries a destination. A byte counter supplies volume and needs an explicit direction and unit. Report the applicable policy snapshot independently of the evidence level. Keep detection limits at the same heading and body size as findings.

## Integration

Use [tokens.json](tokens/tokens.json) as the source of design values. The hierarchy groups `color.light`, `color.dark`, `font`, `space`, `radius` and `stroke`. Numeric font weights are unitless. Other dimensional values carry CSS units. The CSS export joins path segments with hyphens after `--logai-`. For example, `color.light.evidence-hint` becomes `--logai-color-light-evidence-hint`. The shorter `--logai-evidence-hint` alias follows the screen colour scheme and resolves to the light palette in print. After editing JSON, run `python brand/tokens/generate.py` from the repository root and commit both files.

[report.html](templates/report/report.html) and [report.css](templates/report/report.css) are the reference for Claude’s Jinja renderer. Each service article contains a hostname, separate evidence and policy fields, an observation and a source reference. The example files open from disk with their sibling assets. When building the single-file product report, package the required styles, glyphs and artwork within the exported document. Keep the runtime offline and escape substituted text through the template engine.

The [README header snippet](snippets/readme-header.md) uses paths relative to the repository root. The [social artwork](preview/index.html#social) ships with outlined lettering so the exported images render independently of installed fonts.
