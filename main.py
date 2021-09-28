import tkinter as tk
from functools import partial

lst = []



def enter_data(full_name, receipt_no, item_hired, quantity):
    dict = {"full_name": full_name.get(),
            "receipt_no": receipt_no.get(),
            "item_hired": item_hired.get(),
            "quantity": quantity.get()}
    lst.append(dict)
    print(lst)
    return

def view_data():
    return

def delete_data(row):
    lst.remove(lst[row])
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
    view_data = tk.Button(master, text="View Data").grid(row=5, column=1)

    #Delete
    tk.Label(master, text="Delete Data").grid(row=6, column=1)
    tk.Label(master, text="Data Row").grid(row=7, column=0)
    delete_row_value = tk.StringVar()
    delete_row = tk.Entry(master, textvariable=delete_row_value).grid(row=7, column=1)
    delete_row_button = tk.Button(master, text="Delete Data").grid(row=8, column=1)

    master.mainloop()

gui()