from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    login_manager.login_view = "auth.login"

    # HOME PAGE
    @app.route("/")
    def home():
        return render_template("index.html")

    # IMPORT MODELS
    from app.models.user import User
    from app.models.task import Task

    # REGISTER BLUEPRINTS
    from app.auth.routes import auth
    from app.routes.task_routes import tasks
    from app.admin.routes import admin

    app.register_blueprint(auth)
    app.register_blueprint(tasks)
    app.register_blueprint(admin)

    # CREATE DATABASE TABLES
    with app.app_context():
        db.create_all()

    return app


@login_manager.user_loader
def load_user(user_id):
    from app.models.user import User
    return User.query.get(int(user_id))