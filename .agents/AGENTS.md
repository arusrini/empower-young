# Empower Young Website Project Rules

This workspace contains the offline-friendly, patched static copy of the Wix site for the Empower Young Foundation. When working in this workspace, follow these project-specific rules:

## Development Constraints
- **Offline Integrity**: All pages must load and function completely offline. Do not introduce remote CDNs or external APIs unless absolutely necessary.
- **Form Submissions**: The Mentorship portal relies on [mentorship_form.html](file:///Users/sarun/.gemini/antigravity/scratch/empower-young/mentorship_form.html) embedded as an iframe in [mentorship.html](file:///Users/sarun/.gemini/antigravity/scratch/empower-young/mentorship.html). Any edits to the form layout must be made inside `mentorship_form.html`.
- **Wix Animation Override**: Do not remove the `#local-static-overrides` style block from the page headers. If adding new elements, make sure they do not rely on Wix's Thunderbolt client-side scroll animation scripts as they fail under the local `file://` protocol.
- **Sticky Header**: Keep the navigation header relative (`#SITE_HEADER { position: relative !important; }`) to ensure it scrolls out of view naturally rather than blocking page content.

## Asset Reference Rules
- All local images are located in the [images/](file:///Users/sarun/.gemini/antigravity/scratch/empower-young/images) directory.
- Avoid absolute URL prefixes referencing the live Wix CDN or site (`supratimdeb48.wixsite.com`) for internal page media.
