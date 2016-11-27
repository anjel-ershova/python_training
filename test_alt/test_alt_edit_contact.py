# -*- coding: utf-8 -*-
from model.alt_model_contact import *

def test_edit_contact_general(app2):
    if app2.contact.count() == 0:
        app2.contact.create(General(firstname="firstname-created", middlename="middlename-created", lastname="lastname-created", nickname="nickname-created", title="title-created",
                 company="company-created", address="address-created"), Telephone(),Email(), Secondary())
    old_contact_list = app2.contact.get_contact_list()
    # забираем в локальную переменную значение, которое будет присвоено firstname после модификации
    fill_general = General(firstname="new firstname", lastname="new lastname", middlename="new middlename", nickname="new nickname", title="new title", company="new company", address="new address")
    # запоминаем id элемента, который будет видоизменен
    fill_general.id = old_contact_list[0].id
    # меняем значение поля general (и только его, другие поля должны использовать свои методы)
    app2.contact.edit_first_contact_general(fill_general)
    # собираем новый список контактов
    new_contact_list = app2.contact.get_contact_list()
    # сравниваем длины списков, должны совпадать (ничего же не удаляли)
    assert len(old_contact_list) == len(new_contact_list)
    # присваиваем первому элементу старого списка то имя, на которое его меняли
    old_contact_list[0] = fill_general
    # сравниваем 2 списка старый с запомненным id и именем, замененным на новое и новый
    assert sorted(old_contact_list, key=General.id_or_max) == sorted(new_contact_list, key=General.id_or_max)




"""
# в последующих лекциях будет показан более оптимальный способ написания тестов


#def test_edit_contact_picture(app2):
#    app2.contact.edit_first_contact(field="photo", text="C:\\fun\\learn\\Python\\SoftwareTesting\\занятие3\\new_picture_for_contact.png")

# тут начало сделано по аналогии с General, но надо менять get_contact_list в фикстуре, иначе завалится
def test_edit_contact_telephone(app2):
    if app2.contact.count() == 0:
        app2.contact.create(General(), Telephone(home='home-created', mobile='mobile-created', work='work-created', fax='fax-created'),Email(), Secondary())
    old_contact_list = app2.contact.get_contact_list()
    fill_telephone = Telephone(home='new home number', mobile='new mobile number', work='new work number', fax='new fax number')
    app2.contact.edit_first_contact_telephone(fill_telephone)
    new_contact_list = app2.contact.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list)
    old_contact_list[0] = fill_telephone
    assert sorted(old_contact_list, key=General.id_or_max) == sorted(new_contact_list, key=General.id_or_max)

def test_edit_contact_email(app2):
    if app2.contact.count() == 0:
        app2.contact.create(General(), Telephone(), Email(email='email-created@mfsa.ru', email2='email2-created@mfsa.ru', email3='email3-created@mfsa.ru'), Secondary())
    app2.contact.edit_first_contact(field="email", text1="new email")
    app2.contact.edit_first_contact(field="email2", text1="new email2")
    app2.contact.edit_first_contact(field="email3", text1="new email3")

def test_edit_contact_site(app2):
    if app2.contact.count() == 0:
        app2.contact.create(General(), Telephone(), Email(), Secondary())
    app2.contact.edit_first_contact(field="homepage", text1="https://ya.ru")

def test_edit_contact_dates(app2):
    if app2.contact.count() == 0:
        app2.contact.create(General(), Telephone(), Email(), Secondary())
    app2.navigation.open_contact_creation_page()
    app2.contact.open_to_edit()
    #подстановка дат (кроме месяца) работает на рандоме, так что, пока считаем, что дата правда меняется
    app2.contact.fill_calendar(day='bday', month='bmonth', year='byear')
    app2.contact.fill_calendar(day='aday', month='amonth', year='ayear')
    app2.contact.click_to_submit()

def test_edit_contact_secondary(app2):
    if app2.contact.count() == 0:
        app2.contact.create(General(), Telephone(), Email(), Secondary(address2='Another address-created', home='home_secondary-created', notes='Some text-created'))
    secondary = Secondary(address2='Another address-created', home='home_secondary-created', notes='Some text-created')
    app2.contact.edit_first_contact(field="phone2", text1="new phone2")
"""

