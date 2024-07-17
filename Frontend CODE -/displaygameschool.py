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

# Function to retrieve all records from the gameschool table
def fetch_gameschool_data():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT emis_code, game_id FROM gameschool"
        cursor.execute(query)
        gameschools = cursor.fetchall()

        display_gameschool_data(gameschools)

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to display gameschool data in a new window
def display_gameschool_data(gameschools):
    root = Tk()
    root.title("Gameschool Table Data")

    tree = ttk.Treeview(root)

    tree["columns"] = ("EMIS Code", "Game ID")
    tree.column("#0", width=0, stretch=NO)  # To hide the first empty column
    tree.column("EMIS Code", anchor=CENTER, width=120)
    tree.column("Game ID", anchor=CENTER, width=120)

    tree.heading("#0", text="", anchor=CENTER)
    tree.heading("EMIS Code", text="EMIS Code", anchor=CENTER)
    tree.heading("Game ID", text="Game ID", anchor=CENTER)

    for gameschool in gameschools:
        tree.insert("", "end", values=gameschool)

    tree.pack(expand=YES, fill=BOTH)

    root.mainloop()

# Function to handle button click to fetch and display gameschool data
def display_gameschool_table():
    fetch_gameschool_data()

# Function to set up the GUI
def gui_setup():
    root = Tk()
    root.title("Display Gameschool Table")

    display_frame = Frame(root, padx=10, pady=10)
    display_frame.pack(padx=50, pady=50)

    display_button = Button(display_frame, text="Display Gameschool Table", command=display_gameschool_table, font=("Helvetica", 16))
    display_button.pack(pady=20)

    root.mainloop()

