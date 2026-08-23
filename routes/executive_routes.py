from flask import Blueprint, render_template
from extensions import db
from models import (
    Opportunity,
    User
)


executive_bp = Blueprint(
    "executive",
    __name__,
    url_prefix="/executive"
)


@executive_bp.route("/analytics")
def analytics():

    opportunities = Opportunity.query.all()

    total_opportunities = len(
        opportunities
    )

    won_opportunities = sum(
        1
        for opportunity in opportunities
        if opportunity.status == "Won"
    )

    won_revenue = sum(
        opportunity.deal_value or 0
        for opportunity in opportunities
        if opportunity.status == "Won"
    )

    if total_opportunities > 0:

        win_rate = (
            won_opportunities
            /
            total_opportunities
        ) * 100

    else:

        win_rate = 0

    return render_template(
        "executive/analytics.html",
        total_revenue=won_revenue,
        total_opportunities=total_opportunities,
        won_opportunities=won_opportunities,
        win_rate=win_rate
    )


@executive_bp.route("/regional-kpi")
def regional_kpi():

    users = User.query.all()

    opportunities = Opportunity.query.all()

    regions = sorted(
        set(
            user.region
            for user in users
            if getattr(user, "region", None)
        )
    )

    regional_data = []

    for region in regions:

        region_users = [
            user
            for user in users
            if getattr(user, "region", None) == region
        ]

        user_ids = [
            user.id
            for user in region_users
        ]

        region_opportunities = [
            opportunity
            for opportunity in opportunities
            if getattr(
                opportunity,
                "assigned_to",
                None
            ) in user_ids
        ]

        won_deals = [
            opportunity
            for opportunity in region_opportunities
            if opportunity.status == "Won"
        ]

        revenue = sum(
            opportunity.deal_value or 0
            for opportunity in won_deals
        )

        if region_opportunities:

            win_rate = (
                len(won_deals)
                /
                len(region_opportunities)
            ) * 100

        else:

            win_rate = 0

        regional_data.append({
            "region": region,
            "sales_reps": len(region_users),
            "opportunities": len(
                region_opportunities
            ),
            "won_deals": len(won_deals),
            "revenue": revenue,
            "win_rate": win_rate
        })

    return render_template(
        "executive/regional_kpi.html",
        regional_data=regional_data
    )


@executive_bp.route("/win-loss")
def win_loss():

    opportunities = Opportunity.query.filter(
        Opportunity.status.in_([
            "Won",
            "Lost"
        ])
    ).all()

    total_opportunities = len(
        opportunities
    )

    won_opportunities = sum(
        1
        for opportunity in opportunities
        if opportunity.status == "Won"
    )

    lost_opportunities = sum(
        1
        for opportunity in opportunities
        if opportunity.status == "Lost"
    )

    if total_opportunities > 0:

        win_rate = (
            won_opportunities
            /
            total_opportunities
        ) * 100

    else:

        win_rate = 0

    return render_template(
        "executive/win_loss.html",
        opportunities=opportunities,
        total_opportunities=total_opportunities,
        won_opportunities=won_opportunities,
        lost_opportunities=lost_opportunities,
        win_rate=win_rate
    )


@executive_bp.route("/revenue-forecast")
def revenue_forecast():

    opportunities = Opportunity.query.filter_by(
        status="Open"
    ).all()

    total_pipeline = sum(
        opportunity.deal_value or 0
        for opportunity in opportunities
    )

    weighted_forecast = sum(
        (opportunity.deal_value or 0)
        *
        ((opportunity.probability or 0) / 100)
        for opportunity in opportunities
    )

    won_opportunities = Opportunity.query.filter_by(
        status="Won"
    ).all()

    won_revenue = sum(
        opportunity.deal_value or 0
        for opportunity in won_opportunities
    )

    return render_template(
        "executive/revenue_forecast.html",
        opportunities=opportunities,
        total_pipeline=total_pipeline,
        weighted_forecast=weighted_forecast,
        won_revenue=won_revenue
    )