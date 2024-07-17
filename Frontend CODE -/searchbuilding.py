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

# Function to retrieve building details by building_id
def fetch_building_details(building_id):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT building_id, covered_area, uncovered_area, total_area, internet, caregivers, playground, classes, total_computers, ece_rooms, total_rooms, emis_code FROM building WHERE building_id = %s"
        cursor.execute(query, (building_id,))
        building = cursor.fetchone()

        if building:
            display_building_details(building)
        else:
            messagebox.showerror("Error", f"No building found with Building ID {building_id}")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to display building details in a message box
def display_building_details(building):
    details = f"Building ID: {building[0]}\n"
    details += f"Covered Area: {building[1]}\n"
    details += f"Uncovered Area: {building[2]}\n"
    details += f"Total Area: {building[3]}\n"
    details += f"Internet: {building[4]}\n"
    details += f"Caregivers: {building[5]}\n"
    details += f"Playground: {building[6]}\n"
    details += f"Classes: {building[7]}\n"
    details += f"Total Computers: {building[8]}\n"
    details += f"ECE Rooms: {building[9]}\n"
    details += f"Total Rooms: {building[10]}\n"
    details += f"EMIS Code: {building[11]}\n"

    messagebox.showinfo("Building Details", details)

# Function to handle lookup button click
def lookup_building():
    try:
        building_id = int(building_id_entry.get())
        fetch_building_details(building_id)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid Building ID")

# Function to set up the GUI for looking up building details
def gui_setup():
    root = Tk()
    root.title("Lookup Building Details")

    lookup_frame = Frame(root, padx=10, pady=10)
    lookup_frame.pack(padx=50, pady=50)

    building_id_label = Label(lookup_frame, text="Building ID to Lookup:", font=("Helvetica", 16))
    building_id_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    global building_id_entry
    building_id_entry = Entry(lookup_frame, font=("Helvetica", 16))
    building_id_entry.grid(row=0, column=1, padx=10, pady=10)

    lookup_button = Button(lookup_frame, text="Lookup Building", command=lookup_building, font=("Helvetica", 16))
    lookup_button.grid(row=1, column=0, columnspan=2, pady=20)

    root.mainloop()


