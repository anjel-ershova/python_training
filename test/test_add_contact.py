# -*- coding: utf-8 -*-
from model.contacts import Email
from model.contacts import General
from model.contacts import Secondary
from model.contacts import Telephone

def test_add_contact(app2):
    app2.session.login(login='admin', password='secret')
    app2.contact.create(General(), Telephone(), Email(email='email@mfsa.ru', email2='email2@mfsa.ru', email3='email3@mfsa.ru'), Secondary())
    app2.session.logout()