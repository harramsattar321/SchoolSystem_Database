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

# Function to retrieve all records from the game table
def fetch_game_data():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT game_id, game_name FROM game"
        cursor.execute(query)
        games = cursor.fetchall()

        display_game_data(games)

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to display game data in a new window
def display_game_data(games):
    root = Tk()
    root.title("Game Table Data")

    tree = ttk.Treeview(root)

    tree["columns"] = ("Game ID", "Game Name")
    tree.column("#0", width=0, stretch=NO)  # To hide the first empty column
    tree.column("Game ID", anchor=CENTER, width=120)
    tree.column("Game Name", anchor=CENTER, width=200)

    tree.heading("#0", text="", anchor=CENTER)
    tree.heading("Game ID", text="Game ID", anchor=CENTER)
    tree.heading("Game Name", text="Game Name", anchor=CENTER)

    for game in games:
        tree.insert("", "end", values=game)

    tree.pack(expand=YES, fill=BOTH)

    root.mainloop()

# Function to handle button click to fetch and display game data
def display_game_table():
    fetch_game_data()

# Function to set up the GUI
def gui_setup():
    root = Tk()
    root.title("Display Game Table")

    display_frame = Frame(root, padx=10, pady=10)
    display_frame.pack(padx=50, pady=50)

    display_button = Button(display_frame, text="Display Game Table", command=display_game_table, font=("Helvetica", 16))
    display_button.pack(pady=20)

    root.mainloop()


