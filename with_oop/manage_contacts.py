from with_oop.contacts import Contacts


class ManageContacts:

    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        self.contacts.append(Contacts(name, phone))
        print("Contact added successfully.")

    def show_contacts(self):
        if not self.contacts:
            print("No contact available")
        else:
            for contact in self.contacts:
                print(contact)

    def remove_contact(self, name):
        found = False
        for contact in self.contacts:
            if name == contact.name:
                found = True
                self.contacts.remove(contact)
                print("Contact removed successfully")
        if not found:
            print("Contact dose`nt exist")

    def edit_contact(self, name, new_name, new_phone):
        found = False
        for contact in self.contacts:
            if name == contact.name:
                found = True
                contact.name = new_name
                contact.phone = new_phone
                print('contact edited successfully')
        if not found:
            print("Contact dose`nt exist")

    def search_contact(self, name):
        found = False
        for contact in self.contacts:
            if name == contact.name:
                found = True
                print("found = ", contact)
        if not found:
            print("Contact dose`nt exist")
