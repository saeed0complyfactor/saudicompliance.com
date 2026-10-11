# saudicompliance.com

Bilingual (English/Arabic) static site for Saudi Compliance, a ComplyFactor company.

- `python build.py` regenerates `site/` from `content_en.py`, `content_ar.py`, `pages_<lang>_*.py` and `content/insights/<lang>/*.md`.
- Pushing changes under `site/` to `main` deploys to GitHub Pages (`.github/workflows/pages.yml`).
- `site/CNAME` holds `saudicompliance.com`. DNS at the registrar (GoDaddy):
  - `A` records for `@`: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
  - `CNAME` for `www`: saeed0complyfactor.github.io
- Switches (contact details, analytics, placeholders) are at the top of `build.py`.
- Image credits: `CREDITS.md`.
