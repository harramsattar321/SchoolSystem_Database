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

def submit_building_lab_data():
    try:
        # Convert entries to appropriate data types
        building_id = int(building_id_entry.get())
        lab_id = int(lab_id_entry.get())

    

        query = f"""INSERT INTO Building_Lab (Building_ID, Lab_ID) VALUES ({building_id}, {lab_id});"""
        
        submit_data("Building_Lab", query)

    except ValueError as ve:
        messagebox.showerror("Input Error", f"Please enter valid integer values: {ve}")

def gui_setup():
    global building_id_entry, lab_id_entry

    # GUI setup
    root = Tk()
    root.title("Building Lab Data Entry Form")

    # Building_Lab data input
    building_lab_frame = LabelFrame(root, text="Building Lab Data", padx=10, pady=10, font=("Helvetica", 16))
    building_lab_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Configure grid layout to expand properly
    for i in range(3):
        building_lab_frame.grid_rowconfigure(i, weight=1)
        building_lab_frame.grid_columnconfigure(0, weight=1)
        building_lab_frame.grid_columnconfigure(1, weight=2)

    building_id_label = Label(building_lab_frame, text="Building ID", font=("Helvetica", 16))
    building_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    building_id_entry = Entry(building_lab_frame, font=("Helvetica", 16))
    building_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    lab_id_label = Label(building_lab_frame, text="Lab ID", font=("Helvetica", 16))
    lab_id_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    lab_id_entry = Entry(building_lab_frame, font=("Helvetica", 16))
    lab_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    submit_building_lab_button = Button(building_lab_frame, text="Submit Building Lab Data", command=submit_building_lab_data, font=("Helvetica", 16))
    submit_building_lab_button.grid(row=2, columnspan=2, pady=10)

    root.mainloop()

