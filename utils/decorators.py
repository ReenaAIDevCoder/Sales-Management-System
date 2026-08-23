from functools import wraps

from flask import session, redirect, url_for


def login_required(function):

    @wraps(function)
    def decorated_function(*args, **kwargs):

        if "user_id" not in session:
            return redirect(
                url_for("auth.login")
            )

        return function(*args, **kwargs)

    return decorated_function


def role_required(*allowed_roles):

    def decorator(function):

        @wraps(function)
        def decorated_function(*args, **kwargs):

            if "user_id" not in session:
                return redirect(
                    url_for("auth.login")
                )

            user_role = session.get("user_role")

            if user_role not in allowed_roles:
                return (
                    "Access denied. "
                    "You do not have permission "
                    "to access this page."
                ), 403

            return function(*args, **kwargs)

        return decorated_function

    return decorator