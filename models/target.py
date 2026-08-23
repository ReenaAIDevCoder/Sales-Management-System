from extensions import db


class SalesTarget(db.Model):

    __tablename__ = "sales_targets"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=True
    )

    target_period = db.Column(
        db.String(50),
        nullable=False
    )

    target_amount = db.Column(
        db.Float,
        default=0.0
    )

    achieved_amount = db.Column(
        db.Float,
        default=0.0
    )

    start_date = db.Column(
        db.Date,
        nullable=True
    )

    end_date = db.Column(
        db.Date,
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    @property
    def achievement_percentage(self):

        if self.target_amount == 0:
            return 0

        return round(
            (
                self.achieved_amount
                / self.target_amount
            ) * 100,
            2
        )

    def __repr__(self):

        return f"<SalesTarget {self.target_period}>"