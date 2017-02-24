# -*- coding: utf-8 -*-
import random
from model.model_contact import *


def test_edit_contact(app2, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app2.contact.create(Contact(firstname2=None, middlename=None, lastname=None, nickname=None, title=None,
                                    company=None, address="111111", id=None, home=None, mobile=None, work=None, fax=None, email=None, email2=None, email3=None,
                                    address2=None, phone2=None, notes=None))
    # берем из ui
    old_contacts = app2.contact.get_contact_list()
    contact_N = random.choice(old_contacts)
    new_contact_data = Contact(firstname2="new firstname0045676430", lastname="new lastname0")
    app2.contact.edit_contact_by_id(contact_N.id, new_contact_data)
    # берем из базы новый список
    new_contacts = db.get_contact_list()
    # сравниваем длины списков бд и UI
    assert len(old_contacts) == app2.contact.count()
#    old_contacts.remove(contact_N)
#    new_contacts.remove(new_contact_data)
#    второй вариант выравнивания списков бд
    old_contacts.remove(contact_N)
    old_contacts.append(new_contact_data)
    new_contact_data.id = str(contact_N.id)
    # сравниваем 2 списка из базы
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app2.contact.get_contact_list(), key=Contact.id_or_max)
