import sqlite3

def create_db(user_name):
    conn = sqlite3.connect(f"{user_name}.db")

    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE
    IF NOT EXISTS datetime_int (d1 int);''')
