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

# Function to retrieve building_lab details by building_id and lab_id
def fetch_building_lab_details(building_id, lab_id):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT * FROM building_lab WHERE building_id = %s AND lab_id = %s"
        cursor.execute(query, (building_id, lab_id))
        building_lab = cursor.fetchone()

        if building_lab:
            display_building_lab_details(building_lab)
        else:
            messagebox.showerror("Error", f"No record found with Building ID {building_id} and Lab ID {lab_id}")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to display building_lab details in a message box
def display_building_lab_details(building_lab):
    details = f"Building ID: {building_lab[0]}\n"
    details += f"Lab ID: {building_lab[1]}\n"
   

    messagebox.showinfo("Building Lab Details", details)

# Function to handle lookup button click
def lookup_building_lab():
    try:
        building_id = int(building_id_entry.get())
        lab_id = int(lab_id_entry.get())
        fetch_building_lab_details(building_id, lab_id)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid Building ID and Lab ID")

# Function to set up the GUI for looking up building_lab details
def gui_setup():
    root = Tk()
    root.title("Lookup Building Lab Details")

    lookup_frame = Frame(root, padx=10, pady=10)
    lookup_frame.pack(padx=50, pady=50)

    building_id_label = Label(lookup_frame, text="Building ID:", font=("Helvetica", 16))
    building_id_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    global building_id_entry
    building_id_entry = Entry(lookup_frame, font=("Helvetica", 16))
    building_id_entry.grid(row=0, column=1, padx=10, pady=10)

    lab_id_label = Label(lookup_frame, text="Lab ID:", font=("Helvetica", 16))
    lab_id_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    global lab_id_entry
    lab_id_entry = Entry(lookup_frame, font=("Helvetica", 16))
    lab_id_entry.grid(row=1, column=1, padx=10, pady=10)

    lookup_button = Button(lookup_frame, text="Lookup Building Lab", command=lookup_building_lab, font=("Helvetica", 16))
    lookup_button.grid(row=2, column=0, columnspan=2, pady=20)

    root.mainloop()

