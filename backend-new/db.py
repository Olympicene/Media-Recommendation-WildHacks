import sqlite3
from sqlite3 import Error

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
                                     ImageURL TEXT NOT NULL
                                    ); """ 
    try: 
        c = dbConn.cursor()
        c.execute(create_table_sql)
    except Exception as e: 
        print(e)

# Creating media table given connection to a database
def create_pair_table(dbConn): 
    create_table_sql = """ CREATE TABLE IF NOT EXISTS Pairs (
                                     RowID1 INTEGER NOT NULL,
                                     RowID2 INTEGER NOT NULL, 
                                     Timestamp INTEGER NOT NULL,
                                     Score INTEGER NOT NULL,
                                     TotalVotes INTEGER NOT NULL
                                    ); """ 
    try: 
        c = dbConn.cursor()
        c.execute(create_table_sql)
    except Exception as e: 
        print(e)

# Insert row into media table
def add_media(dbConn, Media): 
     
    cursor = dbConn.cursor()
    
    relation_sql = '''INSERT INTO Media (Type, Name, ImageURL)
                      VALUES (?, ?, ?)'''
    
    cursor.execute(relation_sql, [Media['type'], Media['name'], Media['imageURL']])
    dbConn.commit()

# get random media from media table
def random_media(dbConn): 
    cursor = dbConn.cursor()

    in_db_sql = '''SELECT rowid, Type, Name, ImageURL FROM Media
                   ORDER BY random() 
                   LIMIT 1;'''

    cursor.execute(in_db_sql)
    rowid, type, name, imageURL = cursor.fetchone()

    return {
        "rowid": rowid,
        "type": type,  
        "name": name,
        "imageURL": imageURL
    }

# get specific from database
def get_row(dbConn, row): 
    cursor = dbConn.cursor()

    in_db_sql = '''SELECT rowid, Type, Name, ImageURL FROM Media
                   WHERE rowid = ?
                   LIMIT 1;'''

    cursor.execute(in_db_sql, [row])
    rowid, type, name, imageURL = cursor.fetchone()

    return {
        "rowid": rowid,
        "type": type,  
        "name": name,
        "imageURL": imageURL
    }

# Insert row into pair table
def add_pair(dbConn, Pair): 
     
    cursor = dbConn.cursor()
    
    relation_sql = '''INSERT INTO Pairs (RowID1, RowID2, Timestamp, Score, TotalVotes)
                      VALUES (?, ?, ?, ?, ?)'''
    
    cursor.execute(relation_sql, [Pair['rowID1'], Pair['rowID2'], Pair['timestamp'], Pair['score'], Pair['totalVotes']])
    dbConn.commit()

# Check if a pair exists
def pair_exists(dbConn, Pair): 
    cursor = dbConn.cursor()

    in_db_sql = '''SELECT * FROM Pairs WHERE RowID1 = ? AND RowID2 = ?'''

    cursor.execute(in_db_sql, [Pair['rowID1'], Pair['rowID2']])
    lists = cursor.fetchall()

    if lists == None or len(lists) == 0:
        return False
    else: 
        return True 

# upvote
def downvote(dbConn, Pair): 
    update_sql = '''UPDATE Pairs
                    SET 
                    Score = Score - 1 , TotalVotes = TotalVotes + 1
                    WHERE
                    RowID1 = ? AND RowID2 = ?'''
    cursor = dbConn.cursor()
    cursor.execute(update_sql, [Pair['rowID1'], Pair['rowID2']])
    dbConn.commit()

# downvote
def upvote(dbConn, Pair): 
    update_sql = '''UPDATE Pairs
                    SET 
                    Score = Score + 1 , TotalVotes = TotalVotes + 1
                    WHERE
                    RowID1 = ? AND RowID2 = ?'''
    cursor = dbConn.cursor()
    cursor.execute(update_sql, [Pair['rowID1'], Pair['rowID2']])
    dbConn.commit()

# top ten Scores 
def top_ten(dbConn): 
    cursor = dbConn.cursor()

    top_ten_sql = ''' SELECT * FROM Pairs ORDER BY Score LIMIT 10 '''
    cursor.execute(top_ten_sql)

    top_scores = cursor.fetchall()

    list_of_dicts = convert_to_pair_dict(top_scores)
    return list_of_dicts

# top ten TotalVotes
def top_totals(dbConn): 
    cursor = dbConn.cursor()

    top_totals_sql = ''' SELECT * FROM Pairs ORDER BY TotalVotes LIMIT 10 '''
    cursor.execute(top_totals_sql)

    top_votes = cursor.fetchall()

    list_of_dicts = convert_to_pair_dict(top_votes)
    return list_of_dicts

# top ten top_avgs
def top_avgs(dbConn): 
    cursor = dbConn.cursor()

    top_timestamps_sql = ''' SELECT * FROM Pairs ORDER BY TimeStamp LIMIT 10 DESC '''
    cursor.execute(top_timestamps_sql)

    top_timestamps = cursor.fetchall()

    list_of_dicts = convert_to_pair_dict(top_timestamps)
    return list_of_dicts

# converting db tuples to pair dictionaries
def convert_to_pair_dict(pair_tuples): 
    
    pair_dicts = []
    for pair in pair_tuples: 
        pair_dict = { 
                    "rowID1" = pair[0]
                    "rowID2" = pair[1]
                    "ts" = pair[2]
                    "score" = pair[3]
                    "votes" = pair[4]
                    }
        pair_dicts.append(pair_dict)
    return pair_dicts
    


