from flask import Blueprint, render_template
from extensions import db
from models import (
    User,
    Territory,
    DiscountRequest,
    Opportunity
)


manager_bp = Blueprint(
    "manager",
    __name__,
    url_prefix="/manager"
)


@manager_bp.route("/team")
def team():

    team_members = User.query.filter(
        User.role.in_([
            "Sales Representative",
            "Sales Manager"
        ])
    ).all()

    return render_template(
        "manager/team.html",
        team_members=team_members
    )


@manager_bp.route("/territories")
def territories():

    territories = Territory.query.all()

    return render_template(
        "manager/territories.html",
        territories=territories
    )


@manager_bp.route("/discounts")
def discounts():

    discount_requests = (
        DiscountRequest.query
        .order_by(
            DiscountRequest.id.desc()
        )
        .all()
    )

    return render_template(
        "manager/discounts.html",
        discount_requests=discount_requests
    )


@manager_bp.route("/forecasts")
def forecasts():

    opportunities = Opportunity.query.filter_by(
        status="Open"
    ).all()

    total_pipeline = sum(
        opportunity.deal_value or 0
        for opportunity in opportunities
    )

    forecast_revenue = sum(
        (opportunity.deal_value or 0)
        *
        ((opportunity.probability or 0) / 100)
        for opportunity in opportunities
    )

    return render_template(
        "manager/forecasts.html",
        opportunities=opportunities,
        total_pipeline=total_pipeline,
        forecast_revenue=forecast_revenue
    )