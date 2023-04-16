def main(): 
    
    database = "media.db"


    # Establishing connection to media database
    dbConn = db.create_connection(database)

    if dbConn is not None: 
        db.create_relation_table(dbConn)
    else: 
        print("Error! Can't establish the database connection.")