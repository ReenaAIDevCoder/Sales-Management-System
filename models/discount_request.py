from extensions import db

class DiscountRequest(db.Model):
    __tablename__ = "discount_requests"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    opportunity_id = db.Column(
        db.Integer,
        db.ForeignKey("opportunities.id"),
        nullable=False
    )

    requested_by = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    discount_percentage = db.Column(
        db.Float,
        nullable=False
    )

    reason = db.Column(
        db.Text,
        nullable=True
    )

    status = db.Column(
        db.String(30),
        default="Pending"
    )

    reviewed_by = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=True
    )

    review_comment = db.Column(
        db.Text,
        nullable=True
    )

    requested_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    reviewed_at = db.Column(
        db.DateTime,
        nullable=True
    )

    def __repr__(self):
        return f"<DiscountRequest {self.id}>"