from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.extensions import db
from app.models.task import Task

tasks = Blueprint("tasks", __name__)


@tasks.route("/dashboard")
@login_required
def dashboard():
    user_tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template("dashboard.html", tasks=user_tasks)


@tasks.route("/add-task", methods=["POST"])
@login_required
def add_task():
    title = request.form.get("title")
    description = request.form.get("description")

    task = Task(
        title=title,
        description=description,
        user_id=current_user.id
    )

    db.session.add(task)
    db.session.commit()

    return redirect(url_for("tasks.dashboard"))


@tasks.route("/complete-task/<int:id>")
@login_required
def complete_task(id):
    task = Task.query.get_or_404(id)

    if task.user_id == current_user.id:
        task.status = "Completed"
        db.session.commit()

    return redirect(url_for("tasks.dashboard"))


@tasks.route("/delete-task/<int:id>")
@login_required
def delete_task(id):
    task = Task.query.get_or_404(id)

    if task.user_id == current_user.id:
        db.session.delete(task)
        db.session.commit()

    return redirect(url_for("tasks.dashboard"))