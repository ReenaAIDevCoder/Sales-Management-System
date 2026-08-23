from extensions import db

class Campaign(db.Model):
    __tablename__ = "campaigns"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(150),
        nullable=False
    )

    campaign_type = db.Column(
        db.String(100),
        nullable=True
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    start_date = db.Column(
        db.Date,
        nullable=True
    )

    end_date = db.Column(
        db.Date,
        nullable=True
    )

    budget = db.Column(
        db.Float,
        default=0.0
    )

    leads_generated = db.Column(
        db.Integer,
        default=0
    )

    qualified_leads = db.Column(
        db.Integer,
        default=0
    )

    conversions = db.Column(
        db.Integer,
        default=0
    )

    revenue_generated = db.Column(
        db.Float,
        default=0.0
    )

    status = db.Column(
        db.String(50),
        default="Planned"
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    def __repr__(self):
        return f"<Campaign {self.name}>"