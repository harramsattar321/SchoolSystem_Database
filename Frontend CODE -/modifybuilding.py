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

# Function to fetch existing building data based on building_id
def fetch_building_data(building_id):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = f"SELECT * FROM Building WHERE Building_ID = {building_id}"
        cursor.execute(query)
        building_data = cursor.fetchone()
        connection.close()
        return building_data

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        return None

# Function to update building data in the database
def update_building_data(building_id, covered_area, uncovered_area, total_area, internet, caregivers, playground, classes, total_computers, ece_rooms, total_rooms, emis_code):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = f"""UPDATE Building SET
                    Covered_Area = {covered_area},
                    Uncovered_Area = {uncovered_area},
                    Total_Area = {total_area},
                    Internet = {internet},
                    Caregivers = {caregivers},
                    Playground = {playground},
                    Classes = {classes},
                    Total_Computers = {total_computers},
                    Ece_Rooms = {ece_rooms},
                    Total_Rooms = {total_rooms},
                    Emis_Code = {emis_code}
                    WHERE Building_ID = {building_id}"""
        cursor.execute(query)
        connection.commit()
        messagebox.showinfo("Success", f"Building data with ID {building_id} updated successfully")
        connection.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Function to handle form submission for updating building record
def submit_building_update():
    try:
        building_id = int(building_id_entry.get())
        covered_area = float(covered_area_entry.get())
        uncovered_area = float(uncovered_area_entry.get())
        total_area = float(total_area_entry.get())
        internet = int(internet_entry.get())
        caregivers = int(caregivers_entry.get())
        playground = int(playground_entry.get())
        classes = int(classes_entry.get())
        total_computers = int(total_computers_entry.get())
        ece_rooms = int(ece_rooms_entry.get())
        total_rooms = int(total_rooms_entry.get())
        emis_code = int(emis_code_entry.get())
        
        update_building_data(building_id, covered_area, uncovered_area, total_area, internet, caregivers, playground, classes, total_computers, ece_rooms, total_rooms, emis_code)
    
    except ValueError as ve:
        messagebox.showerror("Input Error", f"Invalid input: {ve}")

# Function to set up the GUI for updating building record
def gui_setup():
    global building_id_entry, covered_area_entry, uncovered_area_entry, total_area_entry, internet_entry, caregivers_entry, playground_entry, classes_entry, total_computers_entry, ece_rooms_entry, total_rooms_entry, emis_code_entry

    root = Tk()
    root.title("Modify Building Record")

    # GUI setup for form
    form_frame = LabelFrame(root, text="Update Building Record", padx=10, pady=10, font=("Helvetica", 16))
    form_frame.pack(padx=20, pady=20)

    building_id_label = Label(form_frame, text="Building ID:", font=("Helvetica", 14))
    building_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    building_id_entry = Entry(form_frame, font=("Helvetica", 14))
    building_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    fetch_button = Button(form_frame, text="Fetch Data", command=fetch_and_populate_form, font=("Helvetica", 14))
    fetch_button.grid(row=0, column=2, padx=5, pady=5)

    covered_area_label = Label(form_frame, text="Covered Area (sq. ft.):", font=("Helvetica", 14))
    covered_area_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    covered_area_entry = Entry(form_frame, font=("Helvetica", 14))
    covered_area_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    uncovered_area_label = Label(form_frame, text="Uncovered Area (sq. ft.):", font=("Helvetica", 14))
    uncovered_area_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    uncovered_area_entry = Entry(form_frame, font=("Helvetica", 14))
    uncovered_area_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    total_area_label = Label(form_frame, text="Total Area (sq. ft.):", font=("Helvetica", 14))
    total_area_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
    total_area_entry = Entry(form_frame, font=("Helvetica", 14))
    total_area_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    internet_label = Label(form_frame, text="Internet (1 for Yes, 0 for No):", font=("Helvetica", 14))
    internet_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
    internet_entry = Entry(form_frame, font=("Helvetica", 14))
    internet_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    caregivers_label = Label(form_frame, text="Caregivers:", font=("Helvetica", 14))
    caregivers_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")
    caregivers_entry = Entry(form_frame, font=("Helvetica", 14))
    caregivers_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

    playground_label = Label(form_frame, text="Playground (1 for Yes, 0 for No):", font=("Helvetica", 14))
    playground_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")
    playground_entry = Entry(form_frame, font=("Helvetica", 14))
    playground_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

    classes_label = Label(form_frame, text="Classes:", font=("Helvetica", 14))
    classes_label.grid(row=7, column=0, padx=5, pady=5, sticky="e")
    classes_entry = Entry(form_frame, font=("Helvetica", 14))
    classes_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")

    total_computers_label = Label(form_frame, text="Total Computers:", font=("Helvetica", 14))
    total_computers_label.grid(row=8, column=0, padx=5, pady=5, sticky="e")
    total_computers_entry = Entry(form_frame, font=("Helvetica", 14))
    total_computers_entry.grid(row=8, column=1, padx=5, pady=5, sticky="w")

    ece_rooms_label = Label(form_frame, text="ECE Rooms:", font=("Helvetica", 14))
    ece_rooms_label.grid(row=9, column=0, padx=5, pady=5, sticky="e")
    ece_rooms_entry = Entry(form_frame, font=("Helvetica", 14))
    ece_rooms_entry.grid(row=9, column=1, padx=5, pady=5, sticky="w")

    total_rooms_label = Label(form_frame, text="Total Rooms:", font=("Helvetica", 14))
    total_rooms_label.grid(row=10, column=0, padx=5, pady=5, sticky="e")
    total_rooms_entry = Entry(form_frame, font=("Helvetica", 14))
    total_rooms_entry.grid(row=10, column=1, padx=5, pady=5, sticky="w")

    emis_code_label = Label(form_frame, text="EMIS Code:", font=("Helvetica", 14))
    emis_code_label.grid(row=11, column=0, padx=5, pady=5, sticky="e")
    emis_code_entry = Entry(form_frame, font=("Helvetica", 14))
    emis_code_entry.grid(row=11, column=1, padx=5, pady=5, sticky="w")

    submit_button = Button(form_frame, text="Update Building Data", command=submit_building_update, font=("Helvetica", 14))
    submit_button.grid(row=12, columnspan=2, pady=10)

    root.mainloop()

# Function to fetch and populate form with existing data
def fetch_and_populate_form():
    building_id = int(building_id_entry.get())
    building_data = fetch_building_data(building_id)

    if building_data:
        # Populate form fields with fetched data
        building_id_entry.delete(0, END)
        building_id_entry.insert(0, building_data[0])  # Building_ID
        covered_area_entry.delete(0, END)
        covered_area_entry.insert(0, building_data[1])  # Covered_Area
        uncovered_area_entry.delete(0, END)
        uncovered_area_entry.insert(0, building_data[2])  # Uncovered_Area
        total_area_entry.delete(0, END)
        total_area_entry.insert(0, building_data[3])  # Total_Area
        internet_entry.delete(0, END)
        internet_entry.insert(0, building_data[4])  # Internet
        caregivers_entry.delete(0, END)
        caregivers_entry.insert(0, building_data[5])  # Caregivers
        playground_entry.delete(0, END)
        playground_entry.insert(0, building_data[6])  # Playground
        classes_entry.delete(0, END)
        classes_entry.insert(0, building_data[7])  # Classes
        total_computers_entry.delete(0, END)
        total_computers_entry.insert(0, building_data[8])  # Total_Computers
        ece_rooms_entry.delete(0, END)
        ece_rooms_entry.insert(0, building_data[9])  # Ece_Rooms
        total_rooms_entry.delete(0, END)
        total_rooms_entry.insert(0, building_data[10])  # Total_Rooms
        emis_code_entry.delete(0, END)
        emis_code_entry.insert(0, building_data[11])  # Emis_Code
    else:
        messagebox.showerror("Error", f"Building with ID {building_id} not found")

# If this script is run directly, execute gui_setup function
if __name__ == "__main__":
    gui_setup()
