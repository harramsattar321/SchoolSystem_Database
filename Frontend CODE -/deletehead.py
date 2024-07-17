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
def delete_data(head_id):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "DELETE FROM Head WHERE Head_ID = %s"
        cursor.execute(query, (head_id,))
        connection.commit()
        messagebox.showinfo("Success", f"Record with Head ID {head_id} deleted successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to handle deletion button click
def delete_record():
    try:
        head_id = int(head_id_entry.get())
        delete_data(head_id)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid Head ID")

# Function to set up the GUI for deleting records
def gui_setup():
    root = Tk()
    root.title("Delete Head Record")

    delete_frame = Frame(root, padx=10, pady=10)
    delete_frame.pack(padx=50, pady=50)

    head_id_label = Label(delete_frame, text="Head ID to Delete:", font=("Helvetica", 16))
    head_id_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    global head_id_entry
    head_id_entry = Entry(delete_frame, font=("Helvetica", 16))
    head_id_entry.grid(row=0, column=1, padx=10, pady=10)

    delete_button = Button(delete_frame, text="Delete Record", command=delete_record, font=("Helvetica", 16))
    delete_button.grid(row=1, column=0, columnspan=2, pady=20)

    root.mainloop()


