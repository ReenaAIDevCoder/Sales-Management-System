from flask import Blueprint, render_template
from extensions import db

from models import (
    Activity,
    Satisfaction,
    AccountPlan,
    Renewal
)


account_bp = Blueprint(
    "account",
    __name__,
    url_prefix="/accounts"
)


@account_bp.route("/history")
def history():

    activities = Activity.query.order_by(
        Activity.activity_date.desc()
    ).all()

    return render_template(
        "accounts/history.html",
        activities=activities
    )


@account_bp.route("/satisfaction")
def satisfaction():

    satisfactions = Satisfaction.query.all()

    if satisfactions:

        total_rating = sum(
            satisfaction.rating or 0
            for satisfaction in satisfactions
        )

        average_rating = (
            total_rating /
            len(satisfactions)
        )

    else:

        average_rating = 0


    return render_template(
        "accounts/satisfaction.html",
        satisfactions=satisfactions,
        average_rating=average_rating
    )


@account_bp.route("/plans")
def plans():

    plans = AccountPlan.query.order_by(
        AccountPlan.id.desc()
    ).all()

    return render_template(
        "accounts/plans.html",
        plans=plans
    )


@account_bp.route("/renewals")
def renewals():

    renewals = Renewal.query.order_by(
        Renewal.renewal_date.asc()
    ).all()

    upcoming_renewals = [
        renewal
        for renewal in renewals
        if renewal.status == "Active"
    ]

    expired_renewals = [
        renewal
        for renewal in renewals
        if renewal.status == "Expired"
    ]

    return render_template(
        "accounts/renewals.html",
        renewals=renewals,
        upcoming_renewals=upcoming_renewals,
        expired_renewals=expired_renewals
    )