"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connects to the database."""
    db.app = app
    db.init_app(app)

class User(db.Model):
    """User model."""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String, nullable=True, default=None)

    def get_full_name(self):
        """Return the full name of the user."""
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        """Return the full name of the user as a property."""
        return self.get_full_name()
