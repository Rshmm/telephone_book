contacts = []

while True:
    print("*" * 50)

    print("1-Add contact")
    print("2-show contacts")
    print("3-Remove contact")
    print("4-Edit contact")
    print("5-search contact")
    print("0-exit")

    print("*" * 50)

    choice = int(input("Enter your choice : "))

    match choice:

        case 1:
            code = input("Enter contact`s code : ")
            if any(code == contact[0] for contact in contacts):
                print("code already exist")
            else:
                name = input("enter contact`s name : ")
                phone = input("enter contact`s phone : ")
                contacts.append([code, name, phone])
                print("contact added successfully")
        case 2:
            for contact in contacts:
                print(f"code = {contact[0]}, name = {contact[1]}, phone = {contact[2]}")
        case 3:
            for contact in contacts:
                print(f"code = {contact[0]}, name = {contact[1]}, phone = {contact[2]}")
            code = input("Enter contact code that you want to remove : ")
            found = False
            for contact in contacts:
                if code == contact[0]:
                    found = True
                    contacts.remove(contact)
                    print("contact removed successfully")
                    break
            if not found:
                print("contact dose`nt exist")
        case 4:
            for contact in contacts:
                print(f"code = {contact[0]}, name = {contact[1]}, phone = {contact[2]}")
            code = input("Enter contact code that you want to edit : ")
            found = False
            for contact in contacts:
                if code == contact[0]:
                    found = True
                    new_name = input("Enter contact new name : ")
                    new_phone = input("Enter contact new phone : ")
                    contact[1] = new_name
                    contact[2] = new_phone
                    print("contact edited successfully")
                    break
            if not found:
                print("contact dose`nt exist")

        case 5:
            name = input("Enter contact name that you want to find : ")
            found = False
            for contact in contacts:
                if name == contact[1]:
                    found =True
                    print(f" found ! == code = {contact[0]}, name = {contact[1]}, phone = {contact[2]}")
                    break
            if not found:
                print("contact dose`nt exist")
        case 0:
            exit()
