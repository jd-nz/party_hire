import tkinter as tk
from tkinter import *
from functools import partial
from numpy import disp
import pandas as pd
from pandastable import Table

data = {"full_name": [],
            "receipt_no": [],
            "item_hired": [],
            "quantity": []}

def enter_data(full_name, receipt_no, item_hired, quantity):
    data["full_name"].append(full_name.get())
    data["receipt_no"].append(receipt_no.get())
    data["item_hired"].append(item_hired.get())
    data["quantity"].append(quantity.get())

class view_data(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.main = self.master
        self.main.title('Table')
        f = Toplevel(self.main)
        df = pd.DataFrame(data, columns = ["full_name", "receipt_no", "item_hired", "quantity"])
        self.table = pt = Table(f, dataframe=df,
                                showtoolbar=False, showstatusbar=False)
        pt.show()
        mainloop()
        return

def delete_data(row):
    return

def gui():
    master = tk.Tk()

    master.title("Party Hire")
    master.geometry("")

    #Title
    tk.Label(master, text="Create New").grid(row=0, column=1)

    #Create

    #Full Name
    tk.Label(master, text="Full Name").grid(row=1)
    full_name_value = tk.StringVar()
    full_name = tk.Entry(master, textvariable=full_name_value).grid(row=1, column=1)

    #Receipt No.
    tk.Label(master, text="Receipt No.").grid(row=2)
    receipt_no_value = tk.StringVar()
    receipt_no = tk.Entry(master, textvariable=receipt_no_value).grid(row=2, column=1)

    #Item Hired
    tk.Label(master, text="Item Hired").grid(row=3)
    item_hired_value = tk.StringVar()
    item_hired = tk.Entry(master, textvariable=item_hired_value).grid(row=3, column=1)

    #Quantity
    tk.Label(master, text="Quantity").grid(row=4)
    quantity_value = tk.StringVar()
    quantity = tk.Entry(master, textvariable=quantity_value).grid(row=4, column=1)

    #Commands
    command_enter_data = partial(enter_data, full_name_value, receipt_no_value, item_hired_value, quantity_value)

    #Buttons
    enter_data_button = tk.Button(master, text="Enter Data", command=command_enter_data).grid(row=4, column=2)
    view_data_button = tk.Button(master, text="View Data", command=view_data).grid(row=5, column=1)

    #Delete
    tk.Label(master, text="Delete Data").grid(row=6, column=1)
    tk.Label(master, text="Data Row").grid(row=7, column=0)
    delete_row_value = tk.StringVar()
    delete_row = tk.Entry(master, textvariable=delete_row_value).grid(row=7, column=1)
    delete_row_button = tk.Button(master, text="Delete Data").grid(row=8, column=1)

    master.mainloop()

gui()