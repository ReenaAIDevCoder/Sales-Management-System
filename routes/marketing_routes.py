from flask import Blueprint, render_template
from extensions import db
from models import (
    Campaign,
    Lead,
    Customer,
    Opportunity
)


marketing_bp = Blueprint(
    "marketing",
    __name__,
    url_prefix="/marketing"
)


@marketing_bp.route("/campaigns")
def campaigns():

    campaigns = Campaign.query.order_by(
        Campaign.id.desc()
    ).all()

    total_leads = sum(
        campaign.leads_generated or 0
        for campaign in campaigns
    )

    qualified_leads = sum(
        campaign.qualified_leads or 0
        for campaign in campaigns
    )

    total_revenue = sum(
        campaign.revenue_generated or 0
        for campaign in campaigns
    )

    return render_template(
        "marketing/campaigns.html",
        campaigns=campaigns,
        total_leads=total_leads,
        qualified_leads=qualified_leads,
        total_revenue=total_revenue
    )


@marketing_bp.route("/qualified-leads")
def qualified_leads():

    leads = Lead.query.filter_by(
        status="Qualified"
    ).order_by(
        Lead.id.desc()
    ).all()

    estimated_pipeline = sum(
        lead.estimated_value or 0
        for lead in leads
    )

    return render_template(
        "marketing/qualified_leads.html",
        leads=leads,
        estimated_pipeline=estimated_pipeline
    )


@marketing_bp.route("/segments")
def segments():

    customers = Customer.query.order_by(
        Customer.name.asc()
    ).all()

    active_customers = sum(
        1
        for customer in customers
        if customer.status == "Active"
    )

    industries = sorted(
        set(
            customer.industry
            for customer in customers
            if customer.industry
        )
    )

    return render_template(
        "marketing/segments.html",
        customers=customers,
        active_customers=active_customers,
        industries=industries
    )


@marketing_bp.route("/collaboration")
def collaboration():

    total_leads = Lead.query.count()

    qualified_leads = Lead.query.filter_by(
        status="Qualified"
    ).count()

    total_opportunities = Opportunity.query.count()

    won_opportunities = Opportunity.query.filter_by(
        status="Won"
    ).count()

    return render_template(
        "marketing/collaboration.html",
        total_leads=total_leads,
        qualified_leads=qualified_leads,
        total_opportunities=total_opportunities,
        won_opportunities=won_opportunities
    )