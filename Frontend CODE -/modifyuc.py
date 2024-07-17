import mysql.connector
from tkinter import *
from tkinter import messagebox

# Function to establish database connection
def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Enter your Mysql password',  # Replace with your MySQL password
        database='schoolsystem'
    )

# Function to fetch existing union_council data based on uc_number
def fetch_union_council(uc_number):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = f"SELECT * FROM union_council WHERE uc_number = '{uc_number}'"
        cursor.execute(query)
        uc_data = cursor.fetchone()
        connection.close()
        return uc_data

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        return None

# Function to update union_council data in the database
def update_union_council(uc_number, uc_name):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = f"""UPDATE union_council SET
                    UC_Name = '{uc_name}'
                    WHERE uc_number = '{uc_number}'"""
        cursor.execute(query)
        connection.commit()
        messagebox.showinfo("Success", f"Union Council with Number {uc_number} updated successfully")
        connection.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Function to handle form submission for updating union_council record
def submit_uc_update():
    try:
        uc_number = uc_number_entry.get()
        uc_name = uc_name_entry.get()

        update_union_council(uc_number, uc_name)
    
    except ValueError as ve:
        messagebox.showerror("Input Error", f"Invalid input: {ve}")

# Function to set up the GUI for updating union_council record
def gui_setup():
    global uc_number_entry, uc_name_entry

    root = Tk()
    root.title("Modify Union Council")

    # GUI setup for form
    form_frame = LabelFrame(root, text="Update Union Council", padx=10, pady=10, font=("Helvetica", 16))
    form_frame.pack(padx=20, pady=20)

    uc_number_label = Label(form_frame, text="Union Council Number:", font=("Helvetica", 14))
    uc_number_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    uc_number_entry = Entry(form_frame, font=("Helvetica", 14))
    uc_number_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    fetch_button = Button(form_frame, text="Fetch Data", command=fetch_and_populate_form, font=("Helvetica", 14))
    fetch_button.grid(row=0, column=2, padx=5, pady=5)

    uc_name_label = Label(form_frame, text="Union Council Name:", font=("Helvetica", 14))
    uc_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    uc_name_entry = Entry(form_frame, font=("Helvetica", 14))
    uc_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    submit_button = Button(form_frame, text="Update Union Council", command=submit_uc_update, font=("Helvetica", 14))
    submit_button.grid(row=2, columnspan=2, pady=10)

    root.mainloop()

# Function to fetch and populate form with existing data
def fetch_and_populate_form():
    uc_number = uc_number_entry.get()
    uc_data = fetch_union_council(uc_number)

    if uc_data:
        # Populate form fields with fetched data
        uc_name_entry.delete(0, END)
        uc_name_entry.insert(0, uc_data[1])  # UC_Name
    else:
        messagebox.showerror("Error", f"Union Council with Number {uc_number} not found")
