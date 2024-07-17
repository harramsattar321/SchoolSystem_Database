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

# Function to retrieve gameschool details by emis_code and game_id
def fetch_gameschool_details(emis_code, game_id):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT * FROM gameschool WHERE emis_code = %s AND game_id = %s"
        cursor.execute(query, (emis_code, game_id))
        gameschool = cursor.fetchone()

        if gameschool:
            display_gameschool_details(gameschool)
        else:
            messagebox.showerror("Error", f"No record found with EMIS Code {emis_code} and Game ID {game_id}")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to display gameschool details in a message box
def display_gameschool_details(gameschool):
    details = f"EMIS Code: {gameschool[0]}\n"
    details += f"Game ID: {gameschool[1]}\n"


    messagebox.showinfo("Game School Details", details)

# Function to handle lookup button click
def lookup_gameschool():
    try:
        emis_code = int(emis_code_entry.get())
        game_id = int(game_id_entry.get())
        fetch_gameschool_details(emis_code, game_id)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid EMIS Code and Game ID")

# Function to set up the GUI for looking up gameschool details
def gui_setup():
    root = Tk()
    root.title("Lookup Game School Details")

    lookup_frame = Frame(root, padx=10, pady=10)
    lookup_frame.pack(padx=50, pady=50)

    emis_code_label = Label(lookup_frame, text="EMIS Code:", font=("Helvetica", 16))
    emis_code_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    global emis_code_entry
    emis_code_entry = Entry(lookup_frame, font=("Helvetica", 16))
    emis_code_entry.grid(row=0, column=1, padx=10, pady=10)

    game_id_label = Label(lookup_frame, text="Game ID:", font=("Helvetica", 16))
    game_id_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    global game_id_entry
    game_id_entry = Entry(lookup_frame, font=("Helvetica", 16))
    game_id_entry.grid(row=1, column=1, padx=10, pady=10)

    lookup_button = Button(lookup_frame, text="Lookup Game School", command=lookup_gameschool, font=("Helvetica", 16))
    lookup_button.grid(row=2, column=0, columnspan=2, pady=20)

    root.mainloop()

