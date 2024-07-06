from module import *
def main():
    while True:
        print("1. Add a contact")
        print("2. View contacts")
        print("3. Search for a contact")
        print("4. update a contact")
        print("5. if you want to delete a contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            contact_name = input("Enter name: ")
            contact_number = input("Enter phone number: ")
            contact_email = input("Enter email address: ")
            add_contact(contact_name, contact_number, contact_email)
            
        elif choice == "2":
            view_contact(contacts)

        elif choice == "3":
            name_to_search = input("Enter a name: ")
            search_contact(contacts, name_to_search)

        elif choice == "4":
            name_to_update = input("Enter a name: ")
            new_num = input("Enter the new number: ")
            new_email = input("Enter a new email: ")
            update_contacts(name_to_update,
                            new_num if new_num else None,
                            new_email if new_email else None)
        elif choice == "5":
            name_to_delete = input("Enter a name :")
            delete_contact(contacts, name_to_delete)
        elif choice == "6":
            print("Exiting")
        else:
            print("Invalid Choice")
if __name__ == "__main__":
    main()
