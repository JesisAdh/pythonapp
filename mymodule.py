import sqlite3 as sq
import csv
import mymodule as md
def intValidation(prompt,error_msg):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_msg)
class InvalidEmailError(Exception):
    pass
def emailValidation(prompt):
    while True:
        email = input(prompt)
        if "@" in email and "." in email:
            return email.lower()
        else:
            try:
                raise InvalidEmailError("Invalid email format.")
            except InvalidEmailError as e:
                print(e)
conn = sq.connect('database.db')
cursor = conn.cursor()

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
def get_records(record_id=None):
    if record_id is not None:
        cursor.execute("SELECT * FROM account WHERE id = ?", (record_id,))
    else:
        cursor.execute("SELECT * FROM account")
    return cursor.fetchall()
def update_record(a,b,c,d,e):
    cursor.execute("UPDATE account SET id=?,username=?,email=?,password=? WHERE id=?",(a,b,c,d,e))
    conn.commit()
def delete_record(a):
    cursor.execute("DELETE FROM account WHERE id=?", (a,))
    conn.commit()
def export_record():
    cursor.execute("SELECT * FROM account")
    records = cursor.fetchall()
    with open('exported_records.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Username", "Email", "Password"])
        writer.writerows(records)
    print("Records exported successfully to 'exported_records.csv'.")
def close_db():
    conn.close()