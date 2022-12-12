import sqlite3
from sqlite3 import Error


def open_connection(path: str) -> sqlite3.connect:
    """Open Connection to SQLite Database"""

    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB is success")
    except Error as e:
        print(f"The error '{e}' occured")
    
    return connection

def execute_query(connection: sqlite3.connect, query: str, data=None):
    cursor = connection.cursor()
    try:
        if data == None:
            cursor.execute(query)
            connection.commit()
            print("Query is executed")

        else:
            cursor.executemany(query, data)
            connection.commit()
            print("Query is executed")            
    except Error as e:
        print (f"Query failed, the error '{e}' occured")

def create_table(connection):
    create_fruit_table = """
    CREATE TABLE IF NOT EXISTS breweries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        brewery_type TEXT,
        street TEXT,
        city TEXT,
        state TEXT,
        postal_code TEXT,
        country TEXT,
        longitude REAL,
        latitude REAL,
        phone TEXT,
        website_url TEXT
    );
    """

    execute_query(connection, create_fruit_table)

def insert_data(connection: sqlite3.connect, data: list):
    """Inserting Data to database"""

    insert_fruit_query = f"""
    INSERT INTO
        breweries (name, brewery_type, street, city, state, postal_code, country,
                   longitude, latitude, phone, website_url)
    VALUES
        (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    execute_query(connection, insert_fruit_query, data)


if __name__ == "__main__":
    connection = open_connection("fruityvice.db")
    create_table(connection)