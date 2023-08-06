"""Models for Blogly."""

"""Demo file showing off a model for SQLAlchemy."""
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"


class User(db.Model):
    """Site User."""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"
    
class Post(db.Model):
    """Blog Post"""

    __tablename__= "posts"

    id         = db.Column(db.Integer, primary_key=True)
    title      = db.Column(db.Text, nullable=False)
    content    = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    user_id    = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @property
    def friendly_date(self):
        """Provide date in an aesthetically-pleasing format."""

        return self.created_at.strftime("%a %b %-d %Y, %-I:%M %p")
    
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


    
    
