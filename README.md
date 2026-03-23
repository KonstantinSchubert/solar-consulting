# PV Direktvermarktung Beratung – MVP Website

FastAPI + Jinja2 + Tailwind CSS website for an independent PV direct marketing consulting service.

## Setup

```bash
uv run uvicorn app.main:app --reload
```

Open: http://localhost:8000

## Structure

```
app/
  main.py                        # FastAPI routes
  templates/
    base.html                    # Shared layout (nav, footer)
    index.html                   # Homepage (all sections)
    impressum.html               # Impressum (fill in your data)
    datenschutz.html             # Datenschutzerklärung (fill in your data)
    danke.html                   # Thank-you page after form submit
  static/
    css/custom.css               # Small custom CSS additions
    js/analytics.js              # Event tracking (console + extendable)
    downloads/
      checkliste-direktvermarktung.pdf  # Replace with real PDF
```

## Pages

| URL | Description |
|-----|-------------|
| `/` | Homepage with all sections |
| `/impressum` | Impressum (placeholder – fill in) |
| `/datenschutz` | Datenschutzerklärung (placeholder – fill in) |
| `/danke` | Thank-you page shown after contact form submit |
| `POST /kontakt` | Contact form handler (logs to console, redirects to /danke) |

## Before going live

1. **Impressum**: Fill in name, address, email, USt-ID in `app/templates/impressum.html`
2. **Datenschutz**: Fill in name, address, hosting provider, analytics info in `app/templates/datenschutz.html`
3. **PDF**: Replace `app/static/downloads/checkliste-direktvermarktung.pdf` with your real checklist
4. **Contact form email**: Add email sending in `app/main.py` (see TODO comment). Suggested: [Resend](https://resend.com) (`uv add resend`)
5. **Analytics**: Replace console logs in `app/static/js/analytics.js` with your analytics provider (Plausible, Fathom, GA4)

## Tracked events

- `hero_cta_click` – Hero section CTA button
- `checklist_cta_click` – Checklist download CTA
- `form_submit` – Contact form submitted
- `checklist_download` – PDF download on thank-you page
- `page_scroll_depth` – 25 / 50 / 75 / 100 % scroll milestones

## Deployment (Render / Railway)

**Render**: Create a Web Service, set start command:
```
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

**Railway**: Same start command. Add a `Procfile`:
```
web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```
