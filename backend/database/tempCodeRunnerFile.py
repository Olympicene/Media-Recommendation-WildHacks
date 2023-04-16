def test_create_connection_valid_path():
    # Arrange
    db_file = "test_db.db"

    # Act
    conn = create_connection(db_file)

    # Assert
    assert isinstance(conn, sqlite3.Connection)