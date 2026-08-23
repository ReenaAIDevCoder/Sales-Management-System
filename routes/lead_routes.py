from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from extensions import db
from models import Lead


lead_bp = Blueprint(
    "lead",
    __name__,
    url_prefix="/leads"
)


# =========================================================
# LIST ALL LEADS
# =========================================================

@lead_bp.route("/")
def list_leads():

    leads = Lead.query.order_by(
        Lead.created_at.desc()
    ).all()

    return render_template(
        "leads/list.html",
        leads=leads
    )


# =========================================================
# ADD NEW LEAD
# =========================================================

@lead_bp.route(
    "/add",
    methods=["GET", "POST"]
)
def add_lead():

    if request.method == "POST":

        name = request.form.get(
            "name",
            ""
        ).strip()

        company = request.form.get(
            "company",
            ""
        ).strip()

        email = request.form.get(
            "email",
            ""
        ).strip()

        phone = request.form.get(
            "phone",
            ""
        ).strip()

        source = request.form.get(
            "source",
            ""
        ).strip()

        status = request.form.get(
            "status",
            "New"
        ).strip()

        priority = request.form.get(
            "priority",
            "Medium"
        ).strip()

        estimated_value_text = request.form.get(
            "estimated_value",
            "0"
        ).strip()


        # ---------------------------------------------
        # Validation
        # ---------------------------------------------

        if not name:

            flash(
                "Lead name is required.",
                "error"
            )

            return render_template(
                "leads/add.html"
            )


        try:

            estimated_value = float(
                estimated_value_text or 0
            )

        except ValueError:

            flash(
                "Estimated value must be a valid number.",
                "error"
            )

            return render_template(
                "leads/add.html"
            )


        # ---------------------------------------------
        # Create Lead
        # ---------------------------------------------

        lead = Lead(
            name=name,
            company=company,
            email=email,
            phone=phone,
            source=source,
            status=status,
            priority=priority,
            estimated_value=estimated_value
        )


        db.session.add(lead)

        db.session.commit()


        flash(
            "Lead added successfully.",
            "success"
        )


        return redirect(
            url_for(
                "lead.list_leads"
            )
        )


    return render_template(
        "leads/add.html"
    )


# =========================================================
# LEAD DETAIL
# =========================================================

@lead_bp.route(
    "/<int:lead_id>"
)
def lead_detail(lead_id):

    lead = Lead.query.get_or_404(
        lead_id
    )

    return render_template(
        "leads/detail.html",
        lead=lead
    )


# =========================================================
# EDIT LEAD
# =========================================================

@lead_bp.route(
    "/<int:lead_id>/edit",
    methods=["GET", "POST"]
)
def edit_lead(lead_id):

    lead = Lead.query.get_or_404(
        lead_id
    )


    if request.method == "POST":

        name = request.form.get(
            "name",
            ""
        ).strip()

        company = request.form.get(
            "company",
            ""
        ).strip()

        email = request.form.get(
            "email",
            ""
        ).strip()

        phone = request.form.get(
            "phone",
            ""
        ).strip()

        source = request.form.get(
            "source",
            ""
        ).strip()

        status = request.form.get(
            "status",
            "New"
        ).strip()

        priority = request.form.get(
            "priority",
            "Medium"
        ).strip()

        estimated_value_text = request.form.get(
            "estimated_value",
            "0"
        ).strip()


        # ---------------------------------------------
        # Validation
        # ---------------------------------------------

        if not name:

            flash(
                "Lead name is required.",
                "error"
            )

            return render_template(
                "leads/edit.html",
                lead=lead
            )


        try:

            estimated_value = float(
                estimated_value_text or 0
            )

        except ValueError:

            flash(
                "Estimated value must be a valid number.",
                "error"
            )

            return render_template(
                "leads/edit.html",
                lead=lead
            )


        # ---------------------------------------------
        # Update Lead
        # ---------------------------------------------

        lead.name = name

        lead.company = company

        lead.email = email

        lead.phone = phone

        lead.source = source

        lead.status = status

        lead.priority = priority

        lead.estimated_value = estimated_value


        db.session.commit()


        flash(
            "Lead updated successfully.",
            "success"
        )


        return redirect(
            url_for(
                "lead.lead_detail",
                lead_id=lead.id
            )
        )


    return render_template(
        "leads/edit.html",
        lead=lead
    )


# =========================================================
# DELETE LEAD
# =========================================================

@lead_bp.route(
    "/<int:lead_id>/delete",
    methods=["POST"]
)
def delete_lead(lead_id):

    lead = Lead.query.get_or_404(
        lead_id
    )


    db.session.delete(
        lead
    )

    db.session.commit()


    flash(
        "Lead deleted successfully.",
        "success"
    )


    return redirect(
        url_for(
            "lead.list_leads"
        )
    )