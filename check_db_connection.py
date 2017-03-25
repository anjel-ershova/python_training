from fixture.orm import ORMFixture
from model.model_group import Group
from model.model_contact import Contact


db = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    l = db.get_contacts_not_in_group(Group(id='559'))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass

"""
# извлекаем список групп из БД
try:
    groups = db.get_group_list()
    for group in groups:
        print(group)
    print(len(groups))
finally:
    pass #db.destroy() - orm автоматически закрывает соединение с БД



try: # извлекаем список контактов из БД
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    pass #db.destroy() - orm автоматически закрывает соединение с БД
"""