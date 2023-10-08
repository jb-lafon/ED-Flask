# ==========
# File : forms.py
# Author : Jb
# First created on : 23/10/2018
# Description: File for storing different forms used in the app.
# ==========

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email


class EmailPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class Sphere2RichesForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    minRadius = IntegerField('minRadius', validators=[DataRequired()])
    maxRadius = IntegerField('maxRadius', validators=[DataRequired()])
    valueLimit = IntegerField('valueLimit', validators=[DataRequired()])
    ignore_unknown = BooleanField('Ignore unknown systems')
    ignore_value = BooleanField('Ignore unknown values')
    check_all = BooleanField('Check all systems')
