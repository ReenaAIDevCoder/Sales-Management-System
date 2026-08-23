from extensions import db

class Opportunity(db.Model):
    __tablename__ = "opportunities"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(150),
        nullable=False
    )

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey("customers.id"),
        nullable=True
    )

    assigned_to = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=True
    )

    deal_value = db.Column(
        db.Float,
        default=0.0
    )

    probability = db.Column(
        db.Float,
        default=0.0
    )

    stage = db.Column(
        db.String(50),
        default="Prospecting"
    )

    expected_close_date = db.Column(
        db.Date,
        nullable=True
    )

    status = db.Column(
        db.String(50),
        default="Open"
    )

    notes = db.Column(
        db.Text,
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
        return f"<Opportunity {self.name}>"