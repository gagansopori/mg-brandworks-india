from flask import Flask

from app.blueprints.about import about_bp
from app.blueprints.contact import contact_bp
from app.blueprints.errors import errors_bp
from app.blueprints.home import home_bp
from app.blueprints.projects import projects_bp
from app.configs.app_config import settings
from app.configs.logging_config import LoggerConfig
from app.utils.extensions import mail, load_markdown


def create_app():

    LoggerConfig.setup(log_level='INFO')
    log = LoggerConfig.get_logger(__name__)

    app = Flask(__name__)
    # app.config['SECRET_KEY'] = 'your-very-secret-key-here'
    app.config.from_mapping(settings.flask_config)

    # Mail + CSRF for contact form (future release)
    mail.init_app(app)
    from app.utils.extensions import csrf
    csrf.init_app(app)

    log.info("Application Factory: Backend services and extensions initialized.")

    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(contact_bp)

    log.info("Application Factory: Successfully initialized all blueprints.")

    return app
