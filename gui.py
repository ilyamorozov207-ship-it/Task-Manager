import tkinter as tk


def add_task(entry, listbox):
    task = entry.get()
    listbox.insert(tk.END, task)
    entry.delete(0, tk.END)