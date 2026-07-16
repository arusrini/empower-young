import re

def fix_css(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # styles.css fixes
    content = re.sub(
        r'-webkit-background-clip:\s*text;',
        r'-webkit-background-clip: text;\n    background-clip: text;',
        content
    )

    # index.html minified CSS fixes
    content = re.sub(
        r'-webkit-appearance:none(?![a-zA-Z0-9\-])(?!;appearance:none)',
        r'-webkit-appearance:none;appearance:none',
        content
    )
    
    content = re.sub(
        r'-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none(?![a-zA-Z0-9\-])(?!;user-select:none)',
        r'-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none',
        content
    )
    
    content = re.sub(
        r'-ms-grid-row:([0-9/\s]+);(?![a-zA-Z0-9\-])(?!grid-row:)',
        r'-ms-grid-row:\1;grid-row:\1;',
        content
    )
    
    content = re.sub(
        r'-ms-grid-column:([0-9/\s]+);(?![a-zA-Z0-9\-])(?!grid-column:)',
        r'-ms-grid-column:\1;grid-column:\1;',
        content
    )

    content = re.sub(
        r'-webkit-clip-path:([^;}]+)(?![a-zA-Z0-9\-])(?!;clip-path:)',
        r'-webkit-clip-path:\1;clip-path:\1',
        content
    )

    with open(file_path, 'w') as f:
        f.write(content)

fix_css('/Users/sarun/.gemini/antigravity/scratch/empower-young/index.html')
fix_css('/Users/sarun/.gemini/antigravity/scratch/empower-young/styles.css')

print("Fixed CSS warnings!")
