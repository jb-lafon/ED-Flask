# ==========
# File : aldb.py
# Author : Jb
# First created on : 23/11/2018
# Description: For systems database
# ==========

from app import db
from ..models import SystemWithCoordinates
from ..util.misc import urlify, http_request, Pq, find_whole_word
import re
from sqlalchemy import func, update


class FindSystem:
    @staticmethod
    def by_id(id_val):
        system = SystemWithCoordinates.query.filter_by(id=id_val).first()
        return system

    @staticmethod
    def by_name(name_val=''):
        system = SystemWithCoordinates.query.filter_by(name=name_val).first()
        return system

    @staticmethod
    def by_edsm_id(edsm_id_val):
        system = SystemWithCoordinates.query.filter_by(edsm_id=edsm_id_val).first()
        return system


class SystemDB:
    # TODO-jb: Insert new system
    @staticmethod
    def insert_system(edsm_id, name, date, coordX, coordY, coordZ, value=None):
        if value is not None:
            system = SystemWithCoordinates(edsm_id=edsm_id, name=name, date=date, coordX=coordX, coordY=coordY,
                                           coordZ=coordZ, value=value)
        else:
            system = SystemWithCoordinates(edsm_id=edsm_id, name=name, date=date, coordX=coordX, coordY=coordY,
                                           coordZ=coordZ)
        print("==========\n|--> NAME: " + name + "\n|--> ID: " + str(edsm_id))
        db.session.add(system)
        print("|--> ADDED...")
        db.session.commit()
        print("|--> DONE!")

# TODO-jb: Insert value to system
# TODO-jb: Fill empty values with 1 (after web check)
# TODO-jb: Update value
# TODO-jb: Update coordinates


def value_search():
    db_count = db.session.query(func.count(SystemWithCoordinates.id)).scalar()        # Get count from table
    print(db_count)
    i = 32000   # Start id

    while i <= db_count:
        system = FindSystem.by_id(i)         # SELECT a system WHERE id=...
        if system:          # If system is found
            system_name = system.name  # Store name
            system_id = system.edsm_id  # Store Id
            print('---- SYSTEM ' + system.name + ' -----')
            if system.value is None:      # If system value is empty in database
                print("---- VALUE EMPTY ----")
                edsm_url = "https://www.edsm.net/en_GB/system/id/" + str(system_id) + "/name/" + urlify(system_name)
                edsm_page = http_request(edsm_url).text     # Get EDSM HTML web-page in text
                d = Pq(edsm_page)                           # parse page with PyQuery
                # Select correct HTML bloc
                bloc = str(d("div.card>div.card-body>p:last-of-type>strong"))
                bloc = str(re.sub('&#13;', '', str(bloc)))
                bloc = str(re.sub('\n', '', bloc))

                # Find & store value in dictionary
                if find_whole_word('estimated')(bloc):      # If "estimated" found in bloc :
                    bloc = re.findall('(\d+)', bloc)            # Regex to select only digits
                    bloc = ''.join(bloc)                        # Join regex result to string
                    value = int(bloc)                           # Convert value to integer
                    # UPDATE row to set value
                    system.value = value
                    db.session.commit()
                else:                                       # "estimated" not found
                    print("ID " + str(i) + " | No value found")
                    # UPDATE row to set value to 1 (checked but no value)
                    system.value = 1
                    db.session.commit()
            else:           # Else value is found in database
                if system.value == 0:
                    # UPDATE row to set value to 1 (checked but no value)
                    system.value = 1
                    db.session.commit()
                    print("Value set to 1")
                else:
                    print("ID " + str(i) + " | Already checked")
        elif system is None:                           # Else system not found
            db_count = db_count+1           # Increase db_count to accommodate for skipped system
        i = i+1    # iterate
