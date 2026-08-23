import os
import pandas as pd

from app import app
from models import (
    Customer,
    Lead,
    Opportunity,
    Activity
)


EXPORT_FOLDER = "exports"

os.makedirs(
    EXPORT_FOLDER,
    exist_ok=True
)


def export_sales_data():

    with app.app_context():

        customers = Customer.query.all()
        leads = Lead.query.all()
        opportunities = Opportunity.query.all()
        activities = Activity.query.all()


        customer_data = []

        for customer in customers:

            customer_data.append({
                "Customer ID": customer.id,
                "Name": customer.name,
                "Company": customer.company,
                "Email": customer.email,
                "Phone": customer.phone,
                "Industry": customer.industry,
                "City": customer.city,
                "State": customer.state,
                "Status": customer.status
            })


        lead_data = []

        for lead in leads:

            lead_data.append({
                "Lead ID": lead.id,
                "Name": lead.name,
                "Company": lead.company,
                "Email": lead.email,
                "Source": lead.source,
                "Priority": lead.priority,
                "Estimated Value": lead.estimated_value,
                "Status": lead.status
            })


        opportunity_data = []

        for opportunity in opportunities:

            opportunity_data.append({
                "Opportunity ID": opportunity.id,
                "Name": opportunity.name,
                "Customer ID": opportunity.customer_id,
                "Deal Value": opportunity.deal_value,
                "Probability": opportunity.probability,
                "Stage": opportunity.stage,
                "Status": opportunity.status,
                "Expected Close Date":
                    opportunity.expected_close_date
            })


        activity_data = []

        for activity in activities:

            activity_data.append({
                "Activity ID": activity.id,
                "Activity Type":
                    activity.activity_type,
                "Subject": activity.subject,
                "Customer ID":
                    activity.customer_id,
                "Opportunity ID":
                    activity.opportunity_id,
                "Activity Date":
                    activity.activity_date,
                "Duration Minutes":
                    activity.duration_minutes,
                "Status": activity.status
            })


        file_path = os.path.join(
            EXPORT_FOLDER,
            "sales_data.xlsx"
        )


        with pd.ExcelWriter(
            file_path,
            engine="openpyxl"
        ) as writer:

            pd.DataFrame(
                customer_data
            ).to_excel(
                writer,
                sheet_name="Customers",
                index=False
            )


            pd.DataFrame(
                lead_data
            ).to_excel(
                writer,
                sheet_name="Leads",
                index=False
            )


            pd.DataFrame(
                opportunity_data
            ).to_excel(
                writer,
                sheet_name="Opportunities",
                index=False
            )


            pd.DataFrame(
                activity_data
            ).to_excel(
                writer,
                sheet_name="Activities",
                index=False
            )


        print(
            f"Sales data exported successfully: {file_path}"
        )


if __name__ == "__main__":

    export_sales_data()