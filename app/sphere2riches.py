# ==========
# File : sphere2riches.py
# Author : Jb
# First created on : 24/10/2018
# Description: Sphere2Riches functions file
# ==========

from .util.misc import urlify, http_request, req_value
from .alchemydb.systems_db import FindSystem, SystemDB
from app import db
from datetime import datetime, timedelta
from operator import itemgetter


def apiCall(sysName, minRadius, radius):
    result={'data': '', 'length': ''}
    api_url = "https://www.edsm.net/api-v1/sphere-systems?systemName=" + urlify(sysName) + "&minRadius=" + str(
        minRadius) + "&radius=" + str(radius) + "&showId=1&showCoordinates=1"
    api_datas = http_request(api_url).json()
    result['data'] = api_datas
    result['length'] = int(len(api_datas))
    return result


def s2r_function(api_data, valueLimit = None, ignore_unknown=False, ignore_value=False, check_all=False):
    results = []                                                                                                        # Create empty result table
    # api_url = "https://www.edsm.net/api-v1/sphere-systems?systemName=" + urlify(sysName) + "&minRadius=" + str(
    #     minRadius) + "&radius=" + str(radius) + "&showId=1&showCoordinates=1"
    # api_data = http_request(api_url).json()

    # Debug number of systems found
    print("======================================\nSystems Found : " + str(len(api_data)))

    system_number = 0
    # Loop in systems found
    for system in api_data:
        system_number = system_number+1
        print("======================================\n"+str(system_number))                                                                 # Debug system start
        sys_dict = {'name': system['name'], 'value': '', 'dist': system['distance'], 'id': system['id']}                # Create empty dict for system
        # print(sys_dict)     # debug
        edsm_url = "https://www.edsm.net/en_GB/system/id/" + str(system['id']) + "/name/" + urlify(system['name'])

        # Mark: Check if system is in database
        # SELECT system WHERE edsm_id = str(system['id'])
        system_req = FindSystem.by_edsm_id(system['id'])

        # Mark: System found in db
        if system_req:
            print('System Found !  |  '+system_req.name)    # debug
            value = system_req.value

            # Value clean filter
            if value is None:
                value = 0

            # Mark: |-> Value is filled or known
            if value > 1:
                print("Value Found !\nID : " + str(system['id']) + " | Value : " + str(value))
                sys_dict['value'] = int(value)

                if check_all is True:
                    last_update_date = system_req.date
                    time_difference = datetime.now() - last_update_date

                    # If system hasn't been checked in over 2 days
                    if time_difference.days > 2:
                        print('=======>>> Value has not been updated in over 2 days')  # debug
                        if not ignore_value:
                            value = req_value(edsm_url)  # Get value form web page
                            # If request successful && value > 0
                            if value is not None:
                                if value > 1 and value != system_req.value:
                                    sys_dict['value'] = int(value)  # Store value in dict
                                    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                    system_req.date = time
                                    system_req.value = value
                                    db.session.commit()  # Store value in db
                                    print('Value added to db !')  # debug
                                    # Check value limit
                                    if valueLimit is not None:
                                        if value >= valueLimit:
                                            results.append(sys_dict)  # Add dict to results
                                    else:
                                        results.append(sys_dict)  # Add dict to results
                                else:
                                    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                    system_req.date = time
                                    db.session.commit()  # Store time in db
                                    print('No value change detected')  # debug

                # Check value limit
                if valueLimit is not None:
                    if value >= valueLimit:
                        results.append(sys_dict)                                                                        # Add dict to results
                else:
                    results.append(sys_dict)                                                                            # Add dict to results
                    print(results)

            # Mark: |-> Value is 1
            elif value == 1:
                if check_all is True:
                    print("Value is 1")

                    last_update_date = system_req.date
                    time_difference = datetime.now() - last_update_date

                    # If system hasn't been checked in over 30mn
                    if time_difference.seconds > 25200:
                        print('=======>>> Value has not been updated in over 30mn')    # debug
                        if not ignore_value:
                            value = req_value(edsm_url)  # Get value form web page
                            # If request successful && value > 0
                            if value is not None:
                                if value > 1:
                                    sys_dict['value'] = int(value)  # Store value in dict
                                    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                    system_req.date = time
                                    system_req.value = value
                                    db.session.commit()  # Store value in db
                                    print('Value added to db !')  # debug
                                    # Check value limit
                                    if valueLimit is not None:
                                        if value >= valueLimit:
                                            results.append(sys_dict)  # Add dict to results
                                    else:
                                        results.append(sys_dict)  # Add dict to results
                                else:
                                    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                    system_req.date = time
                                    db.session.commit()     # Store time in db
                                    print('No value change detected')   # debug
                        elif ignore_value:
                            print('System ignored')

                    print('........................')
                else:
                    print(">>>  Value is 1... skipping\n........................")

            # Mark: |-> Value is empty
            else:
                print("Value not known")
                if not ignore_value:
                    value = req_value(edsm_url)                                                                             # Get value form web page
                    # If request successful && value > 0
                    if value is not None:
                        if value >= 0:
                            sys_dict['value'] = int(value)
                            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            system_req.date = time
                            system_req.value = value
                            db.session.commit()                                                                             # Store value in db
                            print('Value added to db !')    # debug
                            # Check value limit
                            if valueLimit is not None:
                                if value >= valueLimit:
                                    results.append(sys_dict)  # Add dict to results
                            else:
                                results.append(sys_dict)  # Add dict to results
                elif ignore_value:
                    print('System ignored')
        # Mark: System not found in db
        else:
            print("System not found in db")
            if not ignore_unknown:
                value = req_value(edsm_url)

                # Value clean filter
                if value is None:
                    value = 0

                # Mark: |-> If request successful && value > 0
                if value is not None:
                    if value > 0:
                        sys_dict['value'] = int(value)
                        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                        # Insert new system w/ value to db
                        SystemDB.insert_system(sys_dict['id'], sys_dict['name'], time, str(system['coords']['x']), str(system['coords']['y']), str(system['coords']['z']), value=value)
                        print('New system saved !')

                        # Check value limit
                        if valueLimit is not None:
                            if value >= valueLimit:
                                results.append(sys_dict)                                                                    # Add dict to results
                        else:
                            results.append(sys_dict)                                                                        # Add dict to results
                else:
                    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    SystemDB.insert_system(sys_dict['id'], sys_dict['name'], time, str(system['coords']['x']),
                                           str(system['coords']['y']), str(system['coords']['z']), value=1)
                    print("Value not known... Value set to 1")
            elif ignore_unknown:
                print("System ignored")

    results = sorted(results, key=itemgetter('value'), reverse=True)
    results = [{'name': 'Name', 'value': 'Value', 'dist': 'Distance'}]+results
    print("\n////////////////////\n===== RESULTS =====")
    # print(results)
    return results
# from datetime import datetime
# from operator import itemgetter
# from flask import Blueprint, render_template, request, redirect, url_for
# from ..forms import Sphere2RichesForm
# from ..util.misc import http_request, urlify, req_value, appstop
# from ..util.database import sql_single_request, update_row, db
#
#
# sphere2riches_blueprint = Blueprint('sphere2riches', __name__, template_folder='templates')
#
#
# def find_systems(sysName, minRadius, radius, valueLimit = None, maxOutput = None):
#     results = []
#     api_url = "https://www.edsm.net/api-v1/sphere-systems?systemName=" + urlify(sysName) + "&minRadius=" + str(
#         minRadius) + "&radius=" + str(
#         radius) + "&showId=1&showCoordinates=1"
#     api_data = http_request(api_url).json()
#     print("======================================\nSystems Found : " + str(len(api_data)))
#     for system in api_data:
#         print("======================================")
#         sys_dict = {'name': system['name'], 'value': '', 'dist': system['distance'], 'id': system['id']}
#         edsm_url = "https://www.edsm.net/en_GB/system/id/" + str(system['id']) + "/name/" + urlify(system['name'])
#
#         # Mark: Check if system is in database
#         sql = "SELECT value FROM edsm.systemswithcoordinates WHERE edsm_id=" + str(system['id']) + " LIMIT 10"
#         print("Looking for system...")
#         sql_req = sql_single_request(sql)
#         if sql_req is None:
#             sql_req = 0
#         else:
#             sql_req = list(filter(None, sql_req))
#         # Debug: Search Query functional
#         # results = str(sql_req)
#
#         # Search found something
#         if sql_req:
#             value = sql_req[0]
#             # Value has been filled & known
#             if value > 1:
#                 print("Value Found !\nID : " + str(system['id']) + " | Value : " + str(sql_req[0]))
#                 sys_dict['value'] = value
#                 if valueLimit is not None:
#                     if sys_dict['value'] > valueLimit:
#                         results.append(sys_dict)
#             # Value is empty
#             else:
#                 print("Value not known")
#                 if req_value(edsm_url) is not None:
#                     sys_dict['value'] = req_value(edsm_url)
#                     results.append(sys_dict)
#                     sql = "UPDATE edsm.systemswithcoordinates SET value=" + str(sys_dict['value']) + \
#                           " WHERE edsm_id=" + str(sys_dict['id'])
#                     update_row(sql)
#                     print(sys_dict)
#
#         # Search found nothing
#         else:
#             print("System not found in db")
#             # No value found in EDSM
#             if req_value(edsm_url) is not None:
#                 print(req_value(edsm_url))
#                 sys_dict['value'] = int(req_value(edsm_url))
#                 time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                 sql = "REPLACE INTO edsm.systemswithcoordinates SET edsm_id=" + str(sys_dict['id']) + ", name='" + \
#                       str(sys_dict["name"]) + "', date='" + time + "', coordX=" + str(system['coords']['x']) + \
#                       ", coordY=" + str(system['coords']['y']) + ", coordZ=" + str(system['coords']['z']) + \
#                       ", value=" + str(sys_dict['value']) + ";"
#                 update_row(sql)
#                 print('New system saved !')
#                 if valueLimit is not None:
#                     if sys_dict['value'] > valueLimit:
#                         results.append(sys_dict)
#             else:
#                 time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                 sql = "REPLACE INTO edsm.systemswithcoordinates SET edsm_id=" + str(sys_dict['id']) + ", name='" + \
#                       str(sys_dict["name"]) + "', date='" + time + "', coordX=" + str(system['coords']['x']) + \
#                       ", coordY=" + str(system['coords']['y']) + ", coordZ=" + str(system['coords']['z']) + \
#                       ", value=" + str(1) + ";"
#                 update_row(sql)
#                 print("Value not known... Value set to 1")
#     results = sorted(results, key=itemgetter('value'), reverse=True)
#     results = [{'name': 'Name', 'value': 'Value', 'dist': 'Distance'}]+results
#     print("\n////////////////////\n===== RESULTS =====")
#     return results
#
#
# @sphere2riches_blueprint.route('/', methods=["GET", "POST"])
# def sphere2riches():
#     form = Sphere2RichesForm()
#     res = ''
#     src = ''
#     if form.validate_on_submit():
#         # Todo: Add action to form after validation
#         res = find_systems(form.name.data, form.minRadius.data, form.maxRadius.data, valueLimit=form.valueLimit.data)
#         # return redirect(url_for('home_blueprint'))
#     return render_template('sphere2riches.html', title='Sphere - 2 - Riches', form=form, res=res, src=src)
#
#
# @sphere2riches_blueprint.route('/exit', methods=["GET", "POST"])
# def appexit():
#     appstop()
