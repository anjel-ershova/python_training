# -*- coding: utf-8 -*-
from model.alt112121212_model_contact import *


def test_edit_contact_general(app2):
    if app2.contact.count() == 0:
        app2.contact.create(Contact(firstname2=None, middlename=None, lastname=None, nickname=None, title=None,
                 company=None, address="111111", id=None, home=None, mobile=None, work=None, fax=None, email=None, email2=None, email3=None,
                 address2=None, home2=None, notes=None))
    old_contact_list = app2.contact.get_contact_list()
        # забираем в локальную переменную значение, которое будет присвоено firstname после модификации
    contact = Contact(firstname2="new firstname1111", lastname="new lastname1111")
        # запоминаем id элемента, который будет видоизменен
    contact.id = old_contact_list[0].id
        # меняем значение поля
    app2.contact.edit_first_contact(contact)
        # собираем новый список контактов
    new_contact_list = app2.contact.get_contact_list()
        # сравниваем длины списков, должны совпадать (ничего же не удаляли)
    assert len(old_contact_list) == len(new_contact_list)
        # присваиваем первому элементу старого списка то имя, на которое его меняли
    old_contact_list[0] = contact
        # сравниваем 2 списка старый с запомненным id и именем, замененным на новое и новый
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)

"""
def test_add_empty_contact(app2):
    # все же заполняется картинка, сайт и даты, т.к. для них не было вынесего отдельных методов в model,
    # а сами изменения делаются напрямую в методе fill_contact_form
    app2.contact.create(Contact())
"""