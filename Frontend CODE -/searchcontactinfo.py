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

# Function to retrieve contact info details by contact_info_id
def fetch_contact_info_details(contact_info_id):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT * FROM contact_info WHERE contact_info_id = %s"
        cursor.execute(query, (contact_info_id,))
        contact_info = cursor.fetchone()

        if contact_info:
            display_contact_info_details(contact_info)
        else:
            messagebox.showerror("Error", f"No contact info found with Contact Info ID {contact_info_id}")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to display contact info details in a message box
def display_contact_info_details(contact_info):
    details = f"Contact Info ID: {contact_info[0]}\n"
    details += f"District: {contact_info[1]}\n"
    details += f"City: {contact_info[2]}\n"
    details += f"Tehsil: {contact_info[3]}\n"
    details += f"Emis_Code: {contact_info[4]}\n"
    details += f"Markaz: {contact_info[5]}\n"
    details += f"Moza: {contact_info[6]}\n"
    details += f"Street_Name: {contact_info[7]}\n"
    details += f" UC_Number: {contact_info[8]}\n"

    messagebox.showinfo("Contact Info Details", details)

# Function to handle lookup button click
def lookup_contact_info():
    try:
        contact_info_id = int(contact_info_id_entry.get())
        fetch_contact_info_details(contact_info_id)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid Contact Info ID")

# Function to set up the GUI for looking up contact info details
def gui_setup():
    root = Tk()
    root.title("Lookup Contact Info Details")

    lookup_frame = Frame(root, padx=10, pady=10)
    lookup_frame.pack(padx=50, pady=50)

    contact_info_id_label = Label(lookup_frame, text="Contact Info ID to Lookup:", font=("Helvetica", 16))
    contact_info_id_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    global contact_info_id_entry
    contact_info_id_entry = Entry(lookup_frame, font=("Helvetica", 16))
    contact_info_id_entry.grid(row=0, column=1, padx=10, pady=10)

    lookup_button = Button(lookup_frame, text="Lookup Contact Info", command=lookup_contact_info, font=("Helvetica", 16))
    lookup_button.grid(row=1, column=0, columnspan=2, pady=20)

    root.mainloop()


