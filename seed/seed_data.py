from datetime import date, datetime, timedelta

from werkzeug.security import generate_password_hash

from app import app
from extensions import db

from models import (
    User,
    Customer,
    Lead,
    Opportunity,
    Activity,
    SalesTarget,
    Product,
    Campaign,
    Territory,
)


# =========================================================
# CLEAR EXISTING DATA
# =========================================================

def clear_existing_data():

    print("Clearing existing sample data...")

    # Delete dependent records first
    Activity.query.delete()
    Opportunity.query.delete()
    Lead.query.delete()
    SalesTarget.query.delete()
    Campaign.query.delete()
    Territory.query.delete()
    Product.query.delete()
    Customer.query.delete()
    User.query.delete()

    db.session.commit()

    print("Existing data cleared.")


# =========================================================
# CREATE USERS
# =========================================================

def create_users():

    default_password = generate_password_hash(
        "password123"
    )

    users = [

        User(
            name="Amit Sharma",
            email="amit@example.com",
            password=generate_password_hash("amit@123"),
            role="Sales Representative",
            region="North",
            is_active=True
        ),

        User(
            name="Priya Singh",
            email="priya@example.com",
            password=generate_password_hash("priya@123"),
            role="Sales Manager",
            region="North",
            is_active=True
        ),

        User(
            name="Rahul Verma",
            email="rahul@example.com",
            password=generate_password_hash("rahul@123"),
            role="Account Manager",
            region="West",
            is_active=True
        ),

        User(
            name="Neha Gupta",
            email="neha@example.com",
            password=default_password,
            role="Marketing",
            region="South",
            is_active=True
        ),

        User(
            name="Vikram Patel",
            email="vikram@example.com",
            password=default_password,
            role="Product Manager",
            region="West",
            is_active=True
        ),

        User(
            name="Anil Mehta",
            email="anil@example.com",
            password=default_password,
            role="Executive",
            region="All",
            is_active=True
        ),

    ]

    db.session.add_all(users)
    db.session.commit()

    print("Users created.")

    return users


# =========================================================
# CREATE CUSTOMERS
# =========================================================

def create_customers(users):

    sales_rep = next(
        user for user in users
        if user.role == "Sales Representative"
    )

    customers = [

        Customer(
            name="Rajesh Kumar",
            company="Tech Solutions Pvt Ltd",
            email="rajesh@techsolutions.com",
            phone="9876543210",
            city="Indore",
            state="Madhya Pradesh",
            country="India",
            industry="Technology",
            status="Active",
            assigned_to=sales_rep.id
        ),

        Customer(
            name="Sneha Sharma",
            company="Global Retail Ltd",
            email="sneha@globalretail.com",
            phone="9876501234",
            city="Bhopal",
            state="Madhya Pradesh",
            country="India",
            industry="Retail",
            status="Active",
            assigned_to=sales_rep.id
        ),

        Customer(
            name="Arjun Patel",
            company="Finance Hub",
            email="arjun@financehub.com",
            phone="9123456789",
            city="Mumbai",
            state="Maharashtra",
            country="India",
            industry="Finance",
            status="Active",
            assigned_to=sales_rep.id
        ),

    ]

    db.session.add_all(customers)
    db.session.commit()

    print("Customers created.")

    return customers


# =========================================================
# CREATE LEADS
# =========================================================

def create_leads(users):

    sales_rep = next(
        user for user in users
        if user.role == "Sales Representative"
    )

    leads = [

        Lead(
            name="Karan Malhotra",
            company="Digital World",
            email="karan@digitalworld.com",
            phone="9876123456",
            source="Website",
            status="New",
            priority="High",
            estimated_value=150000,
            assigned_to=sales_rep.id
        ),

        Lead(
            name="Pooja Jain",
            company="Smart Enterprises",
            email="pooja@smartenterprises.com",
            phone="9812345678",
            source="Campaign",
            status="Qualified",
            priority="Medium",
            estimated_value=250000,
            assigned_to=sales_rep.id
        ),

    ]

    db.session.add_all(leads)
    db.session.commit()

    print("Leads created.")

    return leads


# =========================================================
# CREATE OPPORTUNITIES
# =========================================================

def create_opportunities(users, customers):

    sales_rep = next(
        user for user in users
        if user.role == "Sales Representative"
    )

    opportunities = [

        Opportunity(
            name="CRM Pro Implementation",
            customer_id=customers[0].id,
            assigned_to=sales_rep.id,
            deal_value=500000,
            probability=80,
            stage="Proposal",
            expected_close_date=(
                date.today() + timedelta(days=20)
            ),
            status="Open",
            notes="CRM implementation opportunity."
        ),

        Opportunity(
            name="Analytics Platform Deal",
            customer_id=customers[1].id,
            assigned_to=sales_rep.id,
            deal_value=350000,
            probability=60,
            stage="Negotiation",
            expected_close_date=(
                date.today() + timedelta(days=35)
            ),
            status="Open",
            notes="Analytics platform negotiation."
        ),

        Opportunity(
            name="Finance CRM Upgrade",
            customer_id=customers[2].id,
            assigned_to=sales_rep.id,
            deal_value=450000,
            probability=100,
            stage="Closed Won",
            expected_close_date=(
                date.today() - timedelta(days=5)
            ),
            status="Won",
            notes="Successfully closed deal."
        ),

    ]

    db.session.add_all(opportunities)
    db.session.commit()

    print("Opportunities created.")

    return opportunities


# =========================================================
# CREATE ACTIVITIES
# =========================================================

def create_activities(
    users,
    customers,
    opportunities
):

    sales_rep = next(
        user for user in users
        if user.role == "Sales Representative"
    )

    activities = [

        Activity(
            user_id=sales_rep.id,
            customer_id=customers[0].id,
            opportunity_id=opportunities[0].id,
            activity_type="Meeting",
            subject="CRM Requirement Discussion",
            description=(
                "Discussed CRM implementation requirements."
            ),
            activity_date=datetime.now(),
            duration_minutes=60,
            status="Completed"
        ),

        Activity(
            user_id=sales_rep.id,
            customer_id=customers[1].id,
            opportunity_id=opportunities[1].id,
            activity_type="Call",
            subject="Sales Follow-up",
            description=(
                "Followed up regarding analytics proposal."
            ),
            activity_date=datetime.now(),
            duration_minutes=30,
            status="Completed"
        ),

    ]

    db.session.add_all(activities)
    db.session.commit()

    print("Activities created.")

    return activities


# =========================================================
# CREATE SALES TARGET
# =========================================================

def create_targets(users):

    sales_rep = next(
        user for user in users
        if user.role == "Sales Representative"
    )

    target = SalesTarget(

        user_id=sales_rep.id,

        target_period="2026 - Q3",

        target_amount=1500000,

        achieved_amount=450000,

        start_date=date(2026, 7, 1),

        end_date=date(2026, 9, 30)

    )

    db.session.add(target)
    db.session.commit()

    print("Sales target created.")

    return target


# =========================================================
# CREATE PRODUCTS
# =========================================================

def create_products():

    products = [

        Product(
            name="CRM Pro",
            product_code="CRM-001",
            description=(
                "Customer relationship management solution."
            ),
            category="Software",
            price=50000,
            version="2.0",
            roadmap_status="Active"
        ),

        Product(
            name="Sales Analytics",
            product_code="SA-001",
            description=(
                "Sales analytics and reporting platform."
            ),
            category="Analytics",
            price=75000,
            version="1.5",
            roadmap_status="Active"
        ),

        Product(
            name="Enterprise Suite",
            product_code="ENT-001",
            description=(
                "Enterprise sales management solution."
            ),
            category="Enterprise",
            price=150000,
            version="1.0",
            roadmap_status="Planned"
        ),

    ]

    db.session.add_all(products)
    db.session.commit()

    print("Products created.")

    return products


# =========================================================
# CREATE CAMPAIGNS
# =========================================================

def create_campaigns():

    campaigns = [

        Campaign(
            name="Summer Sales Campaign",
            campaign_type="Digital Marketing",
            description="Summer promotional campaign.",
            start_date=(
                date.today() - timedelta(days=30)
            ),
            end_date=(
                date.today() + timedelta(days=30)
            ),
            budget=200000,
            leads_generated=120,
            qualified_leads=65,
            conversions=15,
            revenue_generated=500000,
            status="Active"
        ),

        Campaign(
            name="Enterprise Lead Generation",
            campaign_type="B2B",
            description=(
                "Enterprise customer acquisition campaign."
            ),
            start_date=date.today(),
            end_date=(
                date.today() + timedelta(days=60)
            ),
            budget=300000,
            leads_generated=80,
            qualified_leads=40,
            conversions=8,
            revenue_generated=350000,
            status="Active"
        ),

    ]

    db.session.add_all(campaigns)
    db.session.commit()

    print("Campaigns created.")

    return campaigns


# =========================================================
# CREATE TERRITORIES
# =========================================================

def create_territories(users):

    manager = next(
        user for user in users
        if user.role == "Sales Manager"
    )

    sales_rep = next(
        user for user in users
        if user.role == "Sales Representative"
    )

    territories = [

        Territory(
            name="Central India",
            region="Central",
            description=(
                "Central India sales territory."
            ),
            manager_id=manager.id,
            assigned_rep_id=sales_rep.id,
            is_active=True
        ),

        Territory(
            name="West India",
            region="West",
            description=(
                "West India sales territory."
            ),
            manager_id=manager.id,
            assigned_rep_id=sales_rep.id,
            is_active=True
        ),

    ]

    db.session.add_all(territories)
    db.session.commit()

    print("Territories created.")

    return territories


# =========================================================
# MAIN SEED FUNCTION
# =========================================================

def seed_database():

    with app.app_context():

        print()
        print("=" * 60)
        print("STARTING DATABASE SEEDING")
        print("=" * 60)

        # Create tables
        db.create_all()

        # Remove old sample data
        clear_existing_data()

        # Create users
        users = create_users()

        # Create customers
        customers = create_customers(users)

        # Create leads
        create_leads(users)

        # Create opportunities
        opportunities = create_opportunities(
            users,
            customers
        )

        # Create activities
        create_activities(
            users,
            customers,
            opportunities
        )

        # Create sales targets
        create_targets(users)

        # Create products
        create_products()

        # Create campaigns
        create_campaigns()

        # Create territories
        create_territories(users)

        print()
        print("=" * 60)
        print("DATABASE SEEDING COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        print()
        print("LOGIN CREDENTIALS")
        print("-" * 60)
        print("Email    : amit@example.com")
        print("Password : password123")
        print()
        print("Other users also use password: password123")
        print("=" * 60)


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":
    seed_database()