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

# Function to retrieve head details by head_id
def fetch_head_details(head_id):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT * FROM HEAD WHERE head_id = %s"
        cursor.execute(query, (head_id,))
        head = cursor.fetchone()

        if head:
            display_head_details(head)
        else:
            messagebox.showerror("Error", f"No head found with Head ID {head_id}")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to display head details in a message box
def display_head_details(head):
    details = f"Head ID: {head[0]}\n"
    details += f"Head Name: {head[1]}\n"
    details += f"Head Type: {head[2]}\n"
    details += f"Head Grade: {head[3]}\n"
    details += f"Emiscode: {head[4]}\n"
    messagebox.showinfo("Head Details", details)

# Function to handle lookup button click
def lookup_head():
    try:
        head_id = int(head_id_entry.get())
        fetch_head_details(head_id)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid Head ID")

# Function to set up the GUI for looking up head details
def gui_setup():
    root = Tk()
    root.title("Lookup Head Details")

    lookup_frame = Frame(root, padx=10, pady=10)
    lookup_frame.pack(padx=50, pady=50)

    head_id_label = Label(lookup_frame, text="Head ID to Lookup:", font=("Helvetica", 16))
    head_id_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    global head_id_entry
    head_id_entry = Entry(lookup_frame, font=("Helvetica", 16))
    head_id_entry.grid(row=0, column=1, padx=10, pady=10)

    lookup_button = Button(lookup_frame, text="Lookup Head", command=lookup_head, font=("Helvetica", 16))
    lookup_button.grid(row=1, column=0, columnspan=2, pady=20)

    root.mainloop()

