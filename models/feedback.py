from extensions import db


class Feedback(db.Model):

    __tablename__ = "customer_feedback"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey("customers.id"),
        nullable=False
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey("products.id"),
        nullable=True
    )

    submitted_by = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=True
    )

    feedback_text = db.Column(
        db.Text,
        nullable=False
    )

    feedback_type = db.Column(
        db.String(100),
        nullable=True
    )

    priority = db.Column(
        db.String(30),
        default="Medium"
    )

    status = db.Column(
        db.String(50),
        default="Open"
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    def __repr__(self):

        return f"<Feedback {self.id}>"