"""Regenerate the distributable CSS from tokens.json using the standard library."""

import json
from pathlib import Path


def properties(group, prefix):
    for name, value in group.items():
        path = f"{prefix}-{name}"
        if isinstance(value, dict):
            yield from properties(value, path)
        else:
            yield f"  {path}: {value};"


def aliases(palette, mode):
    return [f"  --logai-{name}: var(--logai-color-{mode}-{name});" for name in palette]


def stylesheet(tokens):
    colours = tokens["color"]
    if set(colours["light"]) != set(colours["dark"]):
        raise ValueError("Both palettes must define the same roles.")
    lines = ["/* Generated from tokens.json by generate.py. */", ":root {"]
    lines.extend(properties(tokens, "--logai"))
    lines.extend(aliases(colours["light"], "light"))
    lines += ["}", "", "@media screen and (prefers-color-scheme: dark) {", "  :root {"]
    lines.extend("  " + line for line in aliases(colours["dark"], "dark"))
    lines += ["  }", "}", ""]
    return "\n".join(lines)


if __name__ == "__main__":
    directory = Path(__file__).resolve().parent
    source = json.loads((directory / "tokens.json").read_text(encoding="utf-8"))
    (directory / "tokens.css").write_text(stylesheet(source), encoding="utf-8", newline="\n")
