from with_oop.contacts import Contacts
from with_oop.manage_contacts import manageContacts

manager = manageContacts()

c1 = manager.add_contact("Arsham" , 12345)
c2 = manager.add_contact("Reza" , 3456)
c3 = manager.add_contact("Ali" , 5675)
c4 = manager.add_contact("Mohamadmreza" , 3456)
c5 = manager.add_contact("Alireza" , 6578)


manager.show_contacts()
# print(manager.contacts)
manager.remove_contact("Arsham")
manager.edit_contact("Reza","Arsham",12345)
manager.show_contacts()
manager.search_contact("Arsham")
