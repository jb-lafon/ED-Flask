# # # #
# Created by: Jb Lafon
# On: 22/10/2018
# Description: File for accessing the database
# # # #

# from sqlalchemy import create_engine, MetaData, Table
#
# engine = create_engine("mysql+mysqlconnector://root:QxZndMdZ3tSA@localhost/edsm")
# metadata = MetaData()
# systemswithcoordinates = Table('systemswithcoordinates', metadata, autoload=True)

import mysql.connector
from datetime import datetime
from app.util.password import hash_password

db = mysql.connector.connect(host='localhost',
                             user='root',
                             passwd='pwBQTd1942dR',
                             db='developmentdb')
cur = db.cursor(buffered=True)


def sql_single_request(query):
    try:
        cur.execute(query)
    except mysql.connector.Error as err:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(time + ' | MYSQL ERROR : {}'.format(err))
    res = cur.fetchone()
    return res


def update_row(sql):
    try:
        print("=======>>> Querying...")
        cur.execute(sql)
        print(" =======>>> Value stored !")
        db.commit()
    except mysql.connector.Error as err:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(time + ' | MYSQL ERROR : {}'.format(err))


def add_user(username, email, password, ed_name):
    sql = 'INSERT INTO edsm.users (username, email, password, ed_name) VALUES ("'+str(username)+'", "'+str(email)+'", "'+hash_password(password)+'", "'+str(ed_name)+'");'
    try:
        cur.execute(sql)
        db.commit()
    except mysql.connector.Error as err:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(time + ' | MYSQL ERROR : {}'.format(err))


def get_user_password(username):
    sql = 'SELECT password FROM edsm.users WHERE username="'+username+'";'
    try:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur.execute(sql)
        print(time + ' | '+'DONE')
    except mysql.connector.Error as err:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(time + ' | MYSQL ERROR : {}'.format(err))
    res = cur.fetchone()
    return res
