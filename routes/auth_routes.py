from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

from flask_login import (
    login_user,
    logout_user
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from extensions import db
from models import User


# =========================================================
# BLUEPRINT
# =========================================================

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


# =========================================================
# LOGIN
# =========================================================

@auth_bp.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if request.method == "POST":

        email = request.form.get(
            "email",
            ""
        ).strip().lower()

        password = request.form.get(
            "password",
            ""
        )

        # Find user
        user = User.query.filter_by(
            email=email
        ).first()

        # Check credentials
        if (
            user is not None
            and user.is_active
            and check_password_hash(
                user.password,
                password
            )
        ):

            # Flask-Login
            login_user(
                user,
                remember=True
            )

            # Application session
            session["user_id"] = user.id
            session["user_name"] = user.name
            session["user_role"] = user.role

            return redirect(
                url_for(
                    "dashboard.dashboard"
                )
            )

        flash(
            "Invalid email or password.",
            "error"
        )

    return render_template(
        "login.html"
    )


# =========================================================
# CREATE ACCOUNT / REGISTER
# =========================================================

@auth_bp.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    if request.method == "POST":

        name = request.form.get(
            "name",
            ""
        ).strip()

        email = request.form.get(
            "email",
            ""
        ).strip().lower()

        password = request.form.get(
            "password",
            ""
        )

        confirm_password = request.form.get(
            "confirm_password",
            ""
        )

        role = request.form.get(
            "role",
            "Sales Representative"
        ).strip()

        region = request.form.get(
            "region",
            ""
        ).strip()


        # -------------------------------------------------
        # Required fields
        # -------------------------------------------------

        if not name:

            flash(
                "Full name is required.",
                "error"
            )

            return render_template(
                "register.html"
            )


        if not email:

            flash(
                "Email is required.",
                "error"
            )

            return render_template(
                "register.html"
            )


        if not password:

            flash(
                "Password is required.",
                "error"
            )

            return render_template(
                "register.html"
            )


        # -------------------------------------------------
        # Password confirmation
        # -------------------------------------------------

        if password != confirm_password:

            flash(
                "Passwords do not match.",
                "error"
            )

            return render_template(
                "register.html"
            )


        # -------------------------------------------------
        # Password length
        # -------------------------------------------------

        if len(password) < 6:

            flash(
                "Password must contain at least 6 characters.",
                "error"
            )

            return render_template(
                "register.html"
            )


        # -------------------------------------------------
        # Check existing email
        # -------------------------------------------------

        existing_user = User.query.filter_by(
            email=email
        ).first()

        if existing_user:

            flash(
                "An account with this email already exists.",
                "error"
            )

            return render_template(
                "register.html"
            )


        # -------------------------------------------------
        # Create new user
        # -------------------------------------------------

        new_user = User(

            name=name,

            email=email,

            password=generate_password_hash(
                password
            ),

            role=role,

            region=region,

            is_active=True

        )


        try:

            db.session.add(
                new_user
            )

            db.session.commit()

        except Exception:

            db.session.rollback()

            flash(
                "Unable to create account. Please try again.",
                "error"
            )

            return render_template(
                "register.html"
            )


        flash(
            "Account created successfully. Please login.",
            "success"
        )

        return redirect(
            url_for(
                "auth.login"
            )
        )


    return render_template(
        "register.html"
    )


# =========================================================
# FORGOT PASSWORD
# =========================================================

@auth_bp.route(
    "/forgot-password",
    methods=["GET", "POST"]
)
def forgot_password():

    if request.method == "POST":

        email = request.form.get(
            "email",
            ""
        ).strip().lower()


        # Empty email
        if not email:

            flash(
                "Please enter your email address.",
                "error"
            )

            return render_template(
                "forgot_password.html"
            )


        # Find user
        user = User.query.filter_by(
            email=email
        ).first()


        # User does not exist
        if user is None:

            flash(
                "No account found with this email.",
                "error"
            )

            return render_template(
                "forgot_password.html"
            )


        # User exists
        return redirect(
            url_for(
                "auth.reset_password",
                user_id=user.id
            )
        )


    return render_template(
        "forgot_password.html"
    )


# =========================================================
# RESET PASSWORD
# =========================================================

@auth_bp.route(
    "/reset-password/<int:user_id>",
    methods=["GET", "POST"]
)
def reset_password(user_id):

    user = User.query.get_or_404(
        user_id
    )


    if request.method == "POST":

        password = request.form.get(
            "password",
            ""
        )

        confirm_password = request.form.get(
            "confirm_password",
            ""
        )


        # -------------------------------------------------
        # Password required
        # -------------------------------------------------

        if not password:

            flash(
                "Please enter a new password.",
                "error"
            )

            return render_template(
                "reset_password.html",
                user=user
            )


        # -------------------------------------------------
        # Minimum password length
        # -------------------------------------------------

        if len(password) < 6:

            flash(
                "Password must contain at least 6 characters.",
                "error"
            )

            return render_template(
                "reset_password.html",
                user=user
            )


        # -------------------------------------------------
        # Password confirmation
        # -------------------------------------------------

        if password != confirm_password:

            flash(
                "Passwords do not match.",
                "error"
            )

            return render_template(
                "reset_password.html",
                user=user
            )


        # -------------------------------------------------
        # Update password
        # -------------------------------------------------

        user.password = generate_password_hash(
            password
        )


        try:

            db.session.commit()

        except Exception:

            db.session.rollback()

            flash(
                "Unable to reset password. Please try again.",
                "error"
            )

            return render_template(
                "reset_password.html",
                user=user
            )


        flash(
            "Password reset successfully. Please login.",
            "success"
        )

        return redirect(
            url_for(
                "auth.login"
            )
        )


    return render_template(
        "reset_password.html",
        user=user
    )


# =========================================================
# LOGOUT
# =========================================================

@auth_bp.route(
    "/logout"
)
def logout():

    logout_user()

    session.clear()

    flash(
        "You have been logged out.",
        "success"
    )

    return redirect(
        url_for(
            "auth.login"
        )
    )