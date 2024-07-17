import mysql.connector
from tkinter import *
from tkinter import messagebox

# Database connection function
def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Enter your Mysql password',  # Replace with your MySQL password
        database='schoolsystem'    # Replace with your database name
    )

# Function to submit data to the database
def submit_data(table, query):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        messagebox.showinfo("Success", f"{table} data submitted successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to handle submission of union council data
def submit_union_council_data():
    try:
        # Get entries from tkinter widgets
        uc_number = int(uc_number_entry.get())
        uc_name = uc_name_entry.get()

        # Prepare data tuple
      
        # Prepare SQL query
        query = f"""INSERT INTO Union_Council (uc_number, uc_name) 
                   VALUES ({uc_number}, '{uc_name}');"""

        # Submit data to the database
        submit_data("Union_Council", query)

    except ValueError as ve:
        messagebox.showerror("Input Error", f"Please enter valid integer values: {ve}")

# Function to set up the GUI for entering union council data
def gui_setup():
    global uc_number_entry, uc_name_entry

    # GUI setup
    root = Tk()
    root.title("Union Council Data Entry Form")

    # Welcome Message
    welcome_label = Label(root, text="Enter Union Council Data", font=("Helvetica", 24))
    welcome_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Union Council data input
    uc_frame = LabelFrame(root, text="Union Council Data", padx=10, pady=10, font=("Helvetica", 16))
    uc_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    # Labels and Entry fields
    uc_number_label = Label(uc_frame, text="UC Number", font=("Helvetica", 16))
    uc_number_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    uc_number_entry = Entry(uc_frame, font=("Helvetica", 16))
    uc_number_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    uc_name_label = Label(uc_frame, text="UC Name", font=("Helvetica", 16))
    uc_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    uc_name_entry = Entry(uc_frame, font=("Helvetica", 16))
    uc_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    submit_button = Button(uc_frame, text="Submit", command=submit_union_council_data, font=("Helvetica", 16))
    submit_button.grid(row=2, columnspan=2, pady=10)

    root.mainloop()

