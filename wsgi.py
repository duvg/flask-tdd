import os

from application.app import create_app

app = create_app(os.environ.get("FLASK_CONFIG"))
