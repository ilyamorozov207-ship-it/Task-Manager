from database import add_task_to_db, get_tasks_from_db, delete_task_from_db

def add_task(task):
    if task:
        add_task_to_db(task)
        return True
    return False


def delete_task(index):
    delete_task_from_db(index)

def get_tasks():
    return get_tasks_from_db()