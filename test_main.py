from main import create_connection, create_table, insert_user, get_user_by_username, update_user_email, delete_user

def test_insert_user():
    database_file = "test_database.db"
    connection = create_connection(database_file)
    create_table(connection)

    insert_user(connection, "AliceSmith", "alice@example.com")
    user = get_user_by_username(connection, "AliceSmith")
    connection.close()

    assert user is not None
    assert user[2] == "alice@example.com"

def test_update_user_email():
    database_file = "test_database.db"
    connection = create_connection(database_file)
    create_table(connection)

    insert_user(connection, "BobJohnson", "bob@example.com")
    update_user_email(connection, "BobJohnson", "new_email@example.com")
    user = get_user_by_username(connection, "BobJohnson")
    connection.close()

    assert user is not None
    assert user[2] == "new_email@example.com"

def test_delete_user():
    database_file = "test_database.db"
    connection = create_connection(database_file)
    create_table(connection)

    insert_user(connection, "CharlieBrown", "charlie@example.com")
    delete_user(connection, "CharlieBrown")
    user = get_user_by_username(connection, "CharlieBrown")
    connection.close()

    assert user is None

if __name__ == "__main__":
    test_insert_user()
    test_update_user_email()
    test_delete_user()
