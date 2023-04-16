''' Test cases for the create_db and relation files. '''

import relation
import create_db

def test_create_connection_valid_path():
    # Arrange
    db_file = "media.db"

    # Act
    conn = create_connection(db_file)
    print ("Yes sir")
    # Assert
    assert isinstance(conn, sqlite3.Connection)

def test_create_connection_invalid_path():
    # Arrange
    db_file = "invalid_db.db"

    # Act
    conn = create_connection(db_file)

    # Assert
    assert conn is None

def test_create_relation_table_valid_connection():
    # Arrange
    conn = sqlite3.connect(":memory:")

    # Act
    create_relation_table(conn)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Relations';")
    result = cursor.fetchone()

    # Assert
    assert result[0] == "Relations"

def test_create_relation_table_invalid_connection():
    # Arrange
    conn = None

    # Act
    create_relation_table(conn)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Relations';")
    result = cursor.fetchone()

    # Assert
    assert result is None

def test_create_relation_valid_data():
    # Arrange
    conn = sqlite3.connect(":memory:")
    create_relation_table(conn)
    relation = (1, "Type1", 2, "Type2", 3.5, 10)

    # Act
    create_relation(conn, relation)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Relations;")
    result = cursor.fetchone()

    # Assert
    assert result == relation

def test_create_relation_invalid_data():
    # Arrange
    conn = sqlite3.connect(":memory:")
    create_relation_table(conn)
    relation = (1, "Type1", 2, "Type2")  # missing Score and Total_Votes

    # Act/Assert
    with pytest.raises(sqlite3.IntegrityError):
        create_relation(conn, relation)

def test_create_relation():
    dbConn = sqlite3.connect("test_database.db")
    relation_data = (1, "Person", 2, "Movie", 8.5, 100)
    create_relation(dbConn, relation_data)
    cursor = dbConn.cursor()
    cursor.execute("SELECT * FROM Relations WHERE ID_One=1 AND ID_Two=2")
    result = cursor.fetchone()
    assert result == (1, "Person", 2, "Movie", 8.5, 100)


