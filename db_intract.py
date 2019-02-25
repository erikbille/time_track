import sqlite3
from secrets import token_urlsafe as token


def create_db(user_name):
    conn = sqlite3.connect(f"{user_name}.db")

    c = conn.cursor()

    # Create task record
    c.execute('''CREATE TABLE
    IF NOT EXISTS task_record (task_id text, task_name text);''')

    conn.commit()

    conn.close()


def create_task(user_name, task_name):
    conn = sqlite3.connect(f"{user_name}.db")
    c = conn.cursor()

    task_id = token(16)

    # Create table
    c.execute(f'''CREATE TABLE
    IF NOT EXISTS {task_id} (time_stamp int, key int);''')

    conn.commit()

    c.execute(f"""INSERT INTO task_record (task_id, task_name)
    VALUES
    ("{task_id}","{task_name}");""")

    conn.commit()
    conn.close()

    return task_id


def start_timer(user_name, task_id):

    conn = sqlite3.connect(f"{user_name}.db")

    c = conn.cursor()

    session_token = token(8)

    c.execute(f"""INSERT INTO {task_id} (time_stamp, key)
    VALUES
    (("strftime('%s','now')")("{session_token}"));""")

    conn.commit()
    conn.close()

    return session_token


def stop_timer(user_name, task_id, token):

    conn = sqlite3.connect(f"{user_name}.db")

    c = conn.cursor()

    c.execute(f"""INSERT INTO {task_id} (time_stamp, key)
    VALUES
    ((strftime('%s','now'))("{token})");""")

    conn.commit()
    conn.close()


def test_get(user_name, task_id):
    conn = sqlite3.connect(f"{user_name}.db")
    c = conn.cursor()

    c.execute(f"""select * from task_record""")
    print(c.fetchall())
