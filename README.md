# SetupMastery - Static Site (Astro) for Home Office & Productivity Gear

This repository is a ready-to-deploy static site skeleton for a faceless affiliate site (Amazon-focused).

What’s included:
- Astro + Tailwind-ready skeleton (minimal dark theme)
- Example pages and layout
- 10 full medium-depth SEO article Markdown files (examples)
- 90 article outlines (ready to expand)
- article_generator.py — create articles from a CSV
- GitHub Actions workflow template for Cloudflare Pages

Quick deployment:
1. Create a GitHub repo and push this folder to `main`.
2. In Cloudflare Pages, create a new project, connect to the GitHub repo.
3. Build command: `npm run build`
4. Build output directory: `./dist`
5. If you use the Actions deploy, add secrets: `CF_API_TOKEN` and `CF_ACCOUNT_ID`.

Filling affiliate links:
- Replace all `[[AFFILIATE_LINK]]` placeholders with real Amazon Associates links or use automation to fetch ASINs from a sheet.

Generate more content:
- Fill a CSV with columns: `slug,title,content,tags`
- Run: `python article_generator.py articles.csv`

Notes:
- This is a minimal skeleton. Customize design, fonts, or add analytics/email later.
