import tkinter as tk

def gui():
    master = tk.Tk()

    master.title("Tracking Program")
    master.geometry("")

    #Title
    tk.Label(master, text="Create New").grid(row=0, column=1)

    #Full Name
    tk.Label(master, text="Full Name").grid(row=1)
    full_name_value = tk.StringVar()
    full_name = tk.Entry(master, textvariable=full_name_value).grid(row=1, column=1)

    #Receipt No.
    tk.Label(master, text="Receipt No.").grid(row=2)
    receipt_no_value = tk.StringVar()
    receipt_no = tk.Entry(master, textvariable=full_name_value).grid(row=2, column=1)

    #Item Hired
    tk.Label(master, text="Item Hired").grid(row=3)
    item_hired_value = tk.StringVar()
    item_hired = tk.Entry(master, textvariable=full_name_value).grid(row=3, column=1)

    #Quantity
    tk.Label(master, text="Quantity").grid(row=4)
    quantity_value = tk.StringVar()
    quantity = tk.Entry(master, textvariable=full_name_value).grid(row=4, column=1)

    #Buttons
    enter_data = tk.Button(master, text="Enter Data").grid(row=4, column=2)
    view_data = tk.Button(master, text="View Data").grid(row=6, column=1)

    master.mainloop()

gui()