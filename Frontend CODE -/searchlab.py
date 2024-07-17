import mysql.connector
from tkinter import *
from tkinter import messagebox

# Function to establish database connection
def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Enter your Mysql password',
        database='schoolsystem'
    )

# Function to retrieve lab details by lab_id
def fetch_lab_details(lab_id):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT * FROM lab WHERE lab_id = %s"
        cursor.execute(query, (lab_id,))
        lab = cursor.fetchone()

        if lab:
            display_lab_details(lab)
        else:
            messagebox.showerror("Error", f"No lab found with Lab ID {lab_id}")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to display lab details in a message box
def display_lab_details(lab):
    details = f"Lab ID: {lab[0]}\n"
    details += f"Lab Name: {lab[1]}\n"


    messagebox.showinfo("Lab Details", details)

# Function to handle lookup button click
def lookup_lab():
    try:
        lab_id = int(lab_id_entry.get())
        fetch_lab_details(lab_id)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid Lab ID")

# Function to set up the GUI for looking up lab details
def gui_setup():
    root = Tk()
    root.title("Lookup Lab Details")

    lookup_frame = Frame(root, padx=10, pady=10)
    lookup_frame.pack(padx=50, pady=50)

    lab_id_label = Label(lookup_frame, text="Lab ID to Lookup:", font=("Helvetica", 16))
    lab_id_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    global lab_id_entry
    lab_id_entry = Entry(lookup_frame, font=("Helvetica", 16))
    lab_id_entry.grid(row=0, column=1, padx=10, pady=10)

    lookup_button = Button(lookup_frame, text="Lookup Lab", command=lookup_lab, font=("Helvetica", 16))
    lookup_button.grid(row=1, column=0, columnspan=2, pady=20)

    root.mainloop()

