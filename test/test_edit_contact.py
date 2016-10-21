# -*- coding: utf-8 -*-
#from model.contacts import Email
from model.contacts import General
#from model.contacts import Secondary
#from model.contacts import Telephone

def test_edit_first_contact(app2):
    app2.session.login(login='admin', password='secret')
    app2.contact.edit_first_contact(General(firstname="new firstname"))
    app2.session.logout()