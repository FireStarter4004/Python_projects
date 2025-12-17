#Kyler Brungerwood
#To-do list application
#the start date is 12/7/2025

import tkinter as tk
from tkinter import messagebox
import button_commands as bc

tasks=open("To_do_list/tasks.txt")
listoftasks=tasks.readlines()

t_length=len(listoftasks)
for i in range(t_length):
    listoftasks[i]=listoftasks[i].strip("\n")




root=tk.Tk()
root.geometry("400x600")
root.configure(bg="purple")

def myGUI ():
    root.title("to-do list")
    titlelabel = tk.Label(root, text="to-do list", bg="white", fg="black", font=("Arial", 24))
    titlelabel.pack(pady=10)
    titlelabel2 = tk.Label(root, text="for Kyler Brungerwood", bg="white", fg="black", font=("Arial", 14))
    titlelabel2.pack(pady=5)
    taskslabel = tk.Label(root, text="daily tasks", bg="purple", fg="black", font=("Arial", 18,"underline"))
    taskslabel.pack(pady=5)
    

    task_frame = tk.Frame(root, bg="pink", relief="sunken", bd=5)
    task_frame.pack(pady=30, padx=30, fill="both", expand=True)
    
    task_listbox = tk.Listbox(task_frame, font=("Arial", 12), bg="white", fg="black")
    task_listbox.pack(side="left", fill="both", expand=True)
    for task in listoftasks:
        task_listbox.insert("end", task)

    taskentry = tk.Entry(root, width=30, font=("Arial", 14))
    taskentry.pack(side="bottom", pady=30)
    taskentry.insert(0, "enter a new task  :")

    add_button = tk.Button(root, text="add task", bg="green", fg="white", font=("Arial", 14), command=lambda: bc.add_task(task_listbox, taskentry))
    add_button.pack(padx=10, pady=10,)
    

myGUI()
root.mainloop()