import mysql.connector
from tkinter import *
from tkinter import messagebox

# Function to establish database connection
def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Enter your Mysql password',  # Replace with your MySQL password
        database='schoolsystem'
    )

# Function to fetch existing game data based on game_id
def fetch_game(game_id):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = f"SELECT * FROM game WHERE game_id = {game_id}"
        cursor.execute(query)
        game_data = cursor.fetchone()
        connection.close()
        return game_data

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        return None

# Function to update game data in the database
def update_game(game_id, game_name):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = f"""UPDATE game SET
                    Game_Name = '{game_name}'
                    WHERE game_id = {game_id}"""
        cursor.execute(query)
        connection.commit()
        messagebox.showinfo("Success", f"Game with ID {game_id} updated successfully")
        connection.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Function to handle form submission for updating game record
def submit_game_update():
    try:
        game_id = int(game_id_entry.get())
        game_name = game_name_entry.get()

        update_game(game_id, game_name)
    
    except ValueError as ve:
        messagebox.showerror("Input Error", f"Invalid input: {ve}")

# Function to set up the GUI for updating game record
def gui_setup():
    global game_id_entry, game_name_entry

    root = Tk()
    root.title("Modify Game")

    # GUI setup for form
    form_frame = LabelFrame(root, text="Update Game", padx=10, pady=10, font=("Helvetica", 16))
    form_frame.pack(padx=20, pady=20)

    game_id_label = Label(form_frame, text="Game ID:", font=("Helvetica", 14))
    game_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    game_id_entry = Entry(form_frame, font=("Helvetica", 14))
    game_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    fetch_button = Button(form_frame, text="Fetch Data", command=fetch_and_populate_form, font=("Helvetica", 14))
    fetch_button.grid(row=0, column=2, padx=5, pady=5)

    game_name_label = Label(form_frame, text="Game Name:", font=("Helvetica", 14))
    game_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    game_name_entry = Entry(form_frame, font=("Helvetica", 14))
    game_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    submit_button = Button(form_frame, text="Update Game", command=submit_game_update, font=("Helvetica", 14))
    submit_button.grid(row=2, columnspan=2, pady=10)

    root.mainloop()

# Function to fetch and populate form with existing data
def fetch_and_populate_form():
    game_id = int(game_id_entry.get())
    game_data = fetch_game(game_id)

    if game_data:
        # Populate form fields with fetched data
        game_id_entry.delete(0, END)
        game_id_entry.insert(0, game_data[0])  # game_id
        game_name_entry.delete(0, END)
        game_name_entry.insert(0, game_data[1])  # Game_Name
    else:
        messagebox.showerror("Error", f"Game with ID {game_id} not found")


