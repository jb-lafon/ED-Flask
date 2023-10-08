# ==========
# File : DB_upload.py
# Author : Jb
# First created on : 23/11/2018
# Description: JSON upload function
# ==========

import ijson
from datetime import datetime
from .alchemydb.systems_db import SystemDB


def upload_7days_json(json_file='../EDSM-Dumps/2018_12_11/systemsWithCoordinates7days.json'):
    i = 0
    resume = 1
    line = {'id': 0, 'name': '', 'coordX': '', 'coordY': '', 'coordZ': ''}
    parser = ijson.parse(open(json_file))
    for prefix, event, value in parser:
        # mysq DEBUG - ijson parser
        # print('Prefix: ' + str(prefix))
        # print('Event: ' + str(event))
        # print('Value: ' + str(value) + '\n')
        if resume == 1:
            if prefix.endswith('.id'):
                line['id'] = value
            if prefix.endswith('.name'):
                line['name'] = str(value)
            if prefix.endswith('.coords.x'):
                line['coordX'] = value
            if prefix.endswith('.coords.y'):
                line['coordY'] = value
            if prefix.endswith('.coords.z'):
                line['coordZ'] = value
                time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # val = (line['id'], line['name'], time, line['coordX'], line['coordY'], line['coordZ'])
                # TODO-jb: DO SQLAlchemy INSERT
                SystemDB.insert_system(line['id'], line['name'], time, line['coordX'], line['coordY'], line['coordZ'])

        if resume == 0:
            if prefix.endswith('.id') and value == 0:     # Last successful entry
                resume = 1
            elif prefix.endswith('.id'):
                time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(time+' | IGNORED RECORD - ID : '+str(value))
