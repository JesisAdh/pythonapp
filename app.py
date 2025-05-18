import sqlite3 as sq
import csv
conn = sq.connect('database.db')
cursor = conn.cursor()

print("""
Choose any option from below:
      1. Create records
      2. Read records
      3. Update record
      4. Delete record
      5. Export record
      6. Exit
""")

def validation():
    global opt
    try:
        print()
        opt = int(input("Enter the option(1-6): "))
    except ValueError as e:
        print(f"Please enter the integer value.")
        validation()
validation()

# print(opt)

def create_db():
    #defining table layout
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS account (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
create_db()

def add_record(a,b,c,d):
    cursor.execute("INSERT INTO account (id,username,email,password) VALUES (?,?,?,?)",(a,b,c,d)) 
    conn.commit()

def read_record():
    cursor.execute("SELECT * FROM account")
    records = cursor.fetchall()
    for record in records:
        print(f"ID: {record[0]} Username: {record[1]} Email: {record[2]} Password: {record[3]}")

def update_record(a,b,c,d,e):
    cursor.execute("UPDATE account SET id=?,username=?,email=?,password=? WHERE username=?",(a,b,c,d,e))
    conn.commit()

def delete_record(a):
    cursor.execute("DELETE FROM account WHERE username=?", (a,))
    conn.commit()

def export_record():
    cursor.execute("SELECT * FROM account")
    records = cursor.fetchall()
    with open('exported_records.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Username", "Email", "Password"])
        writer.writerows(records)
    print("Records exported successfully to 'exported_records.csv'.")

if opt ==1:
    no_of_records = int(input("Enter the number of records you want to create: "))
    for i in range(no_of_records):
        print(f"Record {i+1}:")
        input_id = int(input("Enter the ID: "))
        input_username = input("Enter the username: ")
        input_email = input("Enter the email: ")
        input_password = input("Enter the password: ")
        add_record(input_id,input_username,input_email,input_password)
    print("""
          Record(s) added successfully.""")
    

elif opt ==2:
    read_record()
    print("""
          Record(s) read successfully.""")

elif opt ==3:
    inputed_username = input("Enter the username of the record you want to update: ")
    input_id = int(input("Enter the ID: "))
    input_username = input("Enter the username: ")
    input_email = input("Enter the email: ")
    input_password = input("Enter the password: ")
    update_record(input_id,input_username,input_email,input_password,inputed_username)
    print("""
          Record(s) updated successfully.""")
    
elif opt ==4:
    inputed_username = input("Enter the username of the record you want to delete: ")
    delete_record(inputed_username)
    print("""
          Record(s) deleted successfully.""")
    
elif opt ==5:
    export_record()
    print("""
          Record(s) exported successfully.""")

elif opt ==6:
    print("""
          Exiting the program...""")
    conn.close()