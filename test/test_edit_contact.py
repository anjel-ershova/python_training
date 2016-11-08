# -*- coding: utf-8 -*-
from model.model_contact import *

def test_edit_contact_general(app2):
    if app2.contact.count() == 0:
        app2.contact.create(General(firstname="firstname-created", middlename="middlename-created", lastname="lastname-created", nickname="nickname-created", title="title-created",
                 company="company-created", address="address-created"), Telephone(),Email(), Secondary())
    app2.contact.edit_first_contact(field="firstname", text1="new firstname")
    app2.contact.edit_first_contact(field="middlename", text1="new middlename")
    app2.contact.edit_first_contact(field="lastname", text1="new lastname")
    app2.contact.edit_first_contact(field="nickname", text1="new nickname")
    app2.contact.edit_first_contact(field="title", text1="new title")
    app2.contact.edit_first_contact(field="company", text1="new company")
    app2.contact.edit_first_contact(field="address", text1="new address")

#def test_edit_contact_picture(app2):
#    app2.contact.edit_first_contact(field="photo", text="C:\\fun\\learn\\Python\\SoftwareTesting\\занятие3\\new_picture_for_contact.png")

def test_edit_contact_telephone(app2):
    if app2.contact.count() == 0:
        app2.contact.create(General(), Telephone(home='home-created', mobile='mobile-created', work='work-created', fax='fax-created'),Email(), Secondary())
    app2.contact.edit_first_contact(field="home", text1="new home number")
    app2.contact.edit_first_contact(field="mobile", text1="new mobile number")
    app2.contact.edit_first_contact(field="work", text1="new work number")
    app2.contact.edit_first_contact(field="fax", text1="new fax number")

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
    app2.contact.edit_first_contact(field="address2", text1="new address2")
    app2.contact.edit_first_contact(field="phone2", text1="new phone2")
    app2.contact.edit_first_contact(field="notes", text1="new notes")
