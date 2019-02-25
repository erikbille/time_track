import db_intract as db


def main():
    # This is a test use case
    # The test will create a new base, start and stop a timer three times
    # and then print all records from the task record table

    db.create_db("test_user")
    test_task_id = db.create_task("test_user", "test_task")
    timer_token = db.start_timer("test_user", test_task_id)
    db.stop_timer("test_user", test_task_id, timer_token)

    timer_token = db.start_timer("test_user", test_task_id)
    db.stop_timer("test_user", test_task_id, timer_token)

    timer_token = db.start_timer("test_user", test_task_id)
    db.stop_timer("test_user", test_task_id, timer_token)

    db.test_get("test_user", test_task_id)

if __name__ == '__main__':
    main()