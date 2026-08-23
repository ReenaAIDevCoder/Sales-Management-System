from extensions import db

class Territory(db.Model):
    __tablename__ = "territories"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(150),
        nullable=False,
        unique=True
    )

    region = db.Column(
        db.String(100),
        nullable=True
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    manager_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=True
    )

    assigned_rep_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=True
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    def __repr__(self):
        return f"<Territory {self.name}>"