from flask import Blueprint, render_template, session, redirect, url_for
from extensions import db

dashboard_bp = Blueprint(
    "dashboard",
    __name__
)


@dashboard_bp.route("/")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    return render_template(
        "dashboard.html",
        user_name=session.get("user_name"),
        user_role=session.get("user_role")
    )