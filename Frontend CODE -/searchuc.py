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

# Function to retrieve union council details by uc_number
def fetch_union_council_details(uc_number):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT * FROM union_council WHERE uc_number = %s"
        cursor.execute(query, (uc_number,))
        union_council = cursor.fetchone()

        if union_council:
            display_union_council_details(union_council)
        else:
            messagebox.showerror("Error", f"No union council found with UC Number {uc_number}")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to display union council details in a message box
def display_union_council_details(union_council):
    details = f"UC Number: {union_council[0]}\n"
    details += f"Name: {union_council[1]}\n"
 

    messagebox.showinfo("Union Council Details", details)

# Function to handle lookup button click
def lookup_union_council():
    try:
        uc_number = int(uc_number_entry.get())
        fetch_union_council_details(uc_number)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid UC Number")

# Function to set up the GUI for looking up union council details
def gui_setup():
    root = Tk()
    root.title("Lookup Union Council Details")

    lookup_frame = Frame(root, padx=10, pady=10)
    lookup_frame.pack(padx=50, pady=50)

    uc_number_label = Label(lookup_frame, text="UC Number to Lookup:", font=("Helvetica", 16))
    uc_number_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    global uc_number_entry
    uc_number_entry = Entry(lookup_frame, font=("Helvetica", 16))
    uc_number_entry.grid(row=0, column=1, padx=10, pady=10)

    lookup_button = Button(lookup_frame, text="Lookup Union Council", command=lookup_union_council, font=("Helvetica", 16))
    lookup_button.grid(row=1, column=0, columnspan=2, pady=20)

    root.mainloop()
