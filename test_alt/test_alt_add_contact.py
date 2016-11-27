# -*- coding: utf-8 -*-
from model.alt_model_contact import Email
from model.alt_model_contact import General
from model.alt_model_contact import Secondary
from model.alt_model_contact import Telephone

def test_add_contact(app2):
    # собираем старый список контактов
    old_contacts = app2.contact.get_contact_list()
    # выносим general в локальную переменную
    contact_general = General(firstname="qqqfirstname", middlename="middlename", lastname="lastname", nickname="nickname", title="title",
                 company="company", address="address")
    # выносим список телефонов в локальную переменную
    contact_telephone = Telephone(home='555-5678', mobile='8-800-200-555-500', work='555-work', fax='812-123-23-34')
    # выносим эл. адреса в локальную переменную
    contact_email = Email(email='email@mfsa.ru', email2='email2@mfsa.ru', email3='email3@mfsa.ru')
    # выносим secondary в локальную переменную
    contact_secondary = Secondary(address2='Another address', home='home_secondary', notes='Some text')
    # выполняем создание контакта в соответствии с локальными переменными
    app2.contact.create(contact_general, contact_telephone, contact_email, contact_secondary)
    # собираем новый список контактов (после создания нового)
    new_contacts = app2.contact.get_contact_list()
    # сравниваем старый и новый списки по длине, новый == старый +1
    assert len(old_contacts) + 1 == len(new_contacts)
    #добавляем в старый список данные от нового созданного контакта (из локальных переменных)
    old_contacts.append(contact_general)
    # сравниваем 2 полученных списка: новый и старый с добавленным контактом
    # для того, чтобы их можно было сравнивать в model_contacts надо добавить 2 метода: __eq__ и id_or_max
    assert sorted(old_contacts, key=General.id_or_max) == sorted(new_contacts, key=General.id_or_max)


#Просто тест создания пустого контакта, без излишеств
def test_add_empty_contact(app2):
    # все же заполняется картинка, сайт и даты, т.к. для них не было вынесего отдельных методов в model,
    # а сами изменения делаются напрямую в методе fill_contact_form
    app2.contact.create(General(), Telephone(), Email(), Secondary())
