from with_func.Modul import *


while True:
    print("\n1. add contact \n2. remove contact \n3. edit contact \n4. search contact \n5. show all \n6. exit")
    choice = input("enter your choice : ")

    if choice == "1":
        name = input("Enter contact name : ")
        phone = input("Enter contact phone : ")
        add_contact(name, phone)
    elif choice == "2":
        name = input("Enter contact name that you wants to remove :  ")
        remove_contact(name)
    elif choice == "3":
        name = input("Enter contact name that you wants to edit :   ")
        new_name = input("Enter new contact name :  ")
        new_phone = input("Enter new contact phone :  ")
        edit_contact(name, new_name, new_phone)
    elif choice == "4":
        name = input("Enter person name that you wants to search :  ")
        search_contact(name)
    elif choice == "5":
        show_contacts()
    elif choice == "6":
        print("exit")
        break
    else:
        print("Invalid input! try again ... ")
