from fixture.db import DbFixture

db = DbFixture(host="127.0.0.1", database="addressbook", user="root", password="")

"""
# извлекаем список групп из БД
try:
    groups = db.get_group_list()
    for group in groups:
        print(group)
    print(len(groups))
finally:
    db.destroy()

"""

try: # извлекаем список контактов из БД
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.destroy()

