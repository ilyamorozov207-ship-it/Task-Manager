import tkinter as tk
from gui import add_task 

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
    command=lambda: add_task(entry, listbox)
)

#Вызов
entry.pack()
button.pack()
listbox.pack()
#Окно
window.mainloop()