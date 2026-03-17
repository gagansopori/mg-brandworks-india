import os
from pathlib import Path

import markdown
from flask_mail import Mail
from flask_wtf import CSRFProtect

from app.configs.app_config import settings

mail = Mail()
csrf = CSRFProtect()

def load_markdown(filename):
    """Load and render markdown file to HTML"""
    content_path = os.path.join(settings.markdown_dir, f'{filename}.md')
    try:
        with open(content_path, 'r') as f:
            md_content = f.read()
        html_content = markdown.markdown(md_content)
        return html_content
    except FileNotFoundError:
        return '<p>Content not found</p>'
