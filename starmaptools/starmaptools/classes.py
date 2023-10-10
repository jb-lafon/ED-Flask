from .config import *

import pandas as pd
import numpy as np
from sqlalchemy import create_engine

#---------------------------------------------------------------------------
# *                           ENGINE
# ?  Main class for connecting to database
# @param hostname string  
# @param dbname string  
# @param uname string  
# @param pwd string  
#---------------------------------------------------------------------------

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
    
    def create_cache(self, dataframe:pd.DataFrame, path="./cached_df_.pkl"):
        dataframe.to_pickle(path)
        return None

    
#---------------------------------------------------------------------------
# *                           SQL QUERY
# ?  Class for performing a simple query
# @param query string  
# @param filter string  
# @param limit integer  
# @param table string 
#---------------------------------------------------------------------------
    
class SQLQuery:
    def __new__(self, query="", filter="", limit=None, ENGINE=Engine().ENGINE, table='systemswithcoordinates'):
        self.ENGINE = ENGINE
        query  = query + "FROM {d}.{t}".format(d=DBNAME, t=table)
        if filter != '':
            query = query + " WHERE {f}".format(f=filter)
        if limit != None:
            query = query + " LIMIT {l}".format(l=limit)
        response = pd.read_sql_query(query, self.ENGINE)
        return response


#---------------------------------------------------------------------------
# *                           SYSTEMS
# ?  Class for queries and filters on systems
#---------------------------------------------------------------------------
         
class Systems:
    def __init__(self, ENGINE=Engine().ENGINE, TABLE='systemswithcoordinates'):
        self.ENGINE = ENGINE
        self.TABLE = TABLE
        return None
    
    #===========================
    # *   all
    # ? Returns all systems
    # @param filter string 
    # @param limit integer
    # @return pd.Dataframe 
    #===========================
    
    def all(self, filter='', limit=None, chunksize=None):
        q = "SELECT * FROM {db}.{t}".format(db=DBNAME, t=self.TABLE)
        if filter != '':
            q = q + " WHERE {f}".format(f=filter)
        if limit != None:
            q = q + " LIMIT {l}".format(l=limit)
        systems = pd.DataFrame()
        if chunksize is not None:
            stream = pd.read_sql_query(q, self.ENGINE, chunksize=chunksize)
            for df in stream:
                systems = df
        systems = pd.read_sql_query(q, self.ENGINE)
        return systems
    
    #===========================
    # *   find_by_name
    # ? Returns systems with corresponding name
    # @param system_name string  
    # @return pd.Dataframe
    #===========================
    
    def find_by_name(self, system_name=""):
        q = Engine.select_all(self.TABLE) + "WHERE name='{n}'".format(n=system_name)
        systems = pd.read_sql_query(q, self.ENGINE)
        return systems
    
    #===========================
    # *   by_value
    # ? Returns systems with corresponding name
    # @param filter string
    # @param limit integer
    # @return pd.Dataframe
    #===========================
    
    def by_value(self, filter="IS NULL", limit=None):
        if limit is not None:
            systems = self.all(filter="`value` {f} {l}".format(f=filter, l=limit))
        else:
            systems = self.all(filter="`value` {f}".format(f=filter))
        return systems

#---------------------------------------------------------------------------
# *                           VALUED SYSTEMS
# ?  A class focusing on systems with values
#---------------------------------------------------------------------------

class ValuedSystems:
    def __new__(self, ENGINE=Engine().ENGINE):
        self.ENGINE = ENGINE
        self.ValuedSystems = Systems().by_value(filter='>1')
        return self.ValuedSystems
