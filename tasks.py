from database import add_task_to_db, get_tasks_from_db, delete_task_from_db, update_task_in_db, toggle_task_completed

def add_task(task):
    if task:
        return add_task_to_db(task)
    return False


def delete_task(index):
    delete_task_from_db(index)

def get_tasks():
    return get_tasks_from_db()

def update_task(task_id, new_task):
    update_task_in_db(task_id, new_task)
    return True

def toggle_completed(task_id):
    completed = toggle_task_completed(task_id)
    return completed