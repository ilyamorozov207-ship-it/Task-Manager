import tkinter as tk
from gui import add_task_to_gui, delete_task_from_gui, load_tasks

#Переменные
window = tk.Tk()
entry = tk.Entry(window)
listbox = tk.Listbox(window)

#КОД
window.title("Task Menager")
window.geometry("500x400")
button = tk.Button(
    window,
    text='Добавить задачу',
    command=lambda: add_task_to_gui(entry, listbox),
)
delete_button = tk.Button(
    window,
    text='Удалить задачу',
    command=lambda: delete_task_from_gui(listbox)
)

#Вызов
entry.pack()
button.pack()
delete_button.pack()
listbox.pack()
load_tasks(listbox)

#Окно
window.mainloop()