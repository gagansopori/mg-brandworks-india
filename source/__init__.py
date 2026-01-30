from flask import Flask, render_template
import markdown
import os

app = Flask(__name__)

def load_markdown(filename):
    """Load and render markdown file to HTML"""
    content_path = os.path.join(os.path.dirname(__file__), '..', 'content', f'{filename}.md')
    try:
        with open(content_path, 'r') as f:
            md_content = f.read()
        html_content = markdown.markdown(md_content)
        return html_content
    except FileNotFoundError:
        return '<p>Content not found</p>'

@app.route("/")
def home():
    content = load_markdown('home')
    return render_template('index.html', content=content)

@app.route("/about")
def about():
    content = load_markdown('about')
    return render_template('about.html', content=content)

@app.route("/projects")
def projects():
    content = load_markdown('projects')
    return render_template('projects.html', content=content)

@app.route("/contact")
def contact():
    content = load_markdown('contact')
    return render_template('contact.html', content=content)

if __name__ == '__main__':
    app.run(debug=True)