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

    #c.execute(f"""select datetime(time_stamp,'unixepoch') from time_tracked """)
    #output = c.fetchall()

    c.execute(f"""select * from time_tracked """)
    output = c.fetchall()

    duration = output[1][0] - output[0][0]

    print(output)
    print(duration)

    c.execute(f"""select * from task_record """)
    output = c.fetchall()


    print(output)
    conn.commit()
    conn.close()

    #print(type(output[0]))