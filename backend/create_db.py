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

    create_relations_table_sql = """ CREATE TABLE IF NOT EXISTS Relations (
                                     ID_One integer NOT NULL,
                                     Type_One text NOT NULL, 
                                     ID_Two integer NOT NULL, 
                                     Type_Two text NOT NULL, 
                                     Score integer NOT NULL, 
                                     Total_Votes integer NOT NULL 
                                    ); """ 

    try: 
        c = dbConn.cursor()
        c.execute(create_relations_table_sql)
    except Error as e: 
        print(e)


# Insert row into media database
def insert_row(dbConn): 
    return None 

# Remove row from media database
def remove_row(dbConn):
    return None 