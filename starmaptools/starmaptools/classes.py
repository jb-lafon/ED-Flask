from .config import *

import pandas as pd
from sqlalchemy import create_engine

class Engine:
    # DEFALUT Credentials to database connection import from _lib.config
    HOSTNAME=HOSTNAME
    DBNAME=DBNAME
    UNAME=UNAME
    PWD=PWD

    def __init__(self, hostname=HOSTNAME, dbname=DBNAME, uname=UNAME, pwd=PWD):

        HOSTNAME=hostname
        DBNAME=dbname
        UNAME=uname
        PWD=pwd

        # Create SQLAlchemy engine to connect to MySQL Database
        self.ENGINE = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                        .format(host=HOSTNAME, db=DBNAME, user=UNAME, pw=PWD))
        
        return None
    
    def set_databases(self, databases={}):
        for (key, value) in databases.items():
            self.__setattr__(key, value)
        return self
    
class SQLQuery:
    def __new__(self, query="", filter="", limit=None, ENGINE=Engine().ENGINE, TABLE='systemswithcoordinates'):
        self.ENGINE = ENGINE
        self.TABLE = TABLE
        query  = query + "FROM {d}.{t}".format(d=DBNAME, t=self.TABLE)
        if filter != '':
            query = query + " WHERE {f}".format(f=filter)
        if limit != None:
            query = query + " LIMIT {l}".format(l=limit)
        response = pd.read_sql_query(query, self.ENGINE)
        return response
         
class Systems:
    def __init__(self, ENGINE=Engine().ENGINE, TABLE='systemswithcoordinates'):
        self.ENGINE = ENGINE
        self.TABLE = TABLE
        return None
    
    def all(self, filter='', limit=None):
        q = "SELECT * FROM {db}.{t}".format(db=DBNAME, t=self.TABLE)
        if filter != '':
            q = q + " WHERE {f}".format(f=filter)
        if limit != None:
            q = q + " LIMIT {l}".format(l=limit)
        systems = pd.read_sql_query(q, self.ENGINE)
        return systems
    
    def find_by_name(self, system_name=""):
        q = Engine.select_all(self.TABLE) + "WHERE name='{n}'".format(n=system_name)
        systems = pd.read_sql_query(q, self.ENGINE)
        return systems