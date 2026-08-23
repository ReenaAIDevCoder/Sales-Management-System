from extensions import db

class Lead(db.Model):
    __tablename__ = "leads"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(150),
        nullable=False
    )

    company = db.Column(
        db.String(150),
        nullable=True
    )

    email = db.Column(
        db.String(120),
        nullable=True
    )

    phone = db.Column(
        db.String(30),
        nullable=True
    )

    source = db.Column(
        db.String(100),
        nullable=True
    )

    status = db.Column(
        db.String(50),
        default="New"
    )

    priority = db.Column(
        db.String(30),
        default="Medium"
    )

    estimated_value = db.Column(
        db.Float,
        default=0.0
    )

    assigned_to = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
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
        return f"<Lead {self.name}>"