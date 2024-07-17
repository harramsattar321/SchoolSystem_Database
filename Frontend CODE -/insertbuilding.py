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

def submit_building_data():
    try:
        # Convert entries to appropriate data types
        building_id = int(building_id_entry.get())
        total_area = int(total_area_entry.get())
        covered_area = int(covered_area_entry.get())
        uncovered_area = int(uncovered_area_entry.get())
        internet = int(internet_entry.get())
        playground = int(playground_entry.get())
        total_computers = int(total_computers_entry.get())
        ece_rooms = int(ece_rooms_entry.get())
        caregivers = int(caregivers_entry.get())
        total_rooms = int(total_rooms_entry.get())
        classes = int(classes_entry.get())

        data = (building_id, total_area, covered_area, uncovered_area, internet, playground, 
                total_computers, ece_rooms, caregivers, total_rooms, classes)

        query = f"""INSERT INTO Building (Building_ID, Total_Area, Covered_Area, Uncovered_Area, Internet, Playground, 
                   Total_Computers, ECE_Rooms, Caregivers, Total_Rooms, Classes) VALUES ({building_id}, {total_area}, {covered_area}, {uncovered_area}, {internet}, {playground}, 
                {total_computers}, {ece_rooms}, {caregivers}, {total_rooms}, {classes});"""
        
        submit_data("Building", query, data)

    except ValueError as ve:
        messagebox.showerror("Input Error", f"Please enter valid integer values: {ve}")


def gui_setup():
    global building_id_entry, total_area_entry, covered_area_entry, uncovered_area_entry, internet_entry, playground_entry, total_computers_entry, ece_rooms_entry, caregivers_entry, total_rooms_entry, classes_entry

    # GUI setup
    root = Tk()
    root.title("School Data Entry Form")

    # Set window to full screen
    root.attributes('-fullscreen', True)

    # Welcome Message
    welcome_label = Label(root, text="Welcome to School System Database", font=("Helvetica", 24))
    welcome_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Building data input
    building_frame = LabelFrame(root, text="Building Data", padx=10, pady=10, font=("Helvetica", 16))
    building_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    # Configure grid layout to expand properly
    for i in range(12):
        building_frame.grid_rowconfigure(i, weight=1)
        building_frame.grid_columnconfigure(0, weight=1)
        building_frame.grid_columnconfigure(1, weight=2)

    building_id_label = Label(building_frame, text="Building ID", font=("Helvetica", 16))
    building_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    building_id_entry = Entry(building_frame, font=("Helvetica", 16))
    building_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    total_area_label = Label(building_frame, text="Total Area", font=("Helvetica", 16))
    total_area_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    total_area_entry = Entry(building_frame, font=("Helvetica", 16))
    total_area_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    covered_area_label = Label(building_frame, text="Covered Area", font=("Helvetica", 16))
    covered_area_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    covered_area_entry = Entry(building_frame, font=("Helvetica", 16))
    covered_area_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    uncovered_area_label = Label(building_frame, text="Uncovered Area", font=("Helvetica", 16))
    uncovered_area_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
    uncovered_area_entry = Entry(building_frame, font=("Helvetica", 16))
    uncovered_area_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    internet_label = Label(building_frame, text="Internet", font=("Helvetica", 16))
    internet_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
    internet_entry = Entry(building_frame, font=("Helvetica", 16))
    internet_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    playground_label = Label(building_frame, text="Playground", font=("Helvetica", 16))
    playground_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")
    playground_entry = Entry(building_frame, font=("Helvetica", 16))
    playground_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

    total_computers_label = Label(building_frame, text="Total Computers", font=("Helvetica", 16))
    total_computers_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")
    total_computers_entry = Entry(building_frame, font=("Helvetica", 16))
    total_computers_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

    ece_rooms_label = Label(building_frame, text="ECE Rooms", font=("Helvetica", 16))
    ece_rooms_label.grid(row=7, column=0, padx=5, pady=5, sticky="e")
    ece_rooms_entry = Entry(building_frame, font=("Helvetica", 16))
    ece_rooms_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")

    caregivers_label = Label(building_frame, text="Caregivers", font=("Helvetica", 16))
    caregivers_label.grid(row=8, column=0, padx=5, pady=5, sticky="e")
    caregivers_entry = Entry(building_frame, font=("Helvetica", 16))
    caregivers_entry.grid(row=8, column=1, padx=5, pady=5, sticky="w")

    total_rooms_label = Label(building_frame, text="Total Rooms", font=("Helvetica", 16))
    total_rooms_label.grid(row=9, column=0, padx=5, pady=5, sticky="e")
    total_rooms_entry = Entry(building_frame, font=("Helvetica", 16))
    total_rooms_entry.grid(row=9, column=1, padx=5, pady=5, sticky="w")

    classes_label = Label(building_frame, text="Classes", font=("Helvetica", 16))
    classes_label.grid(row=10, column=0, padx=5, pady=5, sticky="e")
    classes_entry = Entry(building_frame, font=("Helvetica", 16))
    classes_entry.grid(row=10, column=1, padx=5, pady=5, sticky="w")

    submit_building_button = Button(building_frame, text="Submit Building Data", command=submit_building_data, font=("Helvetica", 16))
    submit_building_button.grid(row=11, columnspan=2, pady=10)

    root.mainloop()
