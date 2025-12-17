
import tkinter as tk
from tkinter import messagebox
import json as js
import To_do_list as tdl

tasks=open("To_do_list/tasks.txt")
listoftasks = tasks.readlines()
tasks.close()


def add_task(task_listbox, task_entry):
    task_text = task_entry.get()
    if task_text and task_text != "enter a new task :":
        task_text.delete("enter a new task :")
        tasks = open("tasks.txt","a+")
        tasks.write(task_text + "\n")
        listoftasks = tasks.readlines()
        tasks.close()
        task_listbox.insert(tk.END, task_text)

        task_entry.delete(0, tk.END)
        task_entry.insert(0, "enter a new task  :")
    return task_text
  