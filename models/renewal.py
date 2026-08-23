from extensions import db

class Renewal(db.Model):
    __tablename__ = "renewals"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey("customers.id"),
        nullable=False
    )

    contract_name = db.Column(
        db.String(150),
        nullable=False
    )

    renewal_date = db.Column(
        db.Date,
        nullable=False
    )

    contract_value = db.Column(
        db.Float,
        default=0.0
    )

    reminder_days = db.Column(
        db.Integer,
        default=30
    )

    status = db.Column(
        db.String(50),
        default="Active"
    )

    reminder_sent = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    def __repr__(self):
        return f"<Renewal {self.contract_name}>"