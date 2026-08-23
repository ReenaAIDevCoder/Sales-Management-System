from datetime import datetime

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from extensions import db
from models import Activity


activity_bp = Blueprint(
    "activity",
    __name__,
    url_prefix="/activities"
)


# =========================================================
# LIST ACTIVITIES
# =========================================================

@activity_bp.route("/")
def list_activities():

    activities = Activity.query.order_by(
        Activity.activity_date.desc()
    ).all()

    return render_template(
        "activities/list.html",
        activities=activities
    )


# =========================================================
# ADD ACTIVITY
# =========================================================

@activity_bp.route(
    "/add",
    methods=["GET", "POST"]
)
def add_activity():

    if request.method == "POST":

        activity_date = request.form.get(
            "activity_date",
            ""
        ).strip()


        # -------------------------------------------------
        # Validate Activity Date
        # -------------------------------------------------

        try:

            parsed_activity_date = (
                datetime.strptime(
                    activity_date,
                    "%Y-%m-%dT%H:%M"
                )
                if activity_date
                else datetime.now()
            )

        except ValueError:

            flash(
                "Invalid activity date.",
                "error"
            )

            return render_template(
                "activities/add.html"
            )


        # -------------------------------------------------
        # Convert IDs safely
        # -------------------------------------------------

        user_id_value = request.form.get(
            "user_id",
            ""
        ).strip()

        customer_id_value = request.form.get(
            "customer_id",
            ""
        ).strip()

        opportunity_id_value = request.form.get(
            "opportunity_id",
            ""
        ).strip()

        duration_value = request.form.get(
            "duration_minutes",
            ""
        ).strip()


        try:

            user_id = (
                int(user_id_value)
                if user_id_value
                else None
            )

            customer_id = (
                int(customer_id_value)
                if customer_id_value
                else None
            )

            opportunity_id = (
                int(opportunity_id_value)
                if opportunity_id_value
                else None
            )

            duration_minutes = (
                int(duration_value)
                if duration_value
                else None
            )

        except ValueError:

            flash(
                "User, customer, opportunity and duration values must be valid numbers.",
                "error"
            )

            return render_template(
                "activities/add.html"
            )


        # -------------------------------------------------
        # Create Activity
        # -------------------------------------------------

        activity = Activity(

            user_id=user_id,

            customer_id=customer_id,

            opportunity_id=opportunity_id,

            activity_type=request.form.get(
                "activity_type",
                ""
            ).strip(),

            subject=request.form.get(
                "subject",
                ""
            ).strip(),

            description=request.form.get(
                "description",
                ""
            ).strip(),

            activity_date=parsed_activity_date,

            duration_minutes=duration_minutes,

            status=request.form.get(
                "status",
                "Completed"
            ).strip()
        )


        db.session.add(
            activity
        )

        db.session.commit()


        flash(
            "Activity added successfully.",
            "success"
        )


        return redirect(
            url_for(
                "activity.list_activities"
            )
        )


    return render_template(
        "activities/add.html"
    )


# =========================================================
# ACTIVITY DETAIL
# =========================================================

@activity_bp.route(
    "/<int:activity_id>"
)
def activity_detail(activity_id):

    activity = Activity.query.get_or_404(
        activity_id
    )

    return render_template(
        "activities/list.html",
        activities=[activity]
    )


# =========================================================
# DELETE ACTIVITY
# =========================================================

@activity_bp.route(
    "/<int:activity_id>/delete",
    methods=["POST"]
)
def delete_activity(activity_id):

    activity = Activity.query.get_or_404(
        activity_id
    )


    db.session.delete(
        activity
    )

    db.session.commit()


    flash(
        "Activity deleted successfully.",
        "success"
    )


    return redirect(
        url_for(
            "activity.list_activities"
        )
    )