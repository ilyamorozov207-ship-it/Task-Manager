import sqlite3

def get_connection():
    return sqlite3.connect("tasks.db")


def get_tasks_from_db():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tasks")
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
    connection.close()

def delete_task_from_db(task_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?",
                   (task_id,))
    connection.commit()
    connection.close()