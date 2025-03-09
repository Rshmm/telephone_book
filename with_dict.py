contacts = {}

while True:
    print("1- Add Contact")
    print("2- Delete Contact")
    print("3- Edit Contact")
    print("4- Show All Contacts")
    print("0- Exit")

    choice = int(input("Enter your choice : "))

    match choice:
        case 1:
            code = input("Enter contact code : ")
            if any(code == contact["code"] for contact in contacts.values()):
                print("code already exists")
            else:
                name = input("Enter contact name : ")
                phone = input("Enter contact phone : ")
                contacts[code] = {"code": code, "name": name, "phone": phone}
                print(contacts)
                print("contact added successfully")

        case 2:
            for contact in contacts.values():
                print(f"code = {contact['code']} , name = {contact['name']}, phone = {contact['phone']}")
            code = input("Enter contact code that you want to delete : ")
            if code in contacts:
                del contacts[code]
                print("contact deleted successfully")
            else:
                print("contact not found!")

        case 3:
            for contact in contacts.values():
                print(f"code = {contact['code']} , name = {contact['name']}, phone = {contact['phone']}")
            code = input("Enter contact code that you want to delete : ")
            if code in contacts:
                new_name = input("Enter new contact name : ")
                new_phone = input("Enter new contact phone : ")
                contacts[code] = {"code": code, "name": new_name, "phone": new_phone}
                print("contact edited successfully")
            else:
                print("contact not found!")

        case 4:
            for contact in contacts.values():
                print(f"code = {contact['code']} , name = {contact['name']}, phone = {contact['phone']}")

        case 0:
            exit()
