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

# Function to retrieve all records from the building table
def fetch_building_data():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT * FROM building"
        cursor.execute(query)
        buildings = cursor.fetchall()

        display_building_data(buildings)

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to display building data in a new window
def display_building_data(buildings):
    root = Tk()
    root.title("Building Table Data")

    tree = ttk.Treeview(root)

    tree["columns"] = ("Building ID", "Covered Area", "Uncovered Area", "Total Area", "Internet", "Caregivers", "Playground", "Classes", "Total Computers", "ECE Rooms", "Total Rooms", "EMIS Code")
    tree.column("#0", width=0, stretch=NO)  # To hide the first empty column
    tree.column("Building ID", anchor=CENTER, width=100)
    tree.column("Covered Area", anchor=CENTER, width=100)
    tree.column("Uncovered Area", anchor=CENTER, width=100)
    tree.column("Total Area", anchor=CENTER, width=100)
    tree.column("Internet", anchor=CENTER, width=100)
    tree.column("Caregivers", anchor=CENTER, width=100)
    tree.column("Playground", anchor=CENTER, width=100)
    tree.column("Classes", anchor=CENTER, width=100)
    tree.column("Total Computers", anchor=CENTER, width=120)
    tree.column("ECE Rooms", anchor=CENTER, width=100)
    tree.column("Total Rooms", anchor=CENTER, width=100)
    tree.column("EMIS Code", anchor=CENTER, width=100)

    tree.heading("#0", text="", anchor=CENTER)
    tree.heading("Building ID", text="Building ID", anchor=CENTER)
    tree.heading("Covered Area", text="Covered Area", anchor=CENTER)
    tree.heading("Uncovered Area", text="Uncovered Area", anchor=CENTER)
    tree.heading("Total Area", text="Total Area", anchor=CENTER)
    tree.heading("Internet", text="Internet", anchor=CENTER)
    tree.heading("Caregivers", text="Caregivers", anchor=CENTER)
    tree.heading("Playground", text="Playground", anchor=CENTER)
    tree.heading("Classes", text="Classes", anchor=CENTER)
    tree.heading("Total Computers", text="Total Computers", anchor=CENTER)
    tree.heading("ECE Rooms", text="ECE Rooms", anchor=CENTER)
    tree.heading("Total Rooms", text="Total Rooms", anchor=CENTER)
    tree.heading("EMIS Code", text="EMIS Code", anchor=CENTER)

    for building in buildings:
        tree.insert("", "end", values=building)

    tree.pack(expand=YES, fill=BOTH)

    root.mainloop()

# Function to handle button click to fetch and display building data
def display_building_table():
    fetch_building_data()

# Function to set up the GUI
def gui_setup():
    root = Tk()
    root.title("Display Building Table")

    display_frame = Frame(root, padx=10, pady=10)
    display_frame.pack(padx=50, pady=50)

    display_button = Button(display_frame, text="Display Building Table", command=display_building_table, font=("Helvetica", 16))
    display_button.pack(pady=20)

    root.mainloop()

