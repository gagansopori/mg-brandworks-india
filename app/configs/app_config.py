import os, json
from dotenv import load_dotenv

load_dotenv()

class ApplicationConfig:
    def __init__(self):
        self.config_dir = os.environ.get('CONFIG_DIR', os.getcwd())
        self.config_file = 'secrets.json'
        self._data = self._load_json()

    def _load_json(self):
        path = os.path.join(self.config_dir, self.config_file)
        if os.path.exists(path):
            with open(path, 'r') as f:
                return json.load(f)
        return None

    @property
    def flask_config(self):
        return {
            'SECRET_KEY': self._data.get('SECRET_KEY', 'default-key'),
            'MAIL_SERVER': self._data.get('MAIL_SERVER'),
            'MAIL_PORT': int(self._data.get('MAIL_PORT', 587)),
            'MAIL_USERNAME': self._data.get('MAIL_USERNAME'),
            'MAIL_PASSWORD': self._data.get('MAIL_PASSWORD'),
        }

settings = ApplicationConfig()