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

# Function to fetch existing contact_info data based on contact_info_id
def fetch_contact_info(contact_info_id):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = f"SELECT * FROM contact_info WHERE contact_info_id = {contact_info_id}"
        cursor.execute(query)
        contact_info_data = cursor.fetchone()
        connection.close()
        return contact_info_data

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        return None

# Function to update contact_info data in the database
def update_contact_info(contact_info_id, district, city, tehsil, emis_code, markaz, moza, street_name, uc_number):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = f"""UPDATE contact_info SET
                    District = '{district}',
                    City = '{city}',
                    Tehsil = '{tehsil}',
                    Emis_Code = {emis_code},
                    Markaz = '{markaz}',
                    Moza = '{moza}',
                    Street_Name = '{street_name}',
                    UC_Number = '{uc_number}'
                    WHERE contact_info_id = {contact_info_id}"""
        cursor.execute(query)
        connection.commit()
        messagebox.showinfo("Success", f"Contact info with ID {contact_info_id} updated successfully")
        connection.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Function to handle form submission for updating contact_info record
def submit_contact_info_update():
    try:
        contact_info_id = int(contact_info_id_entry.get())
        district = district_entry.get()
        city = city_entry.get()
        tehsil = tehsil_entry.get()
        emis_code = int(emis_code_entry.get())
        markaz = markaz_entry.get()
        moza = moza_entry.get()
        street_name = street_name_entry.get()
        uc_number = uc_number_entry.get()

        update_contact_info(contact_info_id, district, city, tehsil, emis_code, markaz, moza, street_name, uc_number)
    
    except ValueError as ve:
        messagebox.showerror("Input Error", f"Invalid input: {ve}")

# Function to set up the GUI for updating contact_info record
def gui_setup():
    global contact_info_id_entry, district_entry, city_entry, tehsil_entry, emis_code_entry, markaz_entry, moza_entry, street_name_entry, uc_number_entry

    root = Tk()
    root.title("Modify Contact Info")

    # GUI setup for form
    form_frame = LabelFrame(root, text="Update Contact Info", padx=10, pady=10, font=("Helvetica", 16))
    form_frame.pack(padx=20, pady=20)

    contact_info_id_label = Label(form_frame, text="Contact Info ID:", font=("Helvetica", 14))
    contact_info_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    contact_info_id_entry = Entry(form_frame, font=("Helvetica", 14))
    contact_info_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    fetch_button = Button(form_frame, text="Fetch Data", command=fetch_and_populate_form, font=("Helvetica", 14))
    fetch_button.grid(row=0, column=2, padx=5, pady=5)

    district_label = Label(form_frame, text="District:", font=("Helvetica", 14))
    district_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    district_entry = Entry(form_frame, font=("Helvetica", 14))
    district_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    city_label = Label(form_frame, text="City:", font=("Helvetica", 14))
    city_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    city_entry = Entry(form_frame, font=("Helvetica", 14))
    city_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    tehsil_label = Label(form_frame, text="Tehsil:", font=("Helvetica", 14))
    tehsil_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
    tehsil_entry = Entry(form_frame, font=("Helvetica", 14))
    tehsil_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    emis_code_label = Label(form_frame, text="EMIS Code:", font=("Helvetica", 14))
    emis_code_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
    emis_code_entry = Entry(form_frame, font=("Helvetica", 14))
    emis_code_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    markaz_label = Label(form_frame, text="Markaz:", font=("Helvetica", 14))
    markaz_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")
    markaz_entry = Entry(form_frame, font=("Helvetica", 14))
    markaz_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

    moza_label = Label(form_frame, text="Moza:", font=("Helvetica", 14))
    moza_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")
    moza_entry = Entry(form_frame, font=("Helvetica", 14))
    moza_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

    street_name_label = Label(form_frame, text="Street Name:", font=("Helvetica", 14))
    street_name_label.grid(row=7, column=0, padx=5, pady=5, sticky="e")
    street_name_entry = Entry(form_frame, font=("Helvetica", 14))
    street_name_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")

    uc_number_label = Label(form_frame, text="UC Number:", font=("Helvetica", 14))
    uc_number_label.grid(row=8, column=0, padx=5, pady=5, sticky="e")
    uc_number_entry = Entry(form_frame, font=("Helvetica", 14))
    uc_number_entry.grid(row=8, column=1, padx=5, pady=5, sticky="w")

    submit_button = Button(form_frame, text="Update Contact Info", command=submit_contact_info_update, font=("Helvetica", 14))
    submit_button.grid(row=9, columnspan=2, pady=10)

    root.mainloop()

# Function to fetch and populate form with existing data
def fetch_and_populate_form():
    contact_info_id = int(contact_info_id_entry.get())
    contact_info_data = fetch_contact_info(contact_info_id)

    if contact_info_data:
        # Populate form fields with fetched data
        contact_info_id_entry.delete(0, END)
        contact_info_id_entry.insert(0, contact_info_data[0])  # contact_info_id
        district_entry.delete(0, END)
        district_entry.insert(0, contact_info_data[1])  # District
        city_entry.delete(0, END)
        city_entry.insert(0, contact_info_data[2])  # City
        tehsil_entry.delete(0, END)
        tehsil_entry.insert(0, contact_info_data[3])  # Tehsil
        emis_code_entry.delete(0, END)
        emis_code_entry.insert(0, contact_info_data[4])  # Emis_Code
        markaz_entry.delete(0, END)
        markaz_entry.insert(0, contact_info_data[5])  # Markaz
        moza_entry.delete(0, END)
        moza_entry.insert(0, contact_info_data[6])  # Moza
        street_name_entry.delete(0, END)
        street_name_entry.insert(0, contact_info_data[7])  # Street_Name
        uc_number_entry.delete(0, END)
        uc_number_entry.insert(0, contact_info_data[8])  # UC_Number
    else:
        messagebox.showerror("Error", f"Contact Info with ID {contact_info_id} not found")

