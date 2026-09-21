import os
import re
import urllib.request

# Resolve workspace_dir dynamically relative to script location
workspace_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
files = [
    "index.html",
    "about.html",
    "about-3.html",
    "about-9.html",
    "get-involved.html",
    "mentorship.html"
]

img_pattern = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']')

for fname in files:
    fpath = os.path.join(workspace_dir, fname)
    if not os.path.exists(fpath):
        print(f"File {fpath} does not exist")
        continue
        
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
        
    imgs = img_pattern.findall(content)
    print(f"\n--- Images in {fname} (Total: {len(imgs)}) ---")
    
    unique_imgs = sorted(list(set(imgs)))
    for img in unique_imgs:
        if img.startswith("http"):
            # Check if URL is accessible
            try:
                # Just send a HEAD request to check availability
                req = urllib.request.Request(img, method="HEAD")
                with urllib.request.urlopen(req, timeout=3) as resp:
                    status = resp.status
                print(f"  [OK] {img} (status: {status})")
            except Exception as e:
                print(f"  [BROKEN] {img} (Error: {e})")
        else:
            # Local path check
            local_path = os.path.join(workspace_dir, img.lstrip("./"))
            if os.path.exists(local_path):
                print(f"  [OK] Local: {img}")
            else:
                print(f"  [MISSING] Local: {img}")
