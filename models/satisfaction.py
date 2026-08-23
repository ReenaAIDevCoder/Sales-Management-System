from extensions import db


class Satisfaction(db.Model):

    __tablename__ = "customer_satisfaction"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey("customers.id"),
        nullable=False
    )

    rating = db.Column(
        db.Float,
        nullable=False
    )

    feedback = db.Column(
        db.Text,
        nullable=True
    )

    survey_date = db.Column(
        db.Date,
        nullable=False
    )

    source = db.Column(
        db.String(100),
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    def __repr__(self):

        return f"<Satisfaction {self.customer_id}>"