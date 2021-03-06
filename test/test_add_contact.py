# -*- coding: utf-8 -*-
from model.model_contact import Contact
import pytest

def test_add_contact(app2, db, data_contacts, check_ui):
    contact = data_contacts
    # берем длину старого списка из базы
    old_contacts = db.get_contact_list()
    # выполняем создание контакта в соответствии с локальными переменными
    app2.contact.create(contact)
    # собираем новый список контактов (после создания нового) - с UI
    new_contacts = db.get_contact_list()
    # сравниваем старый и новый списки по длине, новый == старый +1, длину старого списка берем методом count
    assert len(old_contacts) + 1 == app2.contact.count()
    #добавляем в старый список данные от нового созданного контакта (из локальных переменных)
    old_contacts.append(contact)
    # сравниваем 2 полученных списка: новый и старый с добавленным контактом
    # для того, чтобы их можно было сравнивать в model_contacts надо добавить 2 метода: __eq__ и id_or_max
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app2.contact.get_contact_list(), key=Contact.id_or_max)
#        assert new_contacts == app2.contact.get_contact_list() #раскомментировать, чтобы проверить работоспособность check_ui: если тест упал - работает


