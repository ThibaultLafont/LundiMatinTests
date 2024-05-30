from flask import Flask
from .views import main_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    from .views import format_phone_number
    app.jinja_env.filters['format_phone'] = format_phone_number

    app.register_blueprint(main_blueprint)

    return app
