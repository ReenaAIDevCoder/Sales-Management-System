from extensions import db

class AccountPlan(db.Model):
    __tablename__ = "account_plans"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey("customers.id"),
        nullable=False
    )

    account_manager_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    plan_name = db.Column(
        db.String(150),
        nullable=False
    )

    objectives = db.Column(
        db.Text,
        nullable=True
    )

    strategy = db.Column(
        db.Text,
        nullable=True
    )

    revenue_goal = db.Column(
        db.Float,
        default=0.0
    )

    status = db.Column(
        db.String(50),
        default="Active"
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

    def __repr__(self):
        return f"<AccountPlan {self.plan_name}>"