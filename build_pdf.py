"""
Render the checklist HTML template to PDF.

Usage:
    uv run build_pdf.py
"""

import os
import sys
from pathlib import Path

# WeasyPrint needs Pango/GObject which Homebrew installs to /opt/homebrew/lib.
# uv's isolated Python doesn't pick this up automatically, so we add it here.
HOMEBREW_LIB = "/opt/homebrew/lib"
if sys.platform == "darwin" and Path(HOMEBREW_LIB).exists():
    os.environ["DYLD_LIBRARY_PATH"] = (
        HOMEBREW_LIB + ":" + os.environ.get("DYLD_LIBRARY_PATH", "")
    )

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS

ROOT = Path(__file__).parent
TEMPLATE_DIR = ROOT / "app" / "templates"
OUTPUT = ROOT / "app" / "static" / "downloads" / "checkliste-direktvermarktung.pdf"


def build():
    env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))
    html_string = env.get_template("checklist_pdf.html").render()

    HTML(string=html_string, base_url=str(ROOT)).write_pdf(
        target=str(OUTPUT),
    )
    print(f"PDF written to {OUTPUT}")


if __name__ == "__main__":
    build()
