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

def submit_data(table, query, data):
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

def submit_school_data():
    try:
        # Convert entries to appropriate data types
        emis_code = int(emis_code_entry.get())
        school_name = school_name_entry.get()
        school_shift = school_shift_entry.get()
        school_level = school_level_entry.get()
        establishment_year = int(establishment_year_entry.get())
        school_medium = school_medium_entry.get()
        total_teachers = int(total_teachers_entry.get())
        total_students = int(total_students_entry.get())

        data = (emis_code, school_name, school_shift, school_level, establishment_year, school_medium, total_teachers, total_students)

        query = f"""INSERT INTO School (Emis_Code, School_Name, School_Shift, School_Level, Establishment_Year, 
                   School_Medium, Total_Teachers, Total_Students) VALUES ({emis_code}, '{school_name}', '{school_shift}', '{school_level}', {establishment_year}, '{school_medium}', {total_teachers}, {total_students});"""
        
        submit_data("School", query, data)

    except ValueError as ve:
        messagebox.showerror("Input Error", f"Please enter valid data types: {ve}")

def gui_setup():
    global emis_code_entry, school_name_entry, school_shift_entry, school_level_entry, establishment_year_entry, school_medium_entry, total_teachers_entry, total_students_entry

    # GUI setup
    root = Tk()
    root.title("School Data Entry Form")

    # Set window to full screen
    root.attributes('-fullscreen', True)

    # Welcome Message
    welcome_label = Label(root, text="Welcome to School System Database", font=("Helvetica", 24))
    welcome_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # School data input
    school_frame = LabelFrame(root, text="School Data", padx=10, pady=10, font=("Helvetica", 16))
    school_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    # Configure grid layout to expand properly
    for i in range(9):
        school_frame.grid_rowconfigure(i, weight=1)
        school_frame.grid_columnconfigure(0, weight=1)
        school_frame.grid_columnconfigure(1, weight=2)

    emis_code_label = Label(school_frame, text="EMIS Code", font=("Helvetica", 16))
    emis_code_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    emis_code_entry = Entry(school_frame, font=("Helvetica", 16))
    emis_code_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    school_name_label = Label(school_frame, text="School Name", font=("Helvetica", 16))
    school_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    school_name_entry = Entry(school_frame, font=("Helvetica", 16))
    school_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    school_shift_label = Label(school_frame, text="School Shift", font=("Helvetica", 16))
    school_shift_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    school_shift_entry = Entry(school_frame, font=("Helvetica", 16))
    school_shift_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    school_level_label = Label(school_frame, text="School Level", font=("Helvetica", 16))
    school_level_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
    school_level_entry = Entry(school_frame, font=("Helvetica", 16))
    school_level_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    establishment_year_label = Label(school_frame, text="Establishment Year", font=("Helvetica", 16))
    establishment_year_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
    establishment_year_entry = Entry(school_frame, font=("Helvetica", 16))
    establishment_year_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    school_medium_label = Label(school_frame, text="School Medium", font=("Helvetica", 16))
    school_medium_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")
    school_medium_entry = Entry(school_frame, font=("Helvetica", 16))
    school_medium_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

    total_teachers_label = Label(school_frame, text="Total Teachers", font=("Helvetica", 16))
    total_teachers_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")
    total_teachers_entry = Entry(school_frame, font=("Helvetica", 16))
    total_teachers_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

    total_students_label = Label(school_frame, text="Total Students", font=("Helvetica", 16))
    total_students_label.grid(row=7, column=0, padx=5, pady=5, sticky="e")
    total_students_entry = Entry(school_frame, font=("Helvetica", 16))
    total_students_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")

    submit_school_button = Button(school_frame, text="Submit School Data", command=submit_school_data, font=("Helvetica", 16))
    submit_school_button.grid(row=8, columnspan=2, pady=10)

    root.mainloop()

# Call the GUI setup function when running the script

