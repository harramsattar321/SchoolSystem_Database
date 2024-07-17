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

def submit_contact_info_data():
    try:
        # Convert entries to appropriate data types
        contact_info_id = int(contact_info_id_entry.get())
        district = district_entry.get()
        city = city_entry.get()
        tehsil = tehsil_entry.get()
        emis_code = int(emis_code_entry.get())
        markaz = markaz_entry.get()
        moza = moza_entry.get()
        street_name = street_name_entry.get()
        uc_number = int(uc_number_entry.get())

     

        query = f"""INSERT INTO Contact_Info (Contact_Info_ID, District, City, Tehsil, Emis_Code, Markaz, Moza, Street_Name, UC_Number) 
                   VALUES ({contact_info_id}, '{district}', '{city}', '{tehsil}', {emis_code}, '{markaz}', '{moza}', '{street_name}', {uc_number});"""
        
        submit_data("Contact_Info", query)

    except ValueError as ve:
        messagebox.showerror("Input Error", f"Please enter valid data types: {ve}")

def gui_setup():
    global contact_info_id_entry, district_entry, city_entry, tehsil_entry, emis_code_entry, markaz_entry, moza_entry, street_name_entry, uc_number_entry

    # GUI setup
    root = Tk()
    root.title("Contact Info Data Entry Form")

    # Contact_Info data input
    contact_info_frame = LabelFrame(root, text="Contact Info Data", padx=10, pady=10, font=("Helvetica", 16))
    contact_info_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Configure grid layout to expand properly
    for i in range(10):
        contact_info_frame.grid_rowconfigure(i, weight=1)
        contact_info_frame.grid_columnconfigure(0, weight=1)
        contact_info_frame.grid_columnconfigure(1, weight=2)

    contact_info_id_label = Label(contact_info_frame, text="Contact Info ID", font=("Helvetica", 16))
    contact_info_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    contact_info_id_entry = Entry(contact_info_frame, font=("Helvetica", 16))
    contact_info_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    district_label = Label(contact_info_frame, text="District", font=("Helvetica", 16))
    district_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    district_entry = Entry(contact_info_frame, font=("Helvetica", 16))
    district_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    city_label = Label(contact_info_frame, text="City", font=("Helvetica", 16))
    city_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    city_entry = Entry(contact_info_frame, font=("Helvetica", 16))
    city_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    tehsil_label = Label(contact_info_frame, text="Tehsil", font=("Helvetica", 16))
    tehsil_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
    tehsil_entry = Entry(contact_info_frame, font=("Helvetica", 16))
    tehsil_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    emis_code_label = Label(contact_info_frame, text="EMIS Code", font=("Helvetica", 16))
    emis_code_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
    emis_code_entry = Entry(contact_info_frame, font=("Helvetica", 16))
    emis_code_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    markaz_label = Label(contact_info_frame, text="Markaz", font=("Helvetica", 16))
    markaz_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")
    markaz_entry = Entry(contact_info_frame, font=("Helvetica", 16))
    markaz_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

    moza_label = Label(contact_info_frame, text="Moza", font=("Helvetica", 16))
    moza_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")
    moza_entry = Entry(contact_info_frame, font=("Helvetica", 16))
    moza_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

    street_name_label = Label(contact_info_frame, text="Street Name", font=("Helvetica", 16))
    street_name_label.grid(row=7, column=0, padx=5, pady=5, sticky="e")
    street_name_entry = Entry(contact_info_frame, font=("Helvetica", 16))
    street_name_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")

    uc_number_label = Label(contact_info_frame, text="UC Number", font=("Helvetica", 16))
    uc_number_label.grid(row=8, column=0, padx=5, pady=5, sticky="e")
    uc_number_entry = Entry(contact_info_frame, font=("Helvetica", 16))
    uc_number_entry.grid(row=8, column=1, padx=5, pady=5, sticky="w")

    submit_contact_info_button = Button(contact_info_frame, text="Submit Contact Info Data", command=submit_contact_info_data, font=("Helvetica", 16))
    submit_contact_info_button.grid(row=9, columnspan=2, pady=10)

    root.mainloop()


