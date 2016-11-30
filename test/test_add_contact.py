# -*- coding: utf-8 -*-
from model.model_contact import Contact
import pytest
from data.data_add_contact import constant as testdata

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app2, contact):
    # собираем старый список контактов
    old_contacts = app2.contact.get_contact_list()
    # выполняем создание контакта в соответствии с локальными переменными
    app2.contact.create(contact)
    # сравниваем старый и новый списки по длине, новый == старый +1, длину старого списка берем методом count
    assert len(old_contacts) + 1 == app2.contact.count()
    # собираем новый список контактов (после создания нового)
    new_contacts = app2.contact.get_contact_list()
    #добавляем в старый список данные от нового созданного контакта (из локальных переменных)
    old_contacts.append(contact)
    # сравниваем 2 полученных списка: новый и старый с добавленным контактом
    # для того, чтобы их можно было сравнивать в model_contacts надо добавить 2 метода: __eq__ и id_or_max
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

