# -*- coding: utf-8 -*-
import pytest
from contacts import General
from contacts import Telephone
from contacts import Email
from contacts import Secondary
#from contacts import Date
from application import *

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(login='admin', password='secret')
    app.create_contact(General(), Telephone(), Email(email='email@mfsa.ru', email2='email2@mfsa.ru', email3='email3@mfsa.ru'), Secondary())
    app.logout()