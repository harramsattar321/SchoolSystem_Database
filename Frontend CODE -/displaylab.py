import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Function to establish database connection
def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Enter your Mysql password',
        database='schoolsystem'
    )

# Function to retrieve all records from the LAB table
def fetch_lab_data():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT lab_id, lab_name FROM LAB"
        cursor.execute(query)
        labs = cursor.fetchall()

        display_lab_data(labs)

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to display LAB data in a new window
def display_lab_data(labs):
    root = Tk()
    root.title("LAB Table Data")

    tree = ttk.Treeview(root)

    tree["columns"] = ("Lab ID", "Lab Name")
    tree.column("#0", width=0, stretch=NO)  # To hide the first empty column
    tree.column("Lab ID", anchor=CENTER, width=120)
    tree.column("Lab Name", anchor=CENTER, width=200)

    tree.heading("#0", text="", anchor=CENTER)
    tree.heading("Lab ID", text="Lab ID", anchor=CENTER)
    tree.heading("Lab Name", text="Lab Name", anchor=CENTER)

    for lab in labs:
        tree.insert("", "end", values=lab)

    tree.pack(expand=YES, fill=BOTH)

    root.mainloop()

# Function to handle button click to fetch and display LAB data
def display_lab_table():
    fetch_lab_data()

# Function to set up the GUI
def gui_setup():
    root = Tk()
    root.title("Display LAB Table")

    display_frame = Frame(root, padx=10, pady=10)
    display_frame.pack(padx=50, pady=50)

    display_button = Button(display_frame, text="Display LAB Table", command=display_lab_table, font=("Helvetica", 16))
    display_button.pack(pady=20)

    root.mainloop()


