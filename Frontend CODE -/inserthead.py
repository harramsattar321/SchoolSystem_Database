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

def submit_head_data():
    try:
        # Convert entries to appropriate data types
        head_id = int(head_id_entry.get())
        head_name = head_name_entry.get()
        head_type = head_type_entry.get()
        head_grade =int( head_grade_entry.get())
        emis_code = int(emis_code_entry.get())

    

        query = f"""INSERT INTO Head (Head_ID, Head_Name, Head_Type, Head_Grade, Emis_Code) 
                   VALUES ({head_id}, '{head_name}', '{head_type}', {head_grade}, {emis_code});"""
        
        submit_data("Head", query)

    except ValueError as ve:
        messagebox.showerror("Input Error", f"Please enter valid data types: {ve}")

def gui_setup():
    global head_id_entry, head_name_entry, head_type_entry, head_grade_entry, emis_code_entry

    # GUI setup
    root = Tk()
    root.title("Head Data Entry Form")

    # Head data input
    head_frame = LabelFrame(root, text="Head Data", padx=10, pady=10, font=("Helvetica", 16))
    head_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Configure grid layout to expand properly
    for i in range(5):
        head_frame.grid_rowconfigure(i, weight=1)
        head_frame.grid_columnconfigure(0, weight=1)
        head_frame.grid_columnconfigure(1, weight=2)

    head_id_label = Label(head_frame, text="Head ID", font=("Helvetica", 16))
    head_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    head_id_entry = Entry(head_frame, font=("Helvetica", 16))
    head_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    head_name_label = Label(head_frame, text="Head Name", font=("Helvetica", 16))
    head_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    head_name_entry = Entry(head_frame, font=("Helvetica", 16))
    head_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    head_type_label = Label(head_frame, text="Head Type", font=("Helvetica", 16))
    head_type_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    head_type_entry = Entry(head_frame, font=("Helvetica", 16))
    head_type_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    head_grade_label = Label(head_frame, text="Head Grade", font=("Helvetica", 16))
    head_grade_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
    head_grade_entry = Entry(head_frame, font=("Helvetica", 16))
    head_grade_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    emis_code_label = Label(head_frame, text="EMIS Code", font=("Helvetica", 16))
    emis_code_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
    emis_code_entry = Entry(head_frame, font=("Helvetica", 16))
    emis_code_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    submit_head_button = Button(head_frame, text="Submit Head Data", command=submit_head_data, font=("Helvetica", 16))
    submit_head_button.grid(row=5, columnspan=2, pady=10)

    root.mainloop()


