import sqlite3

def ConnectToDB(pathtodb):
    try:
        sqliteConnection = sqlite3.connect(pathtodb)
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")

        sqlite_select_Query = "select sqlite_version();"
        cursor.execute(sqlite_select_Query)
        record = cursor.fetchall()
        print("SQLite Database Version is: ", record)

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

    return sqliteConnection 