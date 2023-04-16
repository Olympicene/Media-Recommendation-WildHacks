 and methods to update and add Relations

import sqlite3
import relation
from sqlite3 import Error



# Creating connection to database given
def create_connection(db_file):

    dbConn = None 

    try: 
        dbConn = sqlite3.connect(db_file)
        return dbConn
    except Error as e:
        print(e)

    return dbConn

# Creating Relation table given connection to a database
def create_relation_table(dbConn): 

    create_relations_table_sql = """ CREATE TABLE IF NOT EXISTS Relations (
                                     ID_One INTEGER NOT NULL,
                                     Type_One TEXT NOT NULL, 
                                     ID_Two INTEGER NOT NULL, 
                                     Type_Two TEXT NOT NULL, 
                                     Score INTEGER NOT NULL, 
                                     Total_Votes INTEGER NOT NULL 
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
    cursor.execute(relation_sql, [Relation.ID_One, Relation.Type_One, Relation.ID_Two, Relation.Type_Two, Relation.Score, Relation.Total_Votes])
    dbConn.commit()

def check_if_in_db(dbConn, Relation): 

    cursor = dbConn.cursor()

    in_db_sql = '''SELECT * FROM Relations WHERE ID_One = ? AND ID_Two = ?'''

    cursor.execute(in_db_sql)
    lists = cursor.fetchall()
    print(lists)

    if lists == None or len(lists) == 0:
        create_relation(dbConn, Relation)

def upvote_db(dbConn, Relation): 
    if check_if_in_db(dbConn, Relation): 
        update_sql = '''UPDATE Relations 
                        SET Score = ?
                        Total_Votes = ?'''
    else: 
        print("Relation doesn't exist.")

def downvote_db(): 
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