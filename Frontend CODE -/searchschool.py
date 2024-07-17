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

# Function to retrieve school details by Emis_Code
def fetch_school_details(emis_code):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "SELECT * FROM School WHERE Emis_Code = %s"
        cursor.execute(query, (emis_code,))
        school = cursor.fetchone()

        if school:
            display_school_details(school)
        else:
            messagebox.showerror("Error", f"No school found with EMIS Code {emis_code}")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to display school details in a message box
def display_school_details(school):
    details = f"EMIS Code: {school[0]}\n"
    details += f"School Name: {school[1]}\n"
    details += f"School Shift: {school[2]}\n"
    details += f"School Level: {school[3]}\n"
    details += f"Establishment Year: {school[4]}\n"
    details += f"School Medium: {school[5]}\n"
    details += f"Total Teachers: {school[6]}\n"
    details += f"Total Students: {school[7]}\n"

    messagebox.showinfo("School Details", details)

# Function to handle lookup button click
def lookup_school():
    try:
        emis_code = int(emis_code_entry.get())
        fetch_school_details(emis_code)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid EMIS Code")

# Function to set up the GUI for looking up school details
def gui_setup():
    root = Tk()
    root.title("Lookup School Details")

    lookup_frame = Frame(root, padx=10, pady=10)
    lookup_frame.pack(padx=50, pady=50)

    emis_code_label = Label(lookup_frame, text="EMIS Code to Lookup:", font=("Helvetica", 16))
    emis_code_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    global emis_code_entry
    emis_code_entry = Entry(lookup_frame, font=("Helvetica", 16))
    emis_code_entry.grid(row=0, column=1, padx=10, pady=10)

    lookup_button = Button(lookup_frame, text="Lookup School", command=lookup_school, font=("Helvetica", 16))
    lookup_button.grid(row=1, column=0, columnspan=2, pady=20)

    root.mainloop()

