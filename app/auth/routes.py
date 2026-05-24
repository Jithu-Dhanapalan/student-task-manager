from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from app.extensions import db, bcrypt
from app.models.user import User

auth = Blueprint("auth", __name__)


@auth.route("/")
def home():
    return redirect(url_for("auth.login"))


@auth.route("/register", methods=["GET", "POST"])
def register():

    if current_user.is_authenticated:
        return redirect(url_for("tasks.dashboard"))

    if request.method == "POST":

        name = request.form.get("name")

        email = request.form.get("email")

        password = request.form.get("password")

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:

            flash("Email already registered.")

            return redirect(url_for("auth.register"))

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        user = User(
            name=name,
            email=email,
            password=hashed_password
        )

        # ADMIN ACCOUNT

        if email == "admin@gmail.com":
            user.role = "admin"

        db.session.add(user)

        db.session.commit()

        flash("Registration successful. Please login.")

        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        # MAKE ADMIN
        if user and user.email == "admin@gmail.com":
            user.role = "admin"
            db.session.commit()

        if user and bcrypt.check_password_hash(user.password, password):

            login_user(user)

            # ADMIN REDIRECT
            if user.role == "admin":
                return redirect(url_for("admin.admin_dashboard"))

            return redirect(url_for("tasks.dashboard"))

        flash("Invalid email or password", "danger")

    return render_template("login.html")

@auth.route("/logout")
def logout():

    logout_user()

    flash("Logged out successfully.")

    return redirect(url_for("auth.login"))