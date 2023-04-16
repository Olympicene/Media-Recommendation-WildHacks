import sqlite3
import relation
from sqlite3 import Error
import time 

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
    
    relation_sql = '''INSERT INTO Relations (ID_One, Type_One, ID_Two, Type_Two, Score, Total_Votes, Time_Stamp)
                      VALUES (?, ?, ?, ?, ?, ?)'''
    ts = time.time()
    cursor.execute(relation_sql, [Relation.ID_One, Relation.Type_One, Relation.ID_Two, Relation.Type_Two, Relation.Score, Relation.Total_Votes, ts])
    dbConn.commit()
def get_from_db(dbConn, Relation): 
    cursor = dbConn.cursor()

    in_db_sql = '''SELECT * FROM Relations WHERE ID_One = ? AND ID_Two = ?'''

    cursor.execute(in_db_sql, [Relation.ID_One, Relation.ID_Two])
    lists = cursor.fetchall()

    if lists == None or len(lists) == 0:
        create_relation(dbConn, Relation)
        return Relation
    else: 
        return Relation 

def upvote_db(dbConn, Relation): 
    if get_from_db(dbConn, Relation):
        new_score = Relation.Score + 1
        new_total_votes = Relation.Total_Votes + 1  
        update_sql = '''UPDATE Relations 
                        SET Score = ? ,
                        Total_Votes = ?'''
        cursor = dbConn.cursor()
        cursor.execute(update_sql, [new_score, new_total_votes])
    else: 
        print("Relation doesn't exist.")
def downvote_db(dbConn, Relation): 
    if get_from_db(dbConn, Relation): 
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

def convert_to_dict(Relation):
    relationdict = {
                    "id_1": Relation.ID_One,
                    "type_1": Relation.Type_One,
                    "id_2": Relation.ID_Two,
                    "type_2": Relation.Type_Two,
                    "score": Relation.Score,
                    "totalvotes": Relation.Total_Votes
                    }
    
    return relationdict

def convert_to_relation(relationdict):
    relation_obj = relation.Relation(relationdict.get("id_1"), relationdict.get("type_1"), relationdict.get("id_2"), relationdict.get("type_2"), relationdict.get("score"),
                                     relationdict.get("totalvotes"))
    return relation_obj

def top_ten(dbConn):
    dbCursor = dbConn.cursor()

    top_sql = '''SELECT * FROM Relations ORDER BY Time_Stamp LIMIT 10'''

    dbCursor.execute(top_sql)

    top_10 = cursor.fetchall()

    return top_10





        