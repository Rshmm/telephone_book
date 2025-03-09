contacts = []


def add_contact(name, phone):
    contacts.append([name, phone])
    print("contact added successfully")


def remove_contact(name):
    found = False
    for contact in contacts:
        if contact[0] == name:
            found = True
            contacts.remove(contact)
            print("contact removed successfully")
    if not found:
        print("contact dose`nt exist")


def edit_contact(name, new_name, new_phone):
    found = False
    for contact in contacts:
        if contact[0] == name:
            found = True
            contact[0] = new_name
            contact[1] = new_phone
            print("Contact edited successfully")
    if not found:
        print("contact dose`nt exist")


def search_contact(name):
    found = False
    for contact in contacts:
        found = True
        if contact[0] == name:
            print(f"contact found : name = {contact[0]} \t phone = {contact[1]}")

    if not found:
        print("contact dose`nt exist")


def show_contacts():
    for index, contact in enumerate(contacts):
        print(index + 1, f"name = {contact[0]} \t phone = {contact[1]} ")


