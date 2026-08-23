from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from extensions import db
from models import Customer


customer_bp = Blueprint(
    "customer",
    __name__,
    url_prefix="/customers"
)


# =========================================================
# CUSTOMER LIST
# =========================================================

@customer_bp.route("/")
def list_customers():

    customers = Customer.query.order_by(
        Customer.id.desc()
    ).all()

    return render_template(
        "customers/list.html",
        customers=customers
    )


# =========================================================
# ADD CUSTOMER
# =========================================================

@customer_bp.route("/add", methods=["GET", "POST"])
def add_customer():

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

        address = request.form.get(
            "address",
            ""
        ).strip()

        city = request.form.get(
            "city",
            ""
        ).strip()

        state = request.form.get(
            "state",
            ""
        ).strip()

        country = request.form.get(
            "country",
            ""
        ).strip()

        industry = request.form.get(
            "industry",
            ""
        ).strip()

        status = request.form.get(
            "status",
            "Active"
        ).strip()


        # Name validation

        if not name:

            flash(
                "Customer name is required.",
                "error"
            )

            return render_template(
                "customers/add.html"
            )


        customer = Customer(
            name=name,
            company=company,
            email=email,
            phone=phone,
            address=address,
            city=city,
            state=state,
            country=country,
            industry=industry,
            status=status
        )


        db.session.add(customer)
        db.session.commit()


        flash(
            "Customer added successfully.",
            "success"
        )

        return redirect(
            url_for("customer.list_customers")
        )


    return render_template(
        "customers/add.html"
    )


# =========================================================
# CUSTOMER DETAIL
# =========================================================

@customer_bp.route("/<int:customer_id>")
def customer_detail(customer_id):

    customer = Customer.query.get_or_404(
        customer_id
    )

    return render_template(
        "customers/detail.html",
        customer=customer
    )


# =========================================================
# EDIT CUSTOMER
# =========================================================

@customer_bp.route(
    "/<int:customer_id>/edit",
    methods=["GET", "POST"]
)
def edit_customer(customer_id):

    customer = Customer.query.get_or_404(
        customer_id
    )


    if request.method == "POST":

        customer.name = request.form.get(
            "name",
            ""
        ).strip()

        customer.company = request.form.get(
            "company",
            ""
        ).strip()

        customer.email = request.form.get(
            "email",
            ""
        ).strip()

        customer.phone = request.form.get(
            "phone",
            ""
        ).strip()

        customer.address = request.form.get(
            "address",
            ""
        ).strip()

        customer.city = request.form.get(
            "city",
            ""
        ).strip()

        customer.state = request.form.get(
            "state",
            ""
        ).strip()

        customer.country = request.form.get(
            "country",
            ""
        ).strip()

        customer.industry = request.form.get(
            "industry",
            ""
        ).strip()

        customer.status = request.form.get(
            "status",
            "Active"
        ).strip()


        if not customer.name:

            flash(
                "Customer name is required.",
                "error"
            )

            return render_template(
                "customers/edit.html",
                customer=customer
            )


        db.session.commit()


        flash(
            "Customer updated successfully.",
            "success"
        )

        return redirect(
            url_for(
                "customer.customer_detail",
                customer_id=customer.id
            )
        )


    return render_template(
        "customers/edit.html",
        customer=customer
    )


# =========================================================
# DELETE CUSTOMER
# =========================================================

@customer_bp.route(
    "/<int:customer_id>/delete",
    methods=["POST"]
)
def delete_customer(customer_id):

    customer = Customer.query.get_or_404(
        customer_id
    )


    db.session.delete(customer)
    db.session.commit()


    flash(
        "Customer deleted successfully.",
        "success"
    )

    return redirect(
        url_for("customer.list_customers")
    )