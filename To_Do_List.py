import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql

def add_Task():
    task = task_field.get()
    if len(task) == 0:
        messagebox.showinfo('Error', 'Task should contain minimum one character!')
    else:
        tasks.append(task)
        the_cursor.execute('insert into tasks values(?)', (task,))
        update_list()
        task_field.delete(0, 'end')

def update_list():
    clear_list()
    for i in tasks:
        task_listbox.insert('end', i)

def delete_task():
    try:
        value = task_listbox.get(task_listbox.curselection())
        if value in tasks:
            tasks.remove(value)
            update_list()
            the_cursor.execute('delete from tasks where title = ?', (value,))
    except:
        messagebox.showinfo('Error', 'No task selected! Please select a task.')

def delete_all():
    message_box = messagebox.askyesno('Confirmation', 'Are you sure you want to delete all tasks?')
    if message_box:
        tasks.clear()
        the_cursor.execute('delete from tasks')
        update_list()

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    print(tasks)
    connection.commit()
    guiWindow.destroy()

def retrieve():
    tasks.clear()
    for r in the_cursor.execute('select title from tasks'):
        tasks.append(r[0])

guiWindow = tk.Tk()
guiWindow.title("TO-DO LIST APPLICATION")
guiWindow.geometry("600x600+850+350")
guiWindow.resizable(0, 0)
guiWindow.configure(bg="#F0F0F0")

connection = sql.connect('listOfTasks.db')
the_cursor = connection.cursor()
the_cursor.execute('create table if not exists tasks (title text)')
tasks = []

header = tk.Frame(guiWindow, bg="pink")
functions_frame = tk.Frame(guiWindow, bg="pink")
listbox_frame = tk.Frame(guiWindow, bg="pink")

header.pack(fill="both")
functions_frame.pack(side="left", expand=True, fill="both")
listbox_frame.pack(side="right", expand=True, fill="both")

header_label = ttk.Label(header, text="YOUR TO-DO LIST", font=("Helvetica", "25", "bold"), background="salmon",foreground="black")
header_label.pack(padx=20, pady=20)
task_label = ttk.Label(functions_frame, text="Enter a Task:", font=("Consolas", "15", "bold"), background="#FAEBD7",foreground="#000000")
task_label.place(x=30, y=40)
task_field = ttk.Entry(functions_frame, font=("Consolas", "12"), width=18, background="#FFF8DC", foreground="#A52A2A")
task_field.place(x=30, y=80)

add_button = ttk.Button(functions_frame, text="Add Task", width=26, command=add_Task)
del_button = ttk.Button(functions_frame, text="Delete Task", width=26, command=delete_task)
delete_all_button = ttk.Button(functions_frame, text="Delete All Tasks", width=26, command=delete_all)
exit_button = ttk.Button(functions_frame, text="Exit", width=26, command=close)

add_button.place(x=30, y=120)
del_button.place(x=30, y=160)
delete_all_button.place(x=30, y=200)
exit_button.place(x=30, y=240)

task_listbox = tk.Listbox(listbox_frame, width=26, height=20, selectmode='SINGLE', background="#FFFFFF",
                        foreground="#000000", selectbackground="#CD853F", selectforeground="#FFFFFF")

task_listbox.place(x=10, y=20)

retrieve()
update_list()
guiWindow.mainloop()
the_cursor.close()
connection.close() 

