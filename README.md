# Empower Young Website Copy

A fully patched, offline-first static copy of the [Empower Young](https://supratimdeb48.wixsite.com/website-3) Wix website.

## Project Structure
- `index.html` — Homepage
- `about.html` — About Page (repaired team bios)
- `about-3.html` — Our Model
- `about-9.html` — Impact
- `get-involved.html` — Get Involved Page (repaired strip photos)
- `mentorship.html` — Mentorship Page (dynamic iframe portal)
- `mentorship_form.html` — Dynamic Mentorship application widget using EmailJS
- `images/` — Site assets folder
- `.agents/` — **Antigravity Customizations Root** containing rules and skills for coding assistants.

## Antigravity Project Configuration
This workspace is configured as an **Antigravity Project**. It contains a `.agents/` directory that stores context and rules so that future Google Antigravity AI agents can immediately align on project requirements:
- **Project Rules**: Located at [AGENTS.md](file:///Users/sarun/.gemini/antigravity/scratch/empower-young/.agents/AGENTS.md) (defines development constraints like offline integrity, overrides, and header layout).
- **Custom Skill**: Located at [empower-young-manager](file:///Users/sarun/.gemini/antigravity/scratch/empower-young/.agents/skills/empower_young_manager/SKILL.md) (allows future agents to run audits and check pages).

### Run Audits (via custom scripts):
- **Validate Image Assets**:
  ```bash
  python3 .agents/skills/empower_young_manager/scripts/audit_assets.py
  ```
- **Check Page Contents**:
  ```bash
  python3 .agents/skills/empower_young_manager/scripts/check_pages_content.py
  ```

## Getting Started

To run a hot-reloading dev server locally:

1. **Install Node.js Dependencies**:
   ```bash
   npm install
   ```

2. **Start the Dev Server**:
   ```bash
   npm run dev
   ```

3. Open `http://localhost:5173/` in your browser.

## Git Integration
To push changes to GitHub:
```bash
git init
git add .
git commit -m "Initial commit of static wix website project"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```
