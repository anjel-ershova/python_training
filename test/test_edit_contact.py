# -*- coding: utf-8 -*-
#from model.contacts import Email
from model.model_contact import General
#from model.contacts import Secondary
#from model.model_contact import Telephone

#def test_edit_first_contact_general(app2):
#    app2.session.login(login='admin', password='secret')
#    app2.contact.edit_first_contact(General(firstname="new firstname", middlename="new middlename", lastname="new lastname", nickname="new nickname", title="new title", company="new company", address="new address"))
#    app2.session.logout()

#def test_edit_first_contact_telephone(app2):
#    app2.session.login(login='admin', password='secret')
#    app2.contact.edit_first_contact(Telephone(home="new homephone"))
#    app2.session.logout()

#def test_edit_site(app2):
#    app2.session.login(login='admin', password='secret')
#    app2.navigation.open_contact_creation_page()
#    app2.contact.open_to_edit()
#    app2.contact.fill_contact_form("homepage", "https://ya.ru")
#    app2.contact.click_to_submit()
#    app2.session.logout()

def test_edit_site(app2):
    app2.session.login(login='admin', password='secret')
    app2.contact.edit_first_contact(General(firstname="new firstname", middlename="new middlename", lastname="new lastname", nickname="new nickname", title="new title", company="new company", address="new address"))
    app2.session.logout()