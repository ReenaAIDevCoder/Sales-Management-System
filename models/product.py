from extensions import db

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(150),
        nullable=False
    )

    product_code = db.Column(
        db.String(100),
        unique=True,
        nullable=True
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    category = db.Column(
        db.String(100),
        nullable=True
    )

    price = db.Column(
        db.Float,
        default=0.0
    )

    version = db.Column(
        db.String(50),
        nullable=True
    )

    roadmap_status = db.Column(
        db.String(100),
        default="Planned"
    )

    documentation_url = db.Column(
        db.String(255),
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

    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now()
    )

    def __repr__(self):
        return f"<Product {self.name}>"