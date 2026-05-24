from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.models.user import User
from app.models.task import Task

admin = Blueprint("admin", __name__)


@admin.route("/admin")
@login_required
def admin_dashboard():
    if current_user.role != "admin":
        return redirect(url_for("tasks.dashboard"))

    users = User.query.all()
    tasks = Task.query.all()

    total_users = User.query.count()
    total_tasks = Task.query.count()
    completed_tasks = Task.query.filter_by(status="Completed").count()
    pending_tasks = Task.query.filter_by(status="Pending").count()

    return render_template(
        "admin.html",
        users=users,
        tasks=tasks,
        total_users=total_users,
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        pending_tasks=pending_tasks
    )