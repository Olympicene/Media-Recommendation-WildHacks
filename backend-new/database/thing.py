import create_db as db
import relation
import sqlite3

def main(): 
    
    database = "media.db"


# Establishing connection to media database
    dbConn = db.create_connection(database)

    if dbConn is not None: 
        db.create_relation_table(dbConn)
        print("success")
    else: 
        print("Error! Can't establish the database connection.")

    cursor = dbConn.cursor()

    cursor.execute("DELETE FROM Relations")

    lists = cursor.fetchall()

    print(lists)

main()