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
    
    def select_all(table_name=""):
         return "SELECT * FROM {db}.{t} ".format(db=DBNAME, t=table_name)
         
    
class Systems:
    def __init__(self, ENGINE=Engine().ENGINE):
        self.ENGINE = ENGINE
        self.TABLE = 'systemswithcoordinates'
        return None
    
    def all(self):
        q = "SELECT * FROM {db}.{t}".format(db=DBNAME, t=self.TABLE)
        systems = pd.read_sql_query(q, self.ENGINE)
        return systems
    
    def find_by_name(self, system_name=""):
        q = Engine.select_all(self.TABLE) + "WHERE name='{n}'".format(n=system_name)
        systems = pd.read_sql_query(q, self.ENGINE)
        return systems