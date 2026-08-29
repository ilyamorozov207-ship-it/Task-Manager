import tkinter as tk
from tasks import add_task, delete_task, get_tasks, update_task, toggle_completed

task_ids = []
editing_task_id = None

def add_task_to_gui(entry, listbox):
    task = entry.get()
    result = add_task(task)
    if result:
        task_ids.append(result)
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
    listbox.delete(0, tk.END)
    for task in task_list:
        if task[2] == 1:
            text = "☑ " + task[1]
        else:
            text = "☐ " + task[1]
        task_ids.append(task[0])
        listbox.insert(tk.END, text)

def edit_task_from_gui(entry, listbox):
    global editing_task_id
    selected = listbox.curselection()
    if selected:  
        index = selected[0]
        task_id = task_ids[index]
        editing_task_id = task_id
        task = listbox.get(index)
        entry.delete(0, tk.END)
        entry.insert(0, task)

def save_task_from_gui(entry, listbox):   
    if editing_task_id:
        task = entry.get()
        result = update_task(editing_task_id, task)
        index = task_ids.index(editing_task_id)
        if result:
            listbox.delete(index)
            listbox.insert(index, task)
            entry.delete(0, tk.END)

def toggle_completed_from_gui(listbox):
    selected = listbox.curselection()
    if selected:  
        index = selected[0]
        task_id = task_ids[index]
        completed = toggle_completed(task_id)
        task = listbox.get(index)
        task = task[2:]
        if completed == 1:
            text = "☑ " + task
        else:
            text = "☐ " + task
        listbox.delete(index)
        listbox.insert(index, text)