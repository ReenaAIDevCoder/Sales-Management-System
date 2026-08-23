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
from models import Opportunity


opportunity_bp = Blueprint(
    "opportunity",
    __name__,
    url_prefix="/opportunities"
)


# =========================================================
# LIST OPPORTUNITIES
# =========================================================

@opportunity_bp.route("/")
def list_opportunities():

    opportunities = Opportunity.query.order_by(
        Opportunity.created_at.desc()
    ).all()

    return render_template(
        "opportunities/list.html",
        opportunities=opportunities
    )


# =========================================================
# ADD OPPORTUNITY
# =========================================================

@opportunity_bp.route(
    "/add",
    methods=["GET", "POST"]
)
def add_opportunity():

    if request.method == "POST":

        expected_close_date = request.form.get(
            "expected_close_date",
            ""
        ).strip()

        name = request.form.get(
            "name",
            ""
        ).strip()

        customer_id_value = request.form.get(
            "customer_id",
            ""
        ).strip()

        deal_value_text = request.form.get(
            "deal_value",
            "0"
        ).strip()

        probability_text = request.form.get(
            "probability",
            "0"
        ).strip()

        stage = request.form.get(
            "stage",
            "Prospecting"
        ).strip()

        status = request.form.get(
            "status",
            "Open"
        ).strip()

        notes = request.form.get(
            "notes",
            ""
        ).strip()


        if not name:

            flash(
                "Opportunity name is required.",
                "error"
            )

            return render_template(
                "opportunities/add.html"
            )


        try:

            customer_id = (
                int(customer_id_value)
                if customer_id_value
                else None
            )

            deal_value = float(
                deal_value_text or 0
            )

            probability = float(
                probability_text or 0
            )

        except ValueError:

            flash(
                "Customer ID, deal value and probability must be valid numbers.",
                "error"
            )

            return render_template(
                "opportunities/add.html"
            )


        try:

            close_date = (
                datetime.strptime(
                    expected_close_date,
                    "%Y-%m-%d"
                ).date()
                if expected_close_date
                else None
            )

        except ValueError:

            flash(
                "Invalid expected close date.",
                "error"
            )

            return render_template(
                "opportunities/add.html"
            )


        opportunity = Opportunity(

            name=name,

            customer_id=customer_id,

            deal_value=deal_value,

            probability=probability,

            stage=stage,

            expected_close_date=close_date,

            status=status,

            notes=notes
        )


        db.session.add(
            opportunity
        )

        db.session.commit()


        flash(
            "Opportunity added successfully.",
            "success"
        )


        return redirect(
            url_for(
                "opportunity.list_opportunities"
            )
        )


    return render_template(
        "opportunities/add.html"
    )


# =========================================================
# OPPORTUNITY DETAIL
# =========================================================

@opportunity_bp.route(
    "/<int:opportunity_id>"
)
def opportunity_detail(opportunity_id):

    opportunity = Opportunity.query.get_or_404(
        opportunity_id
    )

    return render_template(
        "opportunities/detail.html",
        opportunity=opportunity
    )


# =========================================================
# EDIT OPPORTUNITY
# =========================================================

@opportunity_bp.route(
    "/<int:opportunity_id>/edit",
    methods=["GET", "POST"]
)
def edit_opportunity(opportunity_id):

    opportunity = Opportunity.query.get_or_404(
        opportunity_id
    )


    if request.method == "POST":

        expected_close_date = request.form.get(
            "expected_close_date",
            ""
        ).strip()

        name = request.form.get(
            "name",
            ""
        ).strip()

        customer_id_value = request.form.get(
            "customer_id",
            ""
        ).strip()

        deal_value_text = request.form.get(
            "deal_value",
            "0"
        ).strip()

        probability_text = request.form.get(
            "probability",
            "0"
        ).strip()

        stage = request.form.get(
            "stage",
            "Prospecting"
        ).strip()

        status = request.form.get(
            "status",
            "Open"
        ).strip()

        notes = request.form.get(
            "notes",
            ""
        ).strip()


        if not name:

            flash(
                "Opportunity name is required.",
                "error"
            )

            return render_template(
                "opportunities/edit.html",
                opportunity=opportunity
            )


        try:

            customer_id = (
                int(customer_id_value)
                if customer_id_value
                else None
            )

            deal_value = float(
                deal_value_text or 0
            )

            probability = float(
                probability_text or 0
            )

        except ValueError:

            flash(
                "Customer ID, deal value and probability must be valid numbers.",
                "error"
            )

            return render_template(
                "opportunities/edit.html",
                opportunity=opportunity
            )


        try:

            close_date = (
                datetime.strptime(
                    expected_close_date,
                    "%Y-%m-%d"
                ).date()
                if expected_close_date
                else None
            )

        except ValueError:

            flash(
                "Invalid expected close date.",
                "error"
            )

            return render_template(
                "opportunities/edit.html",
                opportunity=opportunity
            )


        opportunity.name = name

        opportunity.customer_id = customer_id

        opportunity.deal_value = deal_value

        opportunity.probability = probability

        opportunity.stage = stage

        opportunity.expected_close_date = close_date

        opportunity.status = status

        opportunity.notes = notes


        db.session.commit()


        flash(
            "Opportunity updated successfully.",
            "success"
        )


        return redirect(
            url_for(
                "opportunity.opportunity_detail",
                opportunity_id=opportunity.id
            )
        )


    return render_template(
        "opportunities/edit.html",
        opportunity=opportunity
    )


# =========================================================
# DELETE OPPORTUNITY
# =========================================================

@opportunity_bp.route(
    "/<int:opportunity_id>/delete",
    methods=["POST"]
)
def delete_opportunity(opportunity_id):

    opportunity = Opportunity.query.get_or_404(
        opportunity_id
    )


    db.session.delete(
        opportunity
    )

    db.session.commit()


    flash(
        "Opportunity deleted successfully.",
        "success"
    )


    return redirect(
        url_for(
            "opportunity.list_opportunities"
        )
    )