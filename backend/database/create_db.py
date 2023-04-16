

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
        return true
    else: 
        return true

def upvote_db(dbConn, Relation): 
    if check_if_in_db(dbConn, Relation):
        new_score = Relation.Score + 1
        new_total_votes = Relation.Total_Votes + 1  
        update_sql = '''UPDATE Relations 
                        SET Score = ? ,
                        Total_Votes = ?'''
        cursor = dbConn.cursor()

        cursor.execute(update_sql, [new_score, new_total_votes])
    else: 
        print("Relation doesn't exist.")

def downvote_db(): 
    if check_if_in_db(dbConn, Relation): 
        new_score = Relation.Score - 1
        new_total_votes = Relation.Total_Votes + 1 
        update_sql = '''UPDATE Relations 
                        SET Score = ? ,
                        Total_Votes = ?'''
        cursor = dbConn.cursor()

        cursor.execute(update_sql, [new_score, new_total_votes])
    else: 
        print("Relation doesn't exist")



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