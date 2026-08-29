import tkinter as tk
from gui import add_task_to_gui, delete_task_from_gui, load_tasks, edit_task_from_gui, save_task_from_gui, toggle_completed_from_gui

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

update_button = tk.Button(
    window,
    text='Изменить задачу',
    command=lambda: edit_task_from_gui(entry, listbox)
)

save_button = tk.Button(
    window,
    text="Сохранить изменение",
    command=lambda: save_task_from_gui(entry, listbox)
)

completed_button = tk.Button(
    window,
    text="Выполнить задачу",
    command=lambda: toggle_completed_from_gui(listbox)
)
#Вызов
entry.pack()
button.pack()
completed_button.pack()
delete_button.pack()
listbox.pack()
update_button.pack()
save_button.pack()
load_tasks(listbox)

#Окно
window.mainloop()