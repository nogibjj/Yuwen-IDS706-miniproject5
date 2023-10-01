import sqlite3

# Function to create a database connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

# Function to create the 'users' table if it doesn't exist
def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
    except sqlite3.Error as e:
        print(e)

# Function to insert a new user into the database
def insert_user(conn, username, email):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)",
                        (username, email))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# Function to retrieve a user by username
def get_user_by_username(conn, username):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(e)

# Function to update a user's email by username
def update_user_email(conn, username, new_email):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET email=? WHERE username=?",
                        (new_email, username))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# Function to delete a user by username
def delete_user(conn, username):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE username=?", (username,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

if __name__ == "__main__":
    database_file = "my_database.db"
    connection = create_connection(database_file)
    if connection:
        create_table(connection)

        # Create a new user
        insert_user(connection, "JohnDoe", "john@example.com")

        # Read a user
        user = get_user_by_username(connection, "JohnDoe")
        if user:
            print("User found:", user)

        # Update user email
        update_user_email(connection, "JohnDoe", "new_email@example.com")

        # Read the updated user
        updated_user = get_user_by_username(connection, "JohnDoe")
        if updated_user:
            print("Updated user:", updated_user)

        # Delete the user
        delete_user(connection, "JohnDoe")

        connection.close()
