# -*- coding: utf-8 -*-
from model.model_contact import Contact


def test_add_contact(app2):
    # собираем старый список контактов
    old_contacts = app2.contact.get_contact_list()
    # выносим данные контакта в локальную переменную
    contact_data = Contact(firstname2="firstname2", middlename="middlename", lastname="lastname", nickname="nickname", title="title",
                 company="company", address="address", home="555-5678", mobile="8-800-200-555-500", work="555-work", fax="812-123-23-34", email="email@mfsa.ru",
                           email2="email2@mfsa.ru", email3="email3@mfsa.ru",
                 address2="Another address", home2="home_secondary", notes="Some text")
    # выполняем создание контакта в соответствии с локальными переменными
    app2.contact.create(contact_data)
    # собираем новый список контактов (после создания нового)
    new_contacts = app2.contact.get_contact_list()
    # сравниваем старый и новый списки по длине, новый == старый +1
    assert len(old_contacts) + 1 == len(new_contacts)
    #добавляем в старый список данные от нового созданного контакта (из локальных переменных)
    old_contacts.append(contact_data)
    # сравниваем 2 полученных списка: новый и старый с добавленным контактом
    # для того, чтобы их можно было сравнивать в model_contacts надо добавить 2 метода: __eq__ и id_or_max
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#Просто тест создания пустого контакта, без излишеств
def test_add_empty_contact(app2):
    # все же заполняется картинка, сайт и даты, т.к. для них не было вынесего отдельных методов в model,
    # а сами изменения делаются напрямую в методе fill_contact_form
    app2.contact.create(Contact())

