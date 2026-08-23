from flask import Blueprint, render_template
from extensions import db
from models import (
    Product,
    Feedback,
    FeatureRequest
)


product_bp = Blueprint(
    "product",
    __name__,
    url_prefix="/products"
)


@product_bp.route("/")
def products():

    products = Product.query.order_by(
        Product.id.desc()
    ).all()

    active_products = sum(
        1
        for product in products
        if product.status == "Active"
    )

    inactive_products = len(products) - active_products

    return render_template(
        "products/products.html",
        products=products,
        active_products=active_products,
        inactive_products=inactive_products
    )


@product_bp.route("/roadmap")
def roadmap():

    roadmap_items = []

    return render_template(
        "products/roadmap.html",
        roadmap_items=roadmap_items,
        planned_items=0,
        in_progress_items=0,
        completed_items=0
    )


@product_bp.route("/feedback")
def feedback():

    feedback_list = Feedback.query.order_by(
        Feedback.id.desc()
    ).all()

    if feedback_list:

        average_rating = sum(
            feedback.rating or 0
            for feedback in feedback_list
        ) / len(feedback_list)

    else:

        average_rating = 0

    return render_template(
        "products/feedback.html",
        feedback_list=feedback_list,
        average_rating=average_rating
    )


@product_bp.route("/documentation")
def documentation():

    documents = []

    return render_template(
        "products/documentation.html",
        documents=documents
    )


@product_bp.route("/feature-requests")
def feature_requests():

    feature_requests = FeatureRequest.query.order_by(
        FeatureRequest.id.desc()
    ).all()

    pending_requests = sum(
        1
        for request in feature_requests
        if request.status == "Pending"
    )

    in_progress_requests = sum(
        1
        for request in feature_requests
        if request.status == "In Progress"
    )

    completed_requests = sum(
        1
        for request in feature_requests
        if request.status == "Completed"
    )

    return render_template(
        "products/feature_requests.html",
        feature_requests=feature_requests,
        pending_requests=pending_requests,
        in_progress_requests=in_progress_requests,
        completed_requests=completed_requests
    )