import sqlite3
from sqlite3 import Error
import time 

# Creating connection to database given
def create_connection(db_file):
    dbConn = None 
    try: 
        dbConn = sqlite3.connect(db_file, check_same_thread=False)
        return dbConn
    except Error as e:
        print(e)
    return dbConn

# Creating media table given connection to a database
def create_media_table(dbConn): 
    create_table_sql = """ CREATE TABLE IF NOT EXISTS Media (
                                     Type TEXT NOT NULL,
                                     Name TEXT NOT NULL, 
                                     ID INTEGER NOT NULL, 
                                     ImageURL TEXT NOT NULL
                                    ); """ 
    try: 
        c = dbConn.cursor()
        c.execute(create_table_sql)
    except Exception as e: 
        print(e)

# Insert row into media database
def add_media(dbConn, Media): 
     
    cursor = dbConn.cursor()
    
    relation_sql = '''INSERT INTO Media (Type, Name, ID, ImageURL)
                      VALUES (?, ?, ?, ?)'''
    
    cursor.execute(relation_sql, [Media['type'], Media['name'], Media['id'], Media['imageURL']])
    dbConn.commit()

# get random media from database
def random_media(dbConn): 
    cursor = dbConn.cursor()

    in_db_sql = '''SELECT Type, Name, ID, ImageURL FROM Media
                   ORDER BY random() 
                   LIMIT 1;'''

    cursor.execute(in_db_sql)
    type, name, id, imageURL = cursor.fetchone()

    return {
        "type": type,  
        "name": name,
        "id": id, 
        "imageURL": imageURL
    }

#def upvote_db(dbConn, Relation): 
#    if get_from_db(dbConn, Relation):
#        new_score = Relation.Score + 1
#        new_total_votes = Relation.Total_Votes + 1  
#        update_sql = '''UPDATE Relations 
#                        SET Score = ? ,
#                        Total_Votes = ?'''
#        cursor = dbConn.cursor()
#        cursor.execute(update_sql, [new_score, new_total_votes])
#    else: 
#        print("Relation doesn't exist.")


#def downvote_db(dbConn, Relation): 
#    if get_from_db(dbConn, Relation): 
#        new_score = Relation.Score - 1
#        new_total_votes = Relation.Total_Votes + 1 
#        update_sql = '''UPDATE Relations 
#                        SET Score = ? ,
#                        Total_Votes = ?'''
#        cursor = dbConn.cursor()
#        cursor.execute(update_sql, [new_score, new_total_votes])
#    else: 
#        print("Relation doesn't exist")

## Update a Relation in the Relations database
#def update_relation(dbConn, Relation): 
#    cursor = dbConn.cursor()
#    relation_sql = ''' UPDATE Relations
#                       SET Type_One = ? ,  
#                           Type_Two = ? , 
#                           Score = ? , 
#                           Total_Votes = ?
#                        WHERE ID_One = ? AND ID_Two = ?'''
#    cursor.execute(relation_sql, Relation)
#    dbConn.commit()

#def convert_to_dict(Relation):
#    relationdict = {
#                    "id_1": Relation.ID_One,
#                    "type_1": Relation.Type_One,
#                    "id_2": Relation.ID_Two,
#                    "type_2": Relation.Type_Two,
#                    "score": Relation.Score,
#                    "totalvotes": Relation.Total_Votes
#                    }
    
#    return relationdict

#def convert_to_relation(relationdict):
#    relation_obj = relation.Relation(relationdict.get("id_1"), relationdict.get("type_1"), relationdict.get("id_2"), relationdict.get("type_2"), relationdict.get("score"),
#                                     relationdict.get("totalvotes"))
#    return relation_obj

#def top_ten(dbConn):
#    dbCursor = dbConn.cursor()

#    top_sql = '''SELECT * FROM Relations ORDER BY Time_Stamp LIMIT 10'''

#    dbCursor.execute(top_sql)

#    top_10 = dbCursor.fetchall()

#    return top_10

#def grab_rand_relation(dbConn): 
#    dbCursor = dbConn.cursor()

#    rand_sql = '''SELECT * FROM Relations ORDER BY RANDOM() LIMIT 1'''

#    dbCursor.execute(rand_sql)

#    rand = dbCursor.fetchall()

#    return rand





        