# ==========
# File : models.py
# Author : Jb
# First created on : 21/11/2018
# Description: SQLAlchemy database models
# ==========

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


# Mark: User model
class User(UserMixin, db.Model):
    """
    Create a User table
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, nullable=False, unique=True, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), index=True, unique=True)
    password_hash = db.Column(db.String(128), index=True)
    ed_name = db.Column(db.String(255), index=True)

    @property
    def password(self):
        """
        Prevent password access
        """
        raise AttributeError('password is not readable')

    @password.setter
    def password(self, password):
        """
        Hash password
        """
        self.password_hash = generate_password_hash(password)    # Generate password hash here

    def verify_password(self, password):
        """
        Verify hash with string
        """
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        """True, as all users are active."""
        return True

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def get_id(self):
        """return unicode(self.id)"""
        return self.id

    def __repr__(self):
        return '<User: {}>'.format(self.username)


# Mark: user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Mark: SystemWithCoordinates model
class SystemWithCoordinates(db.Model):
    """
    Create a User table
    """

    __tablename__ = 'systemswithcoordimates'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, index=True, unique=True)
    edsm_id = db.Column(db.Integer, index=True, nullable=False)
    name = db.Column(db.String(255), index=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    coordX = db.Column(db.Float, nullable=False)
    coordY = db.Column(db.Float, nullable=False)
    coordZ = db.Column(db.Float, nullable=False)
    value = db.Column(db.Integer, index=True, nullable=True)
    last_visit = db.Column(db.DateTime, index=True, nullable=True)

    # def __repr__(self):
    #     return '<System with coordinates: {}>'.format(self)
