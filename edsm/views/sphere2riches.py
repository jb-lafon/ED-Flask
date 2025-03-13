# ==========
# File : sphere2riches.py
# Author : Jb
# First created on : 24/10/2018
# Description: Sphere2Riches blueprint file
# ==========

from datetime import datetime
from operator import itemgetter
from flask import Blueprint, render_template, request, redirect, url_for
from ..forms import Sphere2RichesForm
from ..util.misc import http_request, urlify, req_value, appstop
from ..util.database import sql_single_request, update_row, db


sphere2riches_blueprint = Blueprint('sphere2riches', __name__, template_folder='templates')


def find_systems(sysName, minRadius, radius, valueLimit = None, maxOutput = None):
    results = []
    api_url = "https://www.edsm.net/api-v1/sphere-systems?systemName=" + urlify(sysName) + "&minRadius=" + str(
        minRadius) + "&radius=" + str(
        radius) + "&showId=1&showCoordinates=1"
    api_data = http_request(api_url).json()
    print("======================================\nSystems Found : " + str(len(api_data)))
    for system in api_data:
        print("======================================")
        sys_dict = {'name': system['name'], 'value': '', 'dist': system['distance'], 'id': system['id']}
        edsm_url = "https://www.edsm.net/en_GB/system/id/" + str(system['id']) + "/name/" + urlify(system['name'])

        # Mark: Check if system is in database
        sql = "SELECT value FROM edsm.systemswithcoordinates WHERE edsm_id=" + str(system['id']) + " LIMIT 10"
        print("Looking for system...")
        sql_req = sql_single_request(sql)
        if sql_req is None:
            sql_req = 0
        else:
            sql_req = list(filter(None, sql_req))
        # Debug: Search Query functional
        # results = str(sql_req)

        # Search found something
        if sql_req:
            value = sql_req[0]
            # Value has been filled & known
            if value > 1:
                print("Value Found !\nID : " + str(system['id']) + " | Value : " + str(sql_req[0]))
                sys_dict['value'] = value
                if valueLimit is not None:
                    if sys_dict['value'] > valueLimit:
                        results.append(sys_dict)
            # Value is empty
            else:
                print("Value not known")
                if req_value(edsm_url) is not None:
                    sys_dict['value'] = req_value(edsm_url)
                    results.append(sys_dict)
                    sql = "UPDATE edsm.systemswithcoordinates SET value=" + str(sys_dict['value']) + \
                          " WHERE edsm_id=" + str(sys_dict['id'])
                    update_row(sql)
                    print(sys_dict)

        # Search found nothing
        else:
            print("System not found in db")
            # No value found in EDSM
            if req_value(edsm_url) is not None:
                print(req_value(edsm_url))
                sys_dict['value'] = int(req_value(edsm_url))
                time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                sql = "REPLACE INTO edsm.systemswithcoordinates SET edsm_id=" + str(sys_dict['id']) + ", name='" + \
                      str(sys_dict["name"]) + "', date='" + time + "', coordX=" + str(system['coords']['x']) + \
                      ", coordY=" + str(system['coords']['y']) + ", coordZ=" + str(system['coords']['z']) + \
                      ", value=" + str(sys_dict['value']) + ";"
                update_row(sql)
                print('New system saved !')
                if valueLimit is not None:
                    if sys_dict['value'] > valueLimit:
                        results.append(sys_dict)
            else:
                time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                sql = "REPLACE INTO edsm.systemswithcoordinates SET edsm_id=" + str(sys_dict['id']) + ", name='" + \
                      str(sys_dict["name"]) + "', date='" + time + "', coordX=" + str(system['coords']['x']) + \
                      ", coordY=" + str(system['coords']['y']) + ", coordZ=" + str(system['coords']['z']) + \
                      ", value=" + str(1) + ";"
                update_row(sql)
                print("Value not known... Value set to 1")
    results = sorted(results, key=itemgetter('value'), reverse=True)
    results = [{'name': 'Name', 'value': 'Value', 'dist': 'Distance'}]+results
    print("\n////////////////////\n===== RESULTS =====")
    return results


@sphere2riches_blueprint.route('/', methods=["GET", "POST"])
def sphere2riches():
    form = Sphere2RichesForm()
    res = ''
    src = ''
    if form.validate_on_submit():
        # Todo: Add action to form after validation
        res = find_systems(form.name.data, form.minRadius.data, form.maxRadius.data, valueLimit=form.valueLimit.data)
        # return redirect(url_for('home_blueprint'))
    return render_template('sphere2riches.html', title='Sphere - 2 - Riches', form=form, res=res, src=src)


@sphere2riches_blueprint.route('/exit', methods=["GET", "POST"])
def appexit():
    appstop()
