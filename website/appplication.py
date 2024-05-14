from flask import Flask
from .views import view
from .auth import auth

def create_app():
    app = Flask(__name__)
    # app.config["SECRET_KEY"] = "w8vh2gbw1"

    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app