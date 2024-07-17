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

# Function to retrieve all records from the HEAD table
def fetch_head_data():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT head_id, head_name, head_type, head_grade, emis_code FROM HEAD"
        cursor.execute(query)
        heads = cursor.fetchall()

        display_head_data(heads)

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to display HEAD data in a new window
def display_head_data(heads):
    root = Tk()
    root.title("HEAD Table Data")

    tree = ttk.Treeview(root)

    tree["columns"] = ("Head ID", "Head Name", "Head Type", "Head Grade", "EMIS Code")
    tree.column("#0", width=0, stretch=NO)  # To hide the first empty column
    tree.column("Head ID", anchor=CENTER, width=120)
    tree.column("Head Name", anchor=CENTER, width=150)
    tree.column("Head Type", anchor=CENTER, width=120)
    tree.column("Head Grade", anchor=CENTER, width=120)
    tree.column("EMIS Code", anchor=CENTER, width=120)

    tree.heading("#0", text="", anchor=CENTER)
    tree.heading("Head ID", text="Head ID", anchor=CENTER)
    tree.heading("Head Name", text="Head Name", anchor=CENTER)
    tree.heading("Head Type", text="Head Type", anchor=CENTER)
    tree.heading("Head Grade", text="Head Grade", anchor=CENTER)
    tree.heading("EMIS Code", text="EMIS Code", anchor=CENTER)

    for head in heads:
        tree.insert("", "end", values=head)

    tree.pack(expand=YES, fill=BOTH)

    root.mainloop()

# Function to handle button click to fetch and display HEAD data
def display_head_table():
    fetch_head_data()

# Function to set up the GUI
def gui_setup():
    root = Tk()
    root.title("Display HEAD Table")

    display_frame = Frame(root, padx=10, pady=10)
    display_frame.pack(padx=50, pady=50)

    display_button = Button(display_frame, text="Display HEAD Table", command=display_head_table, font=("Helvetica", 16))
    display_button.pack(pady=20)

    root.mainloop()

