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

# Function to retrieve game details by game_id
def fetch_game_details(game_id):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT * FROM game WHERE game_id = %s"
        cursor.execute(query, (game_id,))
        game = cursor.fetchone()

        if game:
            display_game_details(game)
        else:
            messagebox.showerror("Error", f"No game found with Game ID {game_id}")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to display game details in a message box
def display_game_details(game):
    details = f"Game ID: {game[0]}\n"
    details += f"Game Name: {game[1]}\n"


    messagebox.showinfo("Game Details", details)

# Function to handle lookup button click
def lookup_game():
    try:
        game_id = int(game_id_entry.get())
        fetch_game_details(game_id)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid Game ID")

# Function to set up the GUI for looking up game details
def gui_setup():
    root = Tk()
    root.title("Lookup Game Details")

    lookup_frame = Frame(root, padx=10, pady=10)
    lookup_frame.pack(padx=50, pady=50)

    game_id_label = Label(lookup_frame, text="Game ID to Lookup:", font=("Helvetica", 16))
    game_id_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    global game_id_entry
    game_id_entry = Entry(lookup_frame, font=("Helvetica", 16))
    game_id_entry.grid(row=0, column=1, padx=10, pady=10)

    lookup_button = Button(lookup_frame, text="Lookup Game", command=lookup_game, font=("Helvetica", 16))
    lookup_button.grid(row=1, column=0, columnspan=2, pady=20)

    root.mainloop()
