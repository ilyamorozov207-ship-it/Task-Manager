import tkinter as tk
from tasks import add_task, delete_task, get_tasks

task_ids = []

def add_task_to_gui(entry, listbox):
    task = entry.get()
    result = add_task(task)
    if result:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task_from_gui(listbox):
    selected = listbox.curselection()
    if selected:   
        index = selected[0]
        task_id = task_ids[index]
        delete_task(task_id)
        task_ids.pop(index)
        listbox.delete(index)


def load_tasks(listbox):
    task_list = get_tasks()
    task_ids.clear()
    for task in task_list:
        task_ids.append(task[0])
        listbox.insert(tk.END, task[1])

