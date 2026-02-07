from flask import Blueprint
from flask import render_template

from app.extensions import load_markdown

about_bp = Blueprint('about', __name__)

@about_bp.route("/about")
def index():
    content = load_markdown('about')
    return render_template('about.html', content=content)
