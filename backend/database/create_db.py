# Creating new DB with new Relation objects and methods to update and add Relations

import sqlite3
import relation
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
def create_relation(dbConn, Relation): 
     
    cursor = dbConn.cursor()
    
    relation_sql = '''INSERT INTO Relations (ID_One, Type_One, ID_Two, Type_Two, Score, Total_Votes)
                      VALUES (?, ?, ?, ?, ?, ?)'''
    cursor.execute(relation_sql, Relation)
    dbConn.commit()
    return None 

# Update a Relation in the Relations database
def update_relation(dbConn, Relation): 

    cursor = dbConn.cursor()

    relation_sql = ''' UPDATE Relations
                       SET Type_One = ? ,  
                           Type_Two = ? , 
                           Score = ? , 
                           Total_Votes = ?
                        WHERE ID_One = ? AND ID_Two = ?'''

    cursor.execute(relation_sql, Relation)
    dbConn.commit()