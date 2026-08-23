from flask import Blueprint, render_template
from extensions import db
from models import SalesTarget, Opportunity


sales_bp = Blueprint(
    "sales",
    __name__,
    url_prefix="/sales"
)


@sales_bp.route("/targets")
def targets():
    targets = SalesTarget.query.all()

    return render_template(
        "sales/targets.html",
        targets=targets
    )


@sales_bp.route("/performance")
def performance():
    targets = SalesTarget.query.all()

    total_target = sum(
        target.target_amount or 0
        for target in targets
    )

    total_achieved = sum(
        target.achieved_amount or 0
        for target in targets
    )

    return render_template(
        "sales/performance.html",
        total_target=total_target,
        total_achieved=total_achieved
    )


@sales_bp.route("/pipeline")
def pipeline():
    opportunities = Opportunity.query.filter_by(
        status="Open"
    ).all()

    total_pipeline = sum(
        opportunity.deal_value or 0
        for opportunity in opportunities
    )

    return render_template(
        "sales/pipeline.html",
        opportunities=opportunities,
        total_pipeline=total_pipeline
    )