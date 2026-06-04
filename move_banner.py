import re

with open('index.html', 'r') as f:
    content = f.read()

# Match the trust banner
trust_banner_regex = re.compile(r'\s*<!-- Cinta de Autoridad -->\n\s*<section class="trust-banner">.*?</section>\n', re.DOTALL)
match = trust_banner_regex.search(content)

if match:
    trust_banner_html = match.group(0)
    
    # Remove it from its current location
    content = content.replace(trust_banner_html, '')
    
    # Find the timeline section
    timeline_regex = re.compile(r'\s*<!-- Timeline -->\n\s*<section id="timeline"')
    timeline_match = timeline_regex.search(content)
    
    if timeline_match:
        # Insert before the timeline
        new_content = content[:timeline_match.start()] + trust_banner_html + content[timeline_match.start():]
        
        with open('index.html', 'w') as f:
            f.write(new_content)
        print("Successfully moved the banner.")
    else:
        print("Timeline section not found.")
else:
    print("Trust banner not found.")
