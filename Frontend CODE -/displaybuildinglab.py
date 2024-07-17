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

# Function to retrieve all records from the building_lab table
def fetch_building_lab_data():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT * FROM building_lab"
        cursor.execute(query)
        building_labs = cursor.fetchall()

        display_building_lab_data(building_labs)

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to display building_lab data in a new window
def display_building_lab_data(building_labs):
    root = Tk()
    root.title("Building_Lab Table Data")

    tree = ttk.Treeview(root)

    tree["columns"] = ("Building ID", "Lab ID")
    tree.column("#0", width=0, stretch=NO)  # To hide the first empty column
    tree.column("Building ID", anchor=CENTER, width=100)
    tree.column("Lab ID", anchor=CENTER, width=100)

    tree.heading("#0", text="", anchor=CENTER)
    tree.heading("Building ID", text="Building ID", anchor=CENTER)
    tree.heading("Lab ID", text="Lab ID", anchor=CENTER)

    for building_lab in building_labs:
        tree.insert("", "end", values=building_lab)

    tree.pack(expand=YES, fill=BOTH)

    root.mainloop()

# Function to handle button click to fetch and display building_lab data
def display_building_lab_table():
    fetch_building_lab_data()

# Function to set up the GUI
def gui_setup():
    root = Tk()
    root.title("Display Building_Lab Table")

    display_frame = Frame(root, padx=10, pady=10)
    display_frame.pack(padx=50, pady=50)

    display_button = Button(display_frame, text="Display Building_Lab Table", command=display_building_lab_table, font=("Helvetica", 16))
    display_button.pack(pady=20)

    root.mainloop()


