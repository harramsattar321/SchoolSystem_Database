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

# Function to retrieve all records from the school table
def fetch_school_data():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT * FROM school"
        cursor.execute(query)
        schools = cursor.fetchall()

        display_school_data(schools)

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to display school data in a new window
def display_school_data(schools):
    root = Tk()
    root.title("School Table Data")

    tree = ttk.Treeview(root)

    tree["columns"] = ("EMIS Code", "School Name", "School Shift", "School Level", "Establishment Year", "School Medium", "Total Teachers", "Total Students")
    tree.column("#0", width=0, stretch=NO)  # To hide the first empty column
    tree.column("EMIS Code", anchor=CENTER, width=100)
    tree.column("School Name", anchor=CENTER, width=150)
    tree.column("School Shift", anchor=CENTER, width=100)
    tree.column("School Level", anchor=CENTER, width=100)
    tree.column("Establishment Year", anchor=CENTER, width=120)
    tree.column("School Medium", anchor=CENTER, width=100)
    tree.column("Total Teachers", anchor=CENTER, width=120)
    tree.column("Total Students", anchor=CENTER, width=120)

    tree.heading("#0", text="", anchor=CENTER)
    tree.heading("EMIS Code", text="EMIS Code", anchor=CENTER)
    tree.heading("School Name", text="School Name", anchor=CENTER)
    tree.heading("School Shift", text="School Shift", anchor=CENTER)
    tree.heading("School Level", text="School Level", anchor=CENTER)
    tree.heading("Establishment Year", text="Establishment Year", anchor=CENTER)
    tree.heading("School Medium", text="School Medium", anchor=CENTER)
    tree.heading("Total Teachers", text="Total Teachers", anchor=CENTER)
    tree.heading("Total Students", text="Total Students", anchor=CENTER)

    for school in schools:
        tree.insert("", "end", values=school)

    tree.pack(expand=YES, fill=BOTH)

    root.mainloop()

# Function to handle button click to fetch and display school data
def display_school_table():
    fetch_school_data()

# Function to set up the GUI
def gui_setup():
    root = Tk()
    root.title("Display School Table")

    display_frame = Frame(root, padx=10, pady=10)
    display_frame.pack(padx=50, pady=50)

    display_button = Button(display_frame, text="Display School Table", command=display_school_table, font=("Helvetica", 16))
    display_button.pack(pady=20)

    root.mainloop()

