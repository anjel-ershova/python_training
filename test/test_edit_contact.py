# -*- coding: utf-8 -*-
from random import randrange
from model.model_contact import *


def test_edit_contact(app2):
    if app2.contact.count() == 0:
        app2.contact.create(Contact(firstname2=None, middlename=None, lastname=None, nickname=None, title=None,
                                    company=None, address="111111", id=None, homephone=None, mobilephone=None, workphone=None, fax=None, email=None, email2=None, email3=None,
                                    address2=None, secondaryphone2=None, notes=None))
    old_contact_list = app2.contact.get_contact_list()
    # забираем в локальную переменную значение, которое будет присвоено firstname после модификации
    contact = Contact(firstname2="new firstname1111", lastname="new lastname1111")
    index = randrange(len(old_contact_list)) # cлучайно генерит число
    # запоминаем id элемента, который будет видоизменен
    contact.id = old_contact_list[index].id
    # меняем значение поля
    app2.contact.edit_contact_by_index(index, contact)
    # сравниваем длины списков, должны совпадать (ничего же не удаляли)
    assert len(old_contact_list) == app2.contact.count()
    # собираем новый список контактов
    new_contact_list = app2.contact.get_contact_list()
    # присваиваем первому элементу старого списка то имя, на которое его меняли
    old_contact_list[index] = contact
    # сравниваем 2 списка старый с запомненным id и именем, замененным на новое и новый
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
