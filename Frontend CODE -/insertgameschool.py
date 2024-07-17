import mysql.connector
from tkinter import *
from tkinter import messagebox

def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Enter your Mysql password',
        database='schoolsystem'
    )

def submit_data(table, query):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        messagebox.showinfo("Success", f"{table} data submitted successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def submit_game_school_data():
    try:
        # Convert entries to appropriate data types
        emiscode = int(emiscode_entry.get())
        game_id = int(game_id_entry.get())

   

        query = f"""INSERT INTO gameschool (Emis_Code, Game_ID) 
                   VALUES ({emiscode}, {game_id});"""
        
        submit_data("Game_School", query)

    except ValueError as ve:
        messagebox.showerror("Input Error", f"Please enter valid data types: {ve}")

def gui_setup():
    global emiscode_entry, game_id_entry

    # GUI setup
    root = Tk()
    root.title("Game-School Data Entry Form")

    # Game-School data input
    game_school_frame = LabelFrame(root, text="Game-School Data", padx=10, pady=10, font=("Helvetica", 16))
    game_school_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Configure grid layout to expand properly
    for i in range(3):
        game_school_frame.grid_rowconfigure(i, weight=1)
        game_school_frame.grid_columnconfigure(0, weight=1)
        game_school_frame.grid_columnconfigure(1, weight=2)

    emiscode_label = Label(game_school_frame, text="EMIS Code", font=("Helvetica", 16))
    emiscode_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    emiscode_entry = Entry(game_school_frame, font=("Helvetica", 16))
    emiscode_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    game_id_label = Label(game_school_frame, text="Game ID", font=("Helvetica", 16))
    game_id_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    game_id_entry = Entry(game_school_frame, font=("Helvetica", 16))
    game_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    submit_game_school_button = Button(game_school_frame, text="Submit Game-School Data", command=submit_game_school_data, font=("Helvetica", 16))
    submit_game_school_button.grid(row=2, columnspan=2, pady=10)

    root.mainloop()


