#!/bin/bash
set -e

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  strommarktberatung.de — Deploy"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# ── 1. Build PDF ─────────────────────────────────────
echo "▶ Building checklist PDF..."
uv run build_pdf.py
echo "  ✓ PDF written to app/static/downloads/checkliste-direktvermarktung.pdf"
echo ""

# ── 2. Done ───────────────────────────────────────────
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  ✓ Build complete."
echo ""
echo "  To deploy strommarktberatung.de, push to GitHub:"
echo ""
echo "    git add -A && git commit -m \"your message\""
echo "    git push"
echo ""
echo "  Railway will deploy automatically on push."
echo "  Track progress: https://railway.app/dashboard"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
