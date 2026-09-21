import os
import re
from html.parser import HTMLParser

class PagesContainerParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_container = False
        self.container_depth = 0
        self.text_pieces = []
        self.sections_count = 0
        self.images_count = 0

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if attrs_dict.get('id') == 'PAGES_CONTAINER':
            self.in_container = True
            self.container_depth = 0
            
        if self.in_container:
            self.container_depth += 1
            if tag == 'section':
                self.sections_count += 1
            elif tag == 'img':
                self.images_count += 1

    def handle_endtag(self, tag):
        if self.in_container:
            self.container_depth -= 1
            if self.container_depth == 0:
                self.in_container = False

    def handle_data(self, data):
        if self.in_container:
            self.text_pieces.append(data)

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

for fname in files:
    fpath = os.path.join(workspace_dir, fname)
    if not os.path.exists(fpath):
        print(f"File {fname} does not exist")
        continue
        
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()
        
    parser = PagesContainerParser()
    parser.feed(html)
    
    text_content = " ".join(parser.text_pieces).strip()
    words = text_content.split()
    word_count = len(words)
    char_count = len(text_content)
    
    print(f"File: {fname} | Words: {word_count} | Chars: {char_count} | Sections: {parser.sections_count} | Images: {parser.images_count}")
    if word_count < 10:
        print(f"  WARNING: Content is extremely sparse: '{text_content[:200]}'")
