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

# Function to handle deletion of data
def delete_data(emis_code):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = f"DELETE FROM School WHERE Emis_Code = {emis_code}; "
        cursor.execute(query)
        connection.commit()
        messagebox.showinfo("Success", f"Record with EMIS Code {emis_code} deleted successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to handle deletion button click
def delete_record():
    try:
        emis_code = int(emis_code_entry.get())
        delete_data(emis_code)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid EMIS Code")

# Function to set up the GUI for deleting records
def gui_setup():
    root = Tk()
    root.title("Delete School Record")

    delete_frame = Frame(root, padx=10, pady=10)
    delete_frame.pack(padx=50, pady=50)

    emis_code_label = Label(delete_frame, text="EMIS Code to Delete:", font=("Helvetica", 16))
    emis_code_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    global emis_code_entry
    emis_code_entry = Entry(delete_frame, font=("Helvetica", 16))
    emis_code_entry.grid(row=0, column=1, padx=10, pady=10)

    delete_button = Button(delete_frame, text="Delete Record", command=delete_record, font=("Helvetica", 16))
    delete_button.grid(row=1, column=0, columnspan=2, pady=20)

    root.mainloop()

