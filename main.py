import tkinter as tk
from tkinter import *
from functools import partial
from numpy.lib.function_base import delete
import pandas as pd
from pandastable import Table
from tkinter import messagebox

data = {"first_name": [],
        "surname": [],
        "receipt_no": [],
        "item_hired": [],
        "quantity": []}

def enter_data(first_name, surname, receipt_no, item_hired, quantity):
    first_name = first_name.get()
    surname = surname.get()
    receipt_no = receipt_no.get()
    item_hired = item_hired.get()
    quantity = quantity.get()

    if first_name == "":
        messagebox.showwarning('Error', 'Please enter first name')
        return
    elif any(char.isdigit() for char in first_name) == True:
        messagebox.showwarning('Error', 'Numbers in first name is not allowed')
        return

    if surname == "":
        messagebox.showwarning('Error', 'Please enter surname')
        return
    elif any(char.isdigit() for char in surname) == True:
        messagebox.showwarning('Error', 'Numbers in surname is not allowed')
        return

    if receipt_no == "":
        messagebox.showwarning('Error', 'Please enter receipt number')
        return
    elif receipt_no.isdigit() == False:
        messagebox.showwarning('Error', 'Letters in receipt number is not allowed')
        return

    if item_hired == "":
        messagebox.showwarning('Error', 'Please enter item hired')
        return
    elif any(char.isdigit() for char in item_hired) == True:
        messagebox.showwarning('Error', 'Numbers in item hird is not allowed')
        return

    if quantity == "":
        messagebox.showwarning('Error', 'Please enter quantity')
        return
    elif quantity.isdigit() == False:
        messagebox.showwarning('Error', 'Letters in quantity is not allowed')
        return

    data["first_name"].append(first_name)
    data["surname"].append(surname)
    data["receipt_no"].append(receipt_no)
    data["item_hired"].append(item_hired)
    data["quantity"].append(quantity)

class view_data(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.main = self.master
        self.main.title('Table')
        f = Toplevel(self.main)
        df = pd.DataFrame(data, columns = ["first_name", "surname", "receipt_no", "item_hired", "quantity"])
        self.table = pt = Table(f, dataframe=df,
                                showtoolbar=False, showstatusbar=False)
        pt.show()
        mainloop()

def delete_data(row):
    row = int(row.get())
    for i in data["first_name"], data["surname"], data["receipt_no"], data["item_hired"], data["quantity"]:
        del i[row-1]

def gui():
    master = tk.Tk()

    master.title("Party Hire")
    master.geometry("")

    #Title
    tk.Label(master, text="New Data").grid(row=0, column=1)

    #Create

    #First Name
    tk.Label(master, text="First Name").grid(row=1)
    first_name_value = tk.StringVar()
    first_name = tk.Entry(master, textvariable=first_name_value).grid(row=1, column=1)

    #Surname
    tk.Label(master, text="Surname").grid(row=2)
    surname_value = tk.StringVar()
    surname = tk.Entry(master, textvariable=surname_value).grid(row=2, column=1)

    #Receipt No.
    tk.Label(master, text="Receipt No.").grid(row=3)
    receipt_no_value = tk.StringVar()
    receipt_no = tk.Entry(master, textvariable=receipt_no_value).grid(row=3, column=1)

    #Item Hired
    tk.Label(master, text="Item Hired").grid(row=4)
    item_hired_value = tk.StringVar()
    item_hired = tk.Entry(master, textvariable=item_hired_value).grid(row=4, column=1)

    #Quantity
    tk.Label(master, text="Quantity").grid(row=5)
    quantity_value = tk.StringVar()
    quantity = tk.Entry(master, textvariable=quantity_value).grid(row=5, column=1)

    #Commands
    command_enter_data = partial(enter_data, first_name_value, surname_value, receipt_no_value, item_hired_value, quantity_value)

    #Buttons
    enter_data_button = tk.Button(master, text="Enter Data", command=command_enter_data).grid(row=5, column=2)
    view_data_button = tk.Button(master, text="View Data", command=view_data).grid(row=6, column=1)

    #Delete
    tk.Label(master, text="Delete Data").grid(row=7, column=1)
    tk.Label(master, text="Data Row").grid(row=8, column=0)
    delete_row_value = tk.StringVar()
    command_delete_row = partial(delete_data, delete_row_value)
    delete_row = tk.Entry(master, textvariable=delete_row_value).grid(row=8, column=1)
    delete_row_button = tk.Button(master, text="Delete Data", command=command_delete_row).grid(row=9, column=1)

    master.mainloop()

gui()