from extensions import db


class FeatureRequest(db.Model):
    __tablename__ = "feature_requests"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey("customers.id"),
        nullable=True
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey("products.id"),
        nullable=True
    )

    requested_by = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=True
    )

    title = db.Column(
        db.String(200),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    priority = db.Column(
        db.String(30),
        default="Medium"
    )

    status = db.Column(
        db.String(50),
        default="Requested"
    )

    target_version = db.Column(
        db.String(50),
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now()
    )

    def __repr__(self):
        return f"<FeatureRequest {self.title}>"