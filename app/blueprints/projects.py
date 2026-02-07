from flask import Blueprint, render_template
from app.extensions import load_markdown

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/projects')
def index():
    content = load_markdown('projects')
    return render_template('projects.html', content=content)
