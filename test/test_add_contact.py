# -*- coding: utf-8 -*-
from model.model_contact import Email
from model.model_contact import General
from model.model_contact import Secondary
from model.model_contact import Telephone

def test_add_contact(app2):
    app2.session.login(login='admin', password='secret')
    app2.contact.create(General(firstname="firstname", middlename="middlename", lastname="lastname", nickname="nickname", title="title",
                 company="company", address="address"), Telephone(home='555-5678', mobile='8-800-200-555-500', work='555-work', fax='812-123-23-34'), Email(email='email@mfsa.ru', email2='email2@mfsa.ru', email3='email3@mfsa.ru'), Secondary(address2='Another address', home='home_secondary', notes='Some text'))
    app2.session.logout()