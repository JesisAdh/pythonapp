# Importing the necessary modules
import mymodule as md
#to run for unlimited
while True:
    # Showing users the options
    print("""
Choose any option from below:
      1. Create records
      2. Read records
      3. Update record
      4. Delete record
      5. Export record
      6. Exit
""")

    # Prompting the user to choose an option with validation
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
        md.read_record()
        print("\nRecord(s) read successfully.\n")

    elif opt == 3:
        inputed_username = input("Enter the username of the record you want to update: ")
        input_id = md.intValidation("Enter the ID: ", "Please enter a valid integer.")
        input_username = input("Enter the username: ")
        input_email = md.emailValidation("Enter the email: ")
        input_password = input("Enter the password: ")
        md.update_record(input_id, input_username, input_email, input_password, inputed_username)
        print("\nRecord(s) updated successfully.\n")

    elif opt == 4:
        inputed_username = input("Enter the username of the record you want to delete: ")
        md.delete_record(inputed_username)
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
        