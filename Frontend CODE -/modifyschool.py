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

# Function to fetch existing school data based on EMIS code
def fetch_school_data(emis_code):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = f"SELECT * FROM School WHERE Emis_Code = {emis_code}"
        cursor.execute(query)
        school_data = cursor.fetchone()
        connection.close()
        return school_data

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        return None

# Function to update school data in the database
def update_school_data(emis_code, school_name, school_shift, school_level, establishment_year, school_medium, total_teachers, total_students):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = f"""UPDATE School SET
                    School_Name = '{school_name}',
                    School_Shift = '{school_shift}',
                    School_Level = '{school_level}',
                    Establishment_Year = {establishment_year},
                    School_Medium = '{school_medium}',
                    Total_Teachers = {total_teachers},
                    Total_Students = {total_students}
                    WHERE Emis_Code = {emis_code}"""
        cursor.execute(query)
        connection.commit()
        messagebox.showinfo("Success", f"School data with EMIS code {emis_code} updated successfully")
        connection.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Function to handle form submission for updating school record
def submit_school_update():
    emis_code = int(emis_code_entry.get())
    school_name = school_name_entry.get()
    school_shift = school_shift_entry.get()
    school_level = school_level_entry.get()
    establishment_year = int(establishment_year_entry.get())
    school_medium = school_medium_entry.get()
    total_teachers = int(total_teachers_entry.get())
    total_students = int(total_students_entry.get())

    update_school_data(emis_code, school_name, school_shift, school_level, establishment_year, school_medium, total_teachers, total_students)

# Function to set up the GUI for updating school record
def gui_setup():
    root = Tk()
    root.title("Modify School Record")

    # GUI setup for form
    form_frame = LabelFrame(root, text="Update School Record", padx=10, pady=10, font=("Helvetica", 16))
    form_frame.pack(padx=20, pady=20)

    emis_code_label = Label(form_frame, text="EMIS Code:", font=("Helvetica", 14))
    emis_code_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    emis_code_entry = Entry(form_frame, font=("Helvetica", 14))
    emis_code_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    fetch_button = Button(form_frame, text="Fetch Data", command=fetch_and_populate_form, font=("Helvetica", 14))
    fetch_button.grid(row=0, column=2, padx=5, pady=5)

    school_name_label = Label(form_frame, text="School Name:", font=("Helvetica", 14))
    school_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    school_name_entry = Entry(form_frame, font=("Helvetica", 14))
    school_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    school_shift_label = Label(form_frame, text="School Shift:", font=("Helvetica", 14))
    school_shift_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    school_shift_entry = Entry(form_frame, font=("Helvetica", 14))
    school_shift_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    school_level_label = Label(form_frame, text="School Level:", font=("Helvetica", 14))
    school_level_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
    school_level_entry = Entry(form_frame, font=("Helvetica", 14))
    school_level_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    establishment_year_label = Label(form_frame, text="Establishment Year:", font=("Helvetica", 14))
    establishment_year_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
    establishment_year_entry = Entry(form_frame, font=("Helvetica", 14))
    establishment_year_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    school_medium_label = Label(form_frame, text="School Medium:", font=("Helvetica", 14))
    school_medium_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")
    school_medium_entry = Entry(form_frame, font=("Helvetica", 14))
    school_medium_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

    total_teachers_label = Label(form_frame, text="Total Teachers:", font=("Helvetica", 14))
    total_teachers_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")
    total_teachers_entry = Entry(form_frame, font=("Helvetica", 14))
    total_teachers_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

    total_students_label = Label(form_frame, text="Total Students:", font=("Helvetica", 14))
    total_students_label.grid(row=7, column=0, padx=5, pady=5, sticky="e")
    total_students_entry = Entry(form_frame, font=("Helvetica", 14))
    total_students_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")

    submit_button = Button(form_frame, text="Update School Data", command=submit_school_update, font=("Helvetica", 14))
    submit_button.grid(row=8, columnspan=2, pady=10)

    root.mainloop()

# Function to fetch data based on EMIS code and populate the form
def fetch_and_populate_form():
    emis_code = int(emis_code_entry.get())
    school_data = fetch_school_data(emis_code)
    if school_data:
        emis_code_entry.delete(0, END)
        emis_code_entry.insert(0, str(school_data[0]))
        school_name_entry.delete(0, END)
        school_name_entry.insert(0, school_data[1])
        school_shift_entry.delete(0, END)
        school_shift_entry.insert(0, school_data[2])
        school_level_entry.delete(0, END)
        school_level_entry.insert(0, school_data[3])
        establishment_year_entry.delete(0, END)
        establishment_year_entry.insert(0, str(school_data[4]))
        school_medium_entry.delete(0, END)
        school_medium_entry.insert(0, school_data[5])
        total_teachers_entry.delete(0, END)
        total_teachers_entry.insert(0, str(school_data[6]))
        total_students_entry.delete(0, END)
        total_students_entry.insert(0, str(school_data[7]))
    else:
        messagebox.showerror("Error", f"School with EMIS code {emis_code} not found")

# Function to set up the GUI for updating school record
def gui_setup():
    global emis_code_entry, school_name_entry, school_shift_entry, school_level_entry, establishment_year_entry, school_medium_entry, total_teachers_entry, total_students_entry

    root = Tk()
    root.title("Modify School Record")

    # GUI setup for form
    form_frame = LabelFrame(root, text="Update School Record", padx=10, pady=10, font=("Helvetica", 16))
    form_frame.pack(padx=20, pady=20)

    emis_code_label = Label(form_frame, text="EMIS Code:", font=("Helvetica", 14))
    emis_code_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    emis_code_entry = Entry(form_frame, font=("Helvetica", 14))
    emis_code_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    fetch_button = Button(form_frame, text="Fetch Data", command=fetch_and_populate_form, font=("Helvetica", 14))
    fetch_button.grid(row=0, column=2, padx=5, pady=5)

    school_name_label = Label(form_frame, text="School Name:", font=("Helvetica", 14))
    school_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    school_name_entry = Entry(form_frame, font=("Helvetica", 14))
    school_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    school_shift_label = Label(form_frame, text="School Shift:", font=("Helvetica", 14))
    school_shift_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    school_shift_entry = Entry(form_frame, font=("Helvetica", 14))
    school_shift_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    school_level_label = Label(form_frame, text="School Level:", font=("Helvetica", 14))
    school_level_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
    school_level_entry = Entry(form_frame, font=("Helvetica", 14))
    school_level_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    establishment_year_label = Label(form_frame, text="Establishment Year:", font=("Helvetica", 14))
    establishment_year_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
    establishment_year_entry = Entry(form_frame, font=("Helvetica", 14))
    establishment_year_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    school_medium_label = Label(form_frame, text="School Medium:", font=("Helvetica", 14))
    school_medium_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")
    school_medium_entry = Entry(form_frame, font=("Helvetica", 14))
    school_medium_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

    total_teachers_label = Label(form_frame, text="Total Teachers:", font=("Helvetica", 14))
    total_teachers_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")
    total_teachers_entry = Entry(form_frame, font=("Helvetica", 14))
    total_teachers_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

    total_students_label = Label(form_frame, text="Total Students:", font=("Helvetica", 14))
    total_students_label.grid(row=7, column=0, padx=5, pady=5, sticky="e")
    total_students_entry = Entry(form_frame, font=("Helvetica", 14))
    total_students_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")

    submit_button = Button(form_frame, text="Update School Data", command=submit_school_update, font=("Helvetica", 14))
    submit_button.grid(row=8, columnspan=2, pady=10)

    root.mainloop()


