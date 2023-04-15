db_conn = sqlite3.connect('test_db.db')
relation = Relation(db_conn, "Type1", 1, "Type2", 2, 3.5, 10)
assert relation.Type_One == "Type1"
assert relation.ID_One == 1
assert relation.Type_Two == "Type2"
assert relation.ID_Two == 2
assert relation.Score == 3.5
assert relation.Total_Votes == 1