# ==========
# File : views.py
# Author : Jb
# First created on : 21/11/2018
# Description: Views controller
# ==========

from flask import Blueprint, render_template, redirect, url_for
from .alchemydb.systems_db import value_search
from .DB_upload import upload_json
from .DB_upload7days import upload_7days_json
from .sphere2riches import s2r_function, apiCall
from .waypoints2riches import w2r
from .forms import Sphere2RichesForm
from .util.misc import shutdown_server

from flask_login import current_user, login_user

# Home BP
home_blueprint = Blueprint('home', __name__, template_folder='templates')


# Mark: Home route
@home_blueprint.route('/')
def home():
    return render_template('home.html', title='Home')


# Mark: shutdown route
@home_blueprint.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


# Mark: Login route
@home_blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.home'))
    # form = LoginForm
    # IF form submit:
    #   QUERY user by username
    #   IF NOT password checks && empty:
    #       flash('Invalid username or password')
    #       return redirect(url_for('login'))
    #   login_user(user, remember=form.remember_me.data)
    #   return redirect(url_for('index'))
    # return render_template('login.html', title='Sign In', form=form)


# Upload BP
upload_blueprint = Blueprint('upload', __name__, template_folder='templates')


# Mark: Upload route
@upload_blueprint.route('/')
def upload():
    upload_json()
    return render_template('upload.html', title='Upload')


# # Upload  7days BP
# upload_7days_blueprint = Blueprint('upload7days', __name__, template_folder='templates')
#
#
# # Mark: Upload 7days route
# @upload_7days_blueprint.route('/')
# def upload_7days():
#     upload_7days_json()
#     return render_template('upload7days.html', title='Upload-7-days')


# Value search BP
value_search_blueprint = Blueprint('value_search', __name__, template_folder='templates')


# Mark: Value_search route
@value_search_blueprint.route('/')
def value_searching():
    value_search()
    return render_template('values-search.html', title='Value Search')


# S2R BP
s2r_blueprint = Blueprint('sphere2riches', __name__, template_folder='templates')


# Mark: s2r route
@s2r_blueprint.route('/', methods=["GET", "POST"])
def s2r_page():
    form = Sphere2RichesForm()
    res = ''
    src = ''
    size = ''

    if form.validate_on_submit():
        print('making call')
        api_call = apiCall(form.name.data, form.minRadius.data, form.maxRadius.data)
        print('call done !')
        if api_call['length'] > 0:
            res = s2r_function(
                api_call['data'],
                valueLimit=form.valueLimit.data,
                ignore_unknown=form.ignore_unknown.data,
                ignore_value=form.ignore_value.data,
                check_all=form.check_all.data
            )
        else:
            print('API RESPONSE EMPTY')
    return render_template('sphere2riches.html', title='Sphere-2-Riches', form=form, res=res, src=src)


# W2R BP
w2r_blueprint = Blueprint('waypoints2riches', __name__, template_folder='templates')


# Mark: w2r route
@w2r_blueprint.route('/', methods=["GET", "POST"])
def w2r_page():
    test = w2r('ez aquarii')
    return test
