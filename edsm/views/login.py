# ==========
# File : login.py
# Author : Jb
# First created on : 23/10/2018
# Description: Login view
# ==========

from flask import Blueprint, render_template, redirect, url_for, session
from ..forms import EmailPasswordForm
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'

    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False


login_blueprint = Blueprint('login', __name__, template_folder='templates')


@login_blueprint.route('/', methods=["GET", "POST"])
def login():
    form = EmailPasswordForm()
    res=''
    if form.validate_on_submit():
        # Todo: Add action to form after validation
        res = form.email.data
        session['username'] = res
        return redirect(url_for('home.home'))
        # return redirect(url_for('home_blueprint'))
    return render_template('login.html', title='Login', form=form, res=res)
