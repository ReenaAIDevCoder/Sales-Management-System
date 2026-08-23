from extensions import db

class Activity(db.Model):
    __tablename__ = "activities"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=True
    )

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey("customers.id"),
        nullable=True
    )

    opportunity_id = db.Column(
        db.Integer,
        db.ForeignKey("opportunities.id"),
        nullable=True
    )

    activity_type = db.Column(
        db.String(50),
        nullable=False
    )

    subject = db.Column(
        db.String(200),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    activity_date = db.Column(
        db.DateTime,
        nullable=False
    )

    duration_minutes = db.Column(
        db.Integer,
        nullable=True
    )

    status = db.Column(
        db.String(50),
        default="Completed"
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    def __repr__(self):
        return f"<Activity {self.subject}>"