contacts = []

def add_contact(name, number, email):
    contact = {
        "name": name,
        "number": number,
        "email": email
    }
    contacts.append(contact)
    print(f"contact {name} added successful")

def view_contact(contacts):
    if not contacts:
        print("No contact found")
        return
    for contact in contacts:
        print(f"Name:{contact['name']} Number: {contact['number']} email: {contact['email']}")

def search_contact(contacts, name):
    for contact in contacts:
        if contact["name"] == name:
            print(f"Name:{contact['name']} Number: {contact['number']} email: {contact['email']}")
            return
    print(f"{name} not found")

def update_contacts(name, new_number = None, new_email = None):
    for contact in contacts:
        if contact["name"]:
            if new_number:
                contact["number"] = new_number
            if new_email:
                contact["email"] = new_email
                return
    print(f"{name} not found") 

def delete_contact(contacts, name):
    for contact in contacts:
        if contact["name"]:
            contacts.remove(contact)
            print(f"{name} removed successfully")
    print(f"{name} not found")


            

