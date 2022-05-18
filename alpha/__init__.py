from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os



basedir = os.path.abspath(os.path.dirname(__file__))

bootstrap = Bootstrap()
db = SQLAlchemy()



def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alpha.db'
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
    app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'
    app.config["uploads"] = os.path.join(basedir, "uploads")
    app.config["output"] = os.path.join(basedir, "output")
    app.config["static"] = os.path.join(basedir, "static")
    app.config["images"] = os.path.join(basedir, "static", "images")
    app.config["templates"] = os.path.join(basedir, "templates")
    db.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .alpha import alpha as alpha_blueprint
    app.register_blueprint(alpha_blueprint)
    return app
