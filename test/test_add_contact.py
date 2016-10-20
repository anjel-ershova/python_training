# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contacts import Email
from model.contacts import General
from model.contacts import Secondary
from model.contacts import Telephone


@pytest.fixture
def app1(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app1):
    app1.session.login(login='admin', password='secret')
    app1.contact.create(General(), Telephone(), Email(email='email@mfsa.ru', email2='email2@mfsa.ru', email3='email3@mfsa.ru'), Secondary())
    app1.session.logout()