# # # #
# Created by: Jb Lafon
# On: 22/10/2018
# Description: File for accessing the database
# # # #


import mysql.connector
from datetime import datetime

db = mysql.connector.connect(host='[your_host]',  # TODO: replace with your actual host
                             user='[your_username]',  # TODO: replace with your actual username
                             passwd='[your_password]',  # TODO: replace with your actual password
                             db='[your_database]')  # TODO: replace with your actual database name
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
