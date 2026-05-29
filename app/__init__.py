from flask import Flask, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from config import Config
from app.extensions import db, bcrypt, login_manager

limiter = Limiter(key_func=get_remote_address)


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    limiter.init_app(app)

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/health/")
    def health():
        return {"status": "healthy"}

    from app.models.user import User
    from app.models.task import Task

    from app.auth.routes import auth
    from app.routes.task_routes import tasks
    from app.admin.routes import admin

    app.register_blueprint(auth)
    app.register_blueprint(tasks)
    app.register_blueprint(admin)

    with app.app_context():
        db.create_all()

    return app