import sqlite3

def get_connection():
    return sqlite3.connect("tasks.db")


def get_tasks_from_db():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, task, completed FROM tasks")
    result = cursor.fetchall()
    connection.close()
    return result


def add_task_to_db(task):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (?)",
                   (task,)
                   )
    connection.commit()
    task_id = cursor.lastrowid
    connection.close()
    return task_id

def delete_task_from_db(task_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?",
                   (task_id,))
    connection.commit()
    
    connection.close()

def update_task_in_db(task_id, new_task):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE tasks SET task = ? WHERE id = ?",
        (new_task, task_id,))
    connection.commit()
    connection.close()

def toggle_task_completed(task_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE tasks SET completed = 1 - completed WHERE id = ?",
                   (task_id,))
    cursor.execute("SELECT completed FROM tasks WHERE id = ?",
                   (task_id,))
    result = cursor.fetchone()
    connection.commit()
    connection.close()
    return result[0]
