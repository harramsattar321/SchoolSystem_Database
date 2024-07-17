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

# Function to retrieve all records from the contact_info table
def fetch_contact_info_data():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT contact_info_id, district, city, tehsil, emis_code, markaz, moza, street_name, uc_number FROM contact_info"
        cursor.execute(query)
        contact_infos = cursor.fetchall()

        display_contact_info_data(contact_infos)

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to display contact_info data in a new window
def display_contact_info_data(contact_infos):
    root = Tk()
    root.title("Contact_Info Table Data")

    tree = ttk.Treeview(root)

    tree["columns"] = ("Contact Info ID", "District", "City", "Tehsil", "EMIS Code", "Markaz", "Moza", "Street Name", "UC Number")
    tree.column("#0", width=0, stretch=NO)  # To hide the first empty column
    tree.column("Contact Info ID", anchor=CENTER, width=120)
    tree.column("District", anchor=CENTER, width=100)
    tree.column("City", anchor=CENTER, width=100)
    tree.column("Tehsil", anchor=CENTER, width=100)
    tree.column("EMIS Code", anchor=CENTER, width=100)
    tree.column("Markaz", anchor=CENTER, width=100)
    tree.column("Moza", anchor=CENTER, width=100)
    tree.column("Street Name", anchor=CENTER, width=150)
    tree.column("UC Number", anchor=CENTER, width=100)

    tree.heading("#0", text="", anchor=CENTER)
    tree.heading("Contact Info ID", text="Contact Info ID", anchor=CENTER)
    tree.heading("District", text="District", anchor=CENTER)
    tree.heading("City", text="City", anchor=CENTER)
    tree.heading("Tehsil", text="Tehsil", anchor=CENTER)
    tree.heading("EMIS Code", text="EMIS Code", anchor=CENTER)
    tree.heading("Markaz", text="Markaz", anchor=CENTER)
    tree.heading("Moza", text="Moza", anchor=CENTER)
    tree.heading("Street Name", text="Street Name", anchor=CENTER)
    tree.heading("UC Number", text="UC Number", anchor=CENTER)

    for contact_info in contact_infos:
        tree.insert("", "end", values=contact_info)

    tree.pack(expand=YES, fill=BOTH)

    root.mainloop()

# Function to handle button click to fetch and display contact_info data
def display_contact_info_table():
    fetch_contact_info_data()

# Function to set up the GUI
def gui_setup():
    root = Tk()
    root.title("Display Contact_Info Table")

    display_frame = Frame(root, padx=10, pady=10)
    display_frame.pack(padx=50, pady=50)

    display_button = Button(display_frame, text="Display Contact_Info Table", command=display_contact_info_table, font=("Helvetica", 16))
    display_button.pack(pady=20)

    root.mainloop()

