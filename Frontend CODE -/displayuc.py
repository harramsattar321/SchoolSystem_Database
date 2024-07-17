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

# Function to retrieve all records from the UNION_COUNCIL table
def fetch_union_council_data():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT uc_number, uc_name FROM UNION_COUNCIL"
        cursor.execute(query)
        union_councils = cursor.fetchall()

        display_union_council_data(union_councils)

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to display UNION_COUNCIL data in a new window
def display_union_council_data(union_councils):
    root = Tk()
    root.title("UNION_COUNCIL Table Data")

    tree = ttk.Treeview(root)

    tree["columns"] = ("UC Number", "UC Name")
    tree.column("#0", width=0, stretch=NO)  # To hide the first empty column
    tree.column("UC Number", anchor=CENTER, width=120)
    tree.column("UC Name", anchor=CENTER, width=200)

    tree.heading("#0", text="", anchor=CENTER)
    tree.heading("UC Number", text="UC Number", anchor=CENTER)
    tree.heading("UC Name", text="UC Name", anchor=CENTER)

    for union_council in union_councils:
        tree.insert("", "end", values=union_council)

    tree.pack(expand=YES, fill=BOTH)

    root.mainloop()

# Function to handle button click to fetch and display UNION_COUNCIL data
def display_union_council_table():
    fetch_union_council_data()

# Function to set up the GUI
def gui_setup():
    root = Tk()
    root.title("Display UNION_COUNCIL Table")

    display_frame = Frame(root, padx=10, pady=10)
    display_frame.pack(padx=50, pady=50)

    display_button = Button(display_frame, text="Display UNION_COUNCIL Table", command=display_union_council_table, font=("Helvetica", 16))
    display_button.pack(pady=20)

    root.mainloop()


