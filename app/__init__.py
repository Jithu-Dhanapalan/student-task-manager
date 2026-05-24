from flask import Flask
from config import Config
from app.extensions import db, bcrypt, login_manager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

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