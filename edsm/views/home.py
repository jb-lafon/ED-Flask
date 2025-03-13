from flask import Blueprint, render_template, session
# from ..util.database import sql_single_request

home_blueprint = Blueprint('home', __name__, template_folder='templates')


@home_blueprint.route('/')
def home():
    sql = "SELECT * FROM edsm.systemswithcoordinates WHERE name='Sol';"
    # result = sql_single_request(sql)
    if 'username' in session:
        return render_template('home.html', title='Home')
    else:
        return "NOT LOGGED IN"


@home_blueprint.route('/home2')
def home2():
    sql = "SELECT * FROM edsm.systemswithcoordinates WHERE name='Sol';"
    # result = sql_single_request(sql)
    return render_template('home2.html', title='Home')