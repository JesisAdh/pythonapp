import mymodule as md
while True:
    print("""
Choose any option from below:
      1. Create records
      2. Read records
      3. Update record
      4. Delete record
      5. Export record
      6. Exit
""")
    opt = md.intValidation("Enter the option(1-6): ", "Please enter a valid option between 1 and 6.")
    if opt == 1:
        no_of_records = md.intValidation("How many records would you like to add? ", "Please enter a valid integer.")
        for i in range(no_of_records):
            print(f"Record {i + 1}:")
            input_id = md.intValidation("Enter the ID: ", "Please enter a valid integer for ID.")
            input_username = input("Enter the username: ")
            input_email = md.emailValidation("Enter the email: ")
            input_password = input("Enter the password: ")
            md.add_record(input_id, input_username, input_email, input_password)
        print("\nRecord(s) added successfully.\n")
    elif opt == 2:
        choice = input("Do you want to read a specific record by ID? (y/n): ").strip().lower()
        if choice == 'y':
            inputed_id = md.intValidation("Enter the ID: ", "Please enter a valid integer ID.")
            records = md.get_records(inputed_id)
        else:
            records = md.get_records()

        if records:
            for record in records:
                print(f"ID: {record[0]} Username: {record[1]} Email: {record[2]} Password: {record[3]}")
        else:
            print("No record(s) found.")
        print("\nRecord(s) read successfully.\n")
    elif opt == 3:
        inputed_id = input("Enter the user ID of the record you want to update: ")
        records = md.get_records()
        record_found = False

        for record in records:
            if str(record[0]) == inputed_id:
                record_found = True
                print(f"""
Which field do you want to update?
  1. ID: {record[0]}
  2. Username: {record[1]}
  3. Email: {record[2]}
  4. Password: {record[3]}
  5. All fields
""")
                choice = md.intValidation("Choose an option to update (1-5): ", "Please enter a valid option between 1 and 5.")
                new_id, new_username, new_email, new_password = record[0], record[1], record[2], record[3]

                if choice == 1:
                    new_id = md.intValidation("Enter the new ID: ", "Please enter a valid integer for ID.")
                elif choice == 2:
                    new_username = input("Enter the new username: ")
                elif choice == 3:
                    new_email = md.emailValidation("Enter the new email: ")
                elif choice == 4:
                    new_password = input("Enter the new password: ")
                elif choice == 5:
                    new_id = md.intValidation("Enter the new ID: ", "Please enter a valid integer for ID.")
                    new_username = input("Enter the new username: ")
                    new_email = md.emailValidation("Enter the new email: ")
                    new_password = input("Enter the new password: ")

                md.update_record(new_id, new_username, new_email, new_password, inputed_id)
                print("\nRecord updated successfully.\n")
                break

        if not record_found:
            print("There is no such record with the given ID.\n")


    elif opt == 4:
        inputed_id = input("Enter the user ID of the record you want to delete: ")
        md.delete_record(inputed_id)
        print("\nRecord(s) deleted successfully.\n")

    elif opt == 5:
        md.export_record()
        print("\nRecord(s) exported successfully.\n")

    elif opt == 6:
        print("\nExiting the program...\n")
        md.close_db()
        break  # This ends the while loop and exits the program
    else:
        print("\nInvalid option. Please try again.\n")