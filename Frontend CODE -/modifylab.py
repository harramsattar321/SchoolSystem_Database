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

# Function to fetch existing lab data based on lab_id
def fetch_lab(lab_id):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = f"SELECT * FROM lab WHERE lab_id = {lab_id}"
        cursor.execute(query)
        lab_data = cursor.fetchone()
        connection.close()
        return lab_data

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        return None

# Function to update lab data in the database
def update_lab(lab_id, lab_name):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = f"""UPDATE lab SET
                    Lab_Name = '{lab_name}'
                    WHERE lab_id = {lab_id}"""
        cursor.execute(query)
        connection.commit()
        messagebox.showinfo("Success", f"Lab with ID {lab_id} updated successfully")
        connection.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Function to handle form submission for updating lab record
def submit_lab_update():
    try:
        lab_id = int(lab_id_entry.get())
        lab_name = lab_name_entry.get()

        update_lab(lab_id, lab_name)
    
    except ValueError as ve:
        messagebox.showerror("Input Error", f"Invalid input: {ve}")

# Function to set up the GUI for updating lab record
def gui_setup():
    global lab_id_entry, lab_name_entry

    root = Tk()
    root.title("Modify Lab")

    # GUI setup for form
    form_frame = LabelFrame(root, text="Update Lab", padx=10, pady=10, font=("Helvetica", 16))
    form_frame.pack(padx=20, pady=20)

    lab_id_label = Label(form_frame, text="Lab ID:", font=("Helvetica", 14))
    lab_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    lab_id_entry = Entry(form_frame, font=("Helvetica", 14))
    lab_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    fetch_button = Button(form_frame, text="Fetch Data", command=fetch_and_populate_form, font=("Helvetica", 14))
    fetch_button.grid(row=0, column=2, padx=5, pady=5)

    lab_name_label = Label(form_frame, text="Lab Name:", font=("Helvetica", 14))
    lab_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    lab_name_entry = Entry(form_frame, font=("Helvetica", 14))
    lab_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    submit_button = Button(form_frame, text="Update Lab", command=submit_lab_update, font=("Helvetica", 14))
    submit_button.grid(row=2, columnspan=2, pady=10)

    root.mainloop()

# Function to fetch and populate form with existing data
def fetch_and_populate_form():
    lab_id = int(lab_id_entry.get())
    lab_data = fetch_lab(lab_id)

    if lab_data:
        # Populate form fields with fetched data
        lab_id_entry.delete(0, END)
        lab_id_entry.insert(0, lab_data[0])  # lab_id
        lab_name_entry.delete(0, END)
        lab_name_entry.insert(0, lab_data[1])  # Lab_Name
    else:
        messagebox.showerror("Error", f"Lab with ID {lab_id} not found")

