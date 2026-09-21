---
name: empower-young-manager
description: Manage, audit, and patch pages for the static Empower Young website. Includes asset validation and content checking.
---

# Empower Young Manager Skill

This skill allows you to validate assets, manage patches, and ensure offline-first compatibility of the static copy of the Empower Young website.

## Core Operations

### 1. Audit Website Assets
Runs a scan of all `<img src="...">` paths on the pages and tests if they load correctly (status 200).
- Script: `scripts/audit_assets.py`
- Command: `python3 .agents/skills/empower_young_manager/scripts/audit_assets.py`

### 2. Verify Page Content
Analyzes word counts and structures of elements inside the main content container (`#PAGES_CONTAINER`).
- Script: `scripts/check_pages_content.py`
- Command: `python3 .agents/skills/empower_young_manager/scripts/check_pages_content.py`

## Maintenance Details
- **Wix Animation Override**: When editing pages, ensure the custom `#local-static-overrides` style block remains in place. This CSS overrides wix scroll animations that freeze and hide layout blocks offline.
- **Iframe Form Integration**: The mentorship application is an iframe leading to `./mentorship_form.html`.
