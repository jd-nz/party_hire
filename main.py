import tkinter as tk
from tkinter import *
from functools import partial
from numpy import disp
from numpy.lib.function_base import delete
import pandas as pd
from pandastable import Table

data = {"first_name": [],
        "surname": [],
        "receipt_no": [],
        "item_hired": [],
        "quantity": []}

def enter_data(first_name, surname, receipt_no, item_hired, quantity):
    data["first_name"].append(first_name.get())
    data["surname"].append(surname.get())
    data["receipt_no"].append(receipt_no.get())
    data["item_hired"].append(item_hired.get())
    data["quantity"].append(quantity.get())
    print(data)

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
    tk.Label(master, text="Create New").grid(row=0, column=1)

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