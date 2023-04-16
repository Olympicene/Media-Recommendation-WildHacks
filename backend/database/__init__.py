import create_db


def main(): 
    
    database = "media.db"


# Establishing connection to media database
dbConn = create_connection(database)

if dbConn is not None: 
    create_relation_table(dbConn)
else: 
    print("Error! Can't establish the database connection.")

