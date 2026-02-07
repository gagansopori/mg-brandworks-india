from flask import Flask

from app.blueprints.about import about_bp
from app.blueprints.contact import contact_bp
from app.blueprints.errors import errors_bp
from app.blueprints.home import home_bp
from app.blueprints.projects import projects_bp
from app.extensions import mail, csrf, load_markdown


def create_app():
    app = Flask(__name__)
    # This will be stored in .env file on the server.
    app.config['SECRET_KEY'] = 'your-very-secret-key-here'

    # Mail + CSRF for contact form (future release)
    mail.init_app(app)
    csrf.init_app(app)

    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(errors_bp)

    return app
