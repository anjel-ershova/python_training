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
    contact = random.choice(old_contacts)
    new_contact_data = Contact(firstname2="new firstname1111", lastname="new lastname1111")
    app2.contact.edit_contact_by_id(contact.id, new_contact_data)
    # берем из базы
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#    # запоминаем id элемента, который будет видоизменен
#    contact.id = old_contact_list[index].id
#    # меняем значение поля
#    app2.contact.edit_contact_by_index(index, contact)
#    # присваиваем первому элементу старого списка то имя, на которое его меняли
#    old_contact_list[index] = contact
#    # сравниваем 2 списка старый с запомненным id и именем, замененным на новое и новый
#    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
