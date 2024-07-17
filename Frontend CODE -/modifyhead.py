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

# Function to fetch existing head data based on head_id
def fetch_head(head_id):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = f"SELECT * FROM head WHERE head_id = {head_id}"
        cursor.execute(query)
        head_data = cursor.fetchone()
        connection.close()
        return head_data

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        return None

# Function to update head data in the database
def update_head(head_id, head_name, head_type, head_grade, emis_code):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = f"""UPDATE head SET
                    Head_Name = '{head_name}',
                    Head_Type = '{head_type}',
                    Head_Grade = '{head_grade}',
                    Emis_Code = {emis_code}
                    WHERE head_id = {head_id}"""
        cursor.execute(query)
        connection.commit()
        messagebox.showinfo("Success", f"Head with ID {head_id} updated successfully")
        connection.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Function to handle form submission for updating head record
def submit_head_update():
    try:
        head_id = int(head_id_entry.get())
        head_name = head_name_entry.get()
        head_type = head_type_entry.get()
        head_grade = head_grade_entry.get()
        emis_code = int(emis_code_entry.get())

        update_head(head_id, head_name, head_type, head_grade, emis_code)
    
    except ValueError as ve:
        messagebox.showerror("Input Error", f"Invalid input: {ve}")

# Function to set up the GUI for updating head record
def gui_setup():
    global head_id_entry, head_name_entry, head_type_entry, head_grade_entry, emis_code_entry

    root = Tk()
    root.title("Modify Head")

    # GUI setup for form
    form_frame = LabelFrame(root, text="Update Head", padx=10, pady=10, font=("Helvetica", 16))
    form_frame.pack(padx=20, pady=20)

    head_id_label = Label(form_frame, text="Head ID:", font=("Helvetica", 14))
    head_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    head_id_entry = Entry(form_frame, font=("Helvetica", 14))
    head_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    fetch_button = Button(form_frame, text="Fetch Data", command=fetch_and_populate_form, font=("Helvetica", 14))
    fetch_button.grid(row=0, column=2, padx=5, pady=5)

    head_name_label = Label(form_frame, text="Head Name:", font=("Helvetica", 14))
    head_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    head_name_entry = Entry(form_frame, font=("Helvetica", 14))
    head_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    head_type_label = Label(form_frame, text="Head Type:", font=("Helvetica", 14))
    head_type_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    head_type_entry = Entry(form_frame, font=("Helvetica", 14))
    head_type_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    head_grade_label = Label(form_frame, text="Head Grade:", font=("Helvetica", 14))
    head_grade_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
    head_grade_entry = Entry(form_frame, font=("Helvetica", 14))
    head_grade_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    emis_code_label = Label(form_frame, text="Emis Code:", font=("Helvetica", 14))
    emis_code_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
    emis_code_entry = Entry(form_frame, font=("Helvetica", 14))
    emis_code_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    submit_button = Button(form_frame, text="Update Head", command=submit_head_update, font=("Helvetica", 14))
    submit_button.grid(row=5, columnspan=2, pady=10)

    root.mainloop()

# Function to fetch and populate form with existing data
def fetch_and_populate_form():
    head_id = int(head_id_entry.get())
    head_data = fetch_head(head_id)

    if head_data:
        # Populate form fields with fetched data
        head_id_entry.delete(0, END)
        head_id_entry.insert(0, head_data[0])  # head_id
        head_name_entry.delete(0, END)
        head_name_entry.insert(0, head_data[1])  # Head_Name
        head_type_entry.delete(0, END)
        head_type_entry.insert(0, head_data[2])  # Head_Type
        head_grade_entry.delete(0, END)
        head_grade_entry.insert(0, head_data[3])  # Head_Grade
        emis_code_entry.delete(0, END)
        emis_code_entry.insert(0, head_data[4])  # Emis_Code
    else:
        messagebox.showerror("Error", f"Head with ID {head_id} not found")
