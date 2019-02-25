import sqlite3
from secrets import token_hex as token
from time import time


def create_db(user_name):
    """Will create a new database-file for the username specified"""

    # Implement best practise from here: http://www.sqlitetutorial.net/sqlite-python/create-tables/

    # Create connection to database and initiate cursor
    conn = sqlite3.connect(f"{user_name}.db")
    c = conn.cursor()

    # Create task record. This table will be used to keep track of all tasks
    query = 'CREATE TABLE IF NOT EXISTS task_record (task_id text, task_name text);'
    c.execute(query)
    query = 'CREATE TABLE IF NOT EXISTS time_tracked (time_stamp int, task_id text, key text);'
    c.execute(query)
    conn.commit()
    conn.close()


def create_task(user_name, task_name):
    """Creates a new task to keep time for"""
    # Create connection to database and initiate cursor
    conn = sqlite3.connect(f"{user_name}.db")
    c = conn.cursor()

    # Creates unique task id for future referencing.
    # The task-specific table will be named by this
    task_id = token(8)

    # Inserts new task to task_record table
    c.execute("""INSERT INTO task_record (task_id, task_name)
    VALUES (?,?)""", (task_id, task_name))

    conn.commit()
    conn.close()

    return task_id


def start_timer(user_name, task_id):

    conn = sqlite3.connect(f"{user_name}.db")
    c = conn.cursor()

    session_token = token(16)

    c.execute("INSERT INTO time_tracked (time_stamp, task_id, key) VALUES (?,?,?)", (time(), task_id, session_token))

    conn.commit()
    conn.close()

    return session_token


def stop_timer(user_name, task_id, session_token):

    conn = sqlite3.connect(f"{user_name}.db")
    c = conn.cursor()

    c.execute("INSERT INTO time_tracked (time_stamp, task_id, key) VALUES (?,?,?)", (time(), task_id, session_token))

    conn.commit()
    conn.close()


def test_get(user_name, task_id):
    conn = sqlite3.connect(f"{user_name}.db")
    c = conn.cursor()

    c.execute(f"""select * from time_tracked WHERE key = 'e5e95f9a31f0db3fda0fe3d369781426'""")
    output = c.fetchall()

    print(output)

    #print(type(output[0]))