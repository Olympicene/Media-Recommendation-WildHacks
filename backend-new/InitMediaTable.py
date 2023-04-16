import db
import sqlite3

def test_create_connection_valid_path():
	db_file = "media.db"
	conn = db.create_connection(db_file)
	print ("Yes sir")

	# Assert
	assert isinstance(conn, sqlite3.Connection)


def test_create_media_table():
	db_file = "media.db"
	conn = db.create_connection(db_file)
	db.create_media_table(conn)
	cursor = conn.cursor()
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Media';")
	result = cursor.fetchone()

	# Assert
	assert result[0] == "Media"

test_create_media_table()


