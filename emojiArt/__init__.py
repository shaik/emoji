from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from .config import Config
from .routes import configure_routes
from .utils import setup_color_trees


def create_app():
    app = Flask(__name__,
                template_folder="../templates",
                static_folder="../static")
    app.config.from_object(Config)

    # Initialize Flask-Limiter
    limiter = Limiter(key_func=get_remote_address, default_limits=["100 per day", "100 per hour"])
    limiter.init_app(app)
    setup_color_trees()  # Call the function to set up color trees

    configure_routes(app)

    return app
