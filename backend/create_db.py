# Creating new DB with new Relation objects

import sqlite3
import Relation.py
from sqlite3 import Error

# Creating connection to database given
def create_connection(db_file):

    dbConn == None 

    try: 
        dbConn = sqlite3.connect(db_file)
        return dbConn
    except Error as e:
        print(e)

    return dbConn

# Creating Relation table given connection to a database
def create_relation_table(dbConn): 

    sql_create_relations_table = """ CREATE TABLE IF NOT EXISTS Relations (
                                     id 

    )"""

