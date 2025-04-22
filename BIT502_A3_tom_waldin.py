# Import modules
import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Connect to our database (or create a new one if none exists)

conn = sqlite3.connect("gym_database.db")

cursor = conn.cursor()

# Create the database
cursor.execute('''CREATE TABLE IF NOT EXISTS Memberships (
                    MemberID INTEGER PRIMARY KEY NOT NULL,
                    First_Name TEXT NOT NULL,
                    Last_Name TEXT NOT NULL,
                    Address TEXT NOT NULL,
                    Mobile TEXT NOT NULL,
                    Membership_Type TEXT NOT NULL,
                    Membership_Duration TEXT NOT NULL,
                    Direct_Debit BOOLEAN NOT NULL,
                    Extra_1 BOOLEAN NOT NULL,
                    Extra_2 BOOLEAN NOT NULL,
                    Extra_3 BOOLEAN NOT NULL,
                    Extra_4 BOOLEAN NOT NULL,
                    Payment_Frequency TEXT NOT NULL
                    )''')


# Basic insert new member function
def insert_new_member(First_Name, Last_Name, Address, Mobile, Membership_Type, Membership_Duration, Direct_Debit, Extra_1, Extra_2, Extra_3, Extra_4, Payment_Frequency):
    cursor.execute('''INSERT INTO Memberships (First_Name, Last_Name, Address, Mobile, Membership_Type, Membership_Duration, Direct_Debit, Extra_1, Extra_2, Extra_3, Extra_4, Payment_Frequency)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (First_Name, Last_Name, Address, Mobile, Membership_Type, Membership_Duration, Direct_Debit, Extra_1, Extra_2, Extra_3, Extra_4, Payment_Frequency))
   

# Populate the database with some data
#insert_new_member("Chris", "Redfield", "21 Patrick St", "555-3840", "Basic", "3 Months", False, True, False, False, True, "Weekly")
#insert_new_member("Jill", "Valentine", "16 Houston St", "555-3350", "Regular", "6 Months", True, False, False, True, True, "Weekly")
#insert_new_member("Sherlock", "Holmes", "221B Baker St, London", "39857693", "Premium", "12 Months", True, False, False, False, True, "Monthly")
#insert_new_member("Frank", "West", "19 Hitch Ln, Willamette", "555-3947", "Regular", "3 Months", True, False, False, True, False, "Weekly")
#insert_new_member("Atticus", "Finch", "98 Windfall Rd, Tirau", "555-9827", "Basic", "6 Months", False, False, True, True, True, "Monthly")
#insert_new_member("Dorothy", "Gale", "1 Yellow St, Warkworth", "555-1984", "Basic", "12 Months", True, True, True, True, False, "Monthly")
#insert_new_member("Steven", "Rogers", "32 Frost Cr, Hamilton", "555-1920", "Premium", "12 Months", False, True, True, True, True, "Monthly")

# GUI structure and function
def main_screen():
    window = tk.Tk()
    window.title("City Gym Membership")

    tk.Label(window, text="Welcome to City Gym").grid(row=0, column=1)
    tk.Button(window, text="Membership Form", command=membership_form).grid(row=1, column=0)
    tk.Button(window, text="Search", command=search_form).grid(row=1, column=1)
    tk.Button(window, text="Statistics", command=statistics_form).grid(row=1, column=2)
    tk.Button(window, text="Help", command=help_screen).grid(row=2, column=1)

    window.mainloop()

def membership_form():
    membership_window = tk.Toplevel()
    membership_window.title("City Gym Membership Form")

    # User entry fields

    tk.Label(membership_window, text="First Name:").grid(row=0, column=0)
    entry_first_name = tk.Entry(membership_window)
    entry_first_name.grid(row=0, column=1)

    tk.Label(membership_window, text="Last Name:").grid(row=1, column=0)
    entry_last_name = tk.Entry(membership_window)
    entry_last_name.grid(row=1, column=1)

    tk.Label(membership_window, text="Address:").grid(row=2, column=0)
    entry_address = tk.Entry(membership_window)
    entry_address.grid(row=2, column=1)

    tk.Label(membership_window, text="Mobile:").grid(row=3, column=0)
    entry_mobile = tk.Entry(membership_window)
    entry_mobile.grid(row=3, column=1)

    tk.Label(membership_window, text="Membership Type:").grid(row=4, column=0)
    member_type = tk.StringVar(value='Basic')
    tk.OptionMenu(membership_window, member_type, "Basic", "Regular", "Premium").grid(row=4, column=1)

    tk.Label(membership_window, text="Membership Duration Duration:").grid(row=5, column=0)
    membership_duration = tk.StringVar(value='3 Months')
    tk.OptionMenu(membership_window, membership_duration, "3 Months", "6 Months", "12 Months").grid(row=5, column=1)    

    tk.Label(membership_window, text="Direct Debit:").grid(row=6, column=0)
    var_dd = tk.IntVar()
    direct_debit = tk.Checkbutton(membership_window, variable=var_dd)
    direct_debit.grid(row=6, column=1)

    tk.Label(membership_window, text="24/7 Access:").grid(row=7, column=0)
    var1 = tk.IntVar()
    extra1 = tk.Checkbutton(membership_window, variable=var1)
    extra1.grid(row=7, column=1)

    tk.Label(membership_window, text="Personal Trainer:").grid(row=8, column=0)
    var2 = tk.IntVar()
    extra2 = tk.Checkbutton(membership_window, variable=var2)
    extra2.grid(row=8, column=1)

    tk.Label(membership_window, text="Diet Consultation:").grid(row=9, column=0)
    var3 = tk.IntVar()
    extra3 = tk.Checkbutton(membership_window, variable=var3)
    extra3.grid(row=9, column=1)

    tk.Label(membership_window, text="Online Fitness Videos:").grid(row=10, column=0)
    var4 = tk.IntVar()
    extra4 = tk.Checkbutton(membership_window, variable=var4)
    extra4.grid(row=10, column=1)
   
    tk.Label(membership_window, text="Payment Frequency:").grid(row=11, column=0)
    payment_frequency = tk.StringVar(value='Weekly')
    tk.OptionMenu(membership_window, payment_frequency, "Weekly", "Monthly").grid(row=11, column=1)

    # Functions for buttons

    def calculate():
        """Calculate total cost and show the user in a messagebox"""
        # Assign a numeric cost value based on the membership type
        membership = 0
        if member_type.get() == 'Basic':
            membership = 10
        elif member_type.get() == 'Regular':
            membership = 15
        else:
            membership = 20

        # Calculate extras
        extras = 0
        if var1.get():
            extras += 1
        if var2.get():
            extras += 20
        if var3.get():
            extras += 20
        if var4.get():
            extras += 2

        # Calculate discounts
        discount = 0
        if membership_duration.get() == '6 months':
            discount += 2
        if membership_duration.get() == '12 months':
            discount += 5 
        if var_dd.get():
            discount += membership * 0.01
            dd = "Direct debit"
        else:
            dd = "Not direct debit"
    
        # Calculate total and regular payment 
        total = membership + extras - discount
        if payment_frequency.get() == 'Monthly':
            total = total * 4
            discount = discount * 4
        
        messagebox.showinfo("Calculation", "This plan will require {} payments of ${}.\n This includes a discount of ${} due to a long membership and/or direct debit payments.".format(payment_frequency.get().lower(), total, discount))

    def submit():
        """Check that the users inputs are valid and write them to a database"""
        if not entry_first_name.get().isalpha() or not entry_last_name.get().isalpha() or not entry_mobile.get().isdigit() or not entry_address.get():
            messagebox.showwarning("Warning", "Fields empty or invalid")
            return 
        insert_new_member(entry_first_name.get(), entry_last_name.get(), entry_address.get(), entry_mobile.get(), member_type.get(), membership_duration.get(), var_dd.get(), var1.get(), var2.get(), var3.get(), var4.get(), payment_frequency.get())
        messagebox.showinfo("Submitted", "Form submitted successfully")
        membership_window.destroy()

    tk.Button(membership_window, text="Calculate", command=calculate).grid(row=12, column=0)
    tk.Button(membership_window, text="Submit", command=submit).grid(row=12, column=1)

def search_form():
    def search_members():
        name = name_entry.get()
        membership_type = type_var.get()
        query = "SELECT * FROM Memberships WHERE First_Name LIKE ? OR Last_Name LIKE ? OR Membership_Type = ?"
        params = (f"%{name}%", f"%{name}%", membership_type)
        
        conn = sqlite3.connect("C:/Users/Tom/Desktop/gym_database.db")
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()
        
        for row in tree.get_children():
            tree.delete(row)
        
        if results:
            for member in results:
                tree.insert("", "end", values=member)
        else:
            messagebox.showinfo("No Results", "No members found with the given criteria.")

    search_window = tk.Toplevel()
    search_window.title("Search Members")
    
    tk.Label(search_window, text="Name:").grid(row=0, column=0)
    name_entry = tk.Entry(search_window)
    name_entry.grid(row=0, column=1)
    
    tk.Label(search_window, text="Membership Type:").grid(row=1, column=0)
    type_var = tk.StringVar()
    membership_dropdown = ttk.Combobox(search_window, textvariable=type_var, values=["", "Basic", "Regular", "Premium"])
    membership_dropdown.grid(row=1, column=1)
    
    tk.Button(search_window, text="Search", command=search_members).grid(row=2, column=1)
    
    tree = ttk.Treeview(search_window, columns=("ID", "First Name", "Last Name", "Address", "Mobile", "Type", "Duration", "Direct Debit", "Extra 1", "Extra 2", "Extra 3", "Extra 4", "Frequency"), show="headings")
    
    columns = ["ID", "First Name", "Last Name", "Address", "Mobile", "Type", "Duration", "Direct Debit", "Extra 1", "Extra 2", "Extra 3", "Extra 4", "Frequency"]
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    
    tree.grid(row=3, column=0, columnspan=2)

def statistics_form():
    conn = sqlite3.connect("C:/Users/Tom/Desktop/gym_database.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM Memberships")
    total_members = cursor.fetchone()[0]
    
    cursor.execute("SELECT Membership_Type, COUNT(*) FROM Memberships GROUP BY Membership_Type")
    membership_counts = cursor.fetchall()
    
    cursor.execute("SELECT COUNT(*) FROM Memberships WHERE Direct_Debit = 1")
    direct_debit_count = cursor.fetchone()[0]
    
    extra_counts = []
    for i in range(1, 5):
        cursor.execute(f"SELECT COUNT(*) FROM Memberships WHERE Extra_{i} = 1")
        extra_counts.append(cursor.fetchone()[0])
    
    conn.close()
    
    stats_window = tk.Toplevel()
    stats_window.title("Membership Statistics")
    
    tk.Label(stats_window, text=f"Total Members: {total_members}").pack()
    
    for membership_type, count in membership_counts:
        tk.Label(stats_window, text=f"{membership_type} Members: {count}").pack()
    
    for i, count in enumerate(extra_counts, start=1):
        tk.Label(stats_window, text=f"Extra {i} Selected: {count}").pack()
    
    tk.Label(stats_window, text=f"Members with Direct Debit: {direct_debit_count}").pack()

def help_screen():
    help_window = tk.Toplevel()
    help_window.title("Help")
    tk.Label(help_window, text="This is the help section. Contact support for assistance.").pack()

if __name__ == "__main__":
    main_screen()

# Close the database before exiting
conn.commit()
conn.close()