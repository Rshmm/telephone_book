from manage_contacts import ManageContacts

manager = ManageContacts()

while True:
    print("1-Add contact \n2-Show contacts \n3-Remove contact \n4-Edit contact \n5-Search contact \n0-Exit")

    choice = int(input("Enter your choice : "))

    match choice:

        case 1:
            name = input("Enter contact name : ")
            phone = input("Enter contact phone : ")
            manager.add_contact(name, phone)
        case 2:
            manager.show_contacts()
        case 3:
            manager.show_contacts()
            name = input("Enter contact name that you wants to Remove : ")
            manager.remove_contact(name)
        case 4:
            manager.show_contacts()
            name = input("Enter contact name that you wants to Edit : ")
            new_name = input("Enter contact new name : ")
            new_phone = input("Enter contact new phone : ")
            manager.edit_contact(name, new_name, new_phone)
        case 5:
            name = input("Enter contact name that you want to find : ")
            manager.search_contact(name)
        case 0:
            exit()
