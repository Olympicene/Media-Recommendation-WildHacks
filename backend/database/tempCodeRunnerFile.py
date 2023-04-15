def create_relation(dbConn, relation): 
     
    cursor = dbConn.cursor()
    
    relation_sql = '''INSERT INTO Relations (ID_One, Type_One, ID_Two, Type_Two, Score, Total_Votes)
                      VALUES (?, ?, ?, ?, ?, ?)'''
    cur.execute(relation_sql, relation)
    conn.commit()
    return None 