import os

import markdown
from flask_mail import Mail
from flask_wtf import CSRFProtect


def load_markdown(filename):
    """Load and render markdown file to HTML"""
    content_path = os.path.join(os.path.dirname(__file__), 'static', 'content', f'{filename}.md')
    try:
        with open(content_path, 'r') as f:
            md_content = f.read()
        html_content = markdown.markdown(md_content)
        return html_content
    except FileNotFoundError:
        return '<p>Content not found</p>'


mail = Mail()
csrf = CSRFProtect()
