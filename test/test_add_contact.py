# -*- coding: utf-8 -*-
import pytest

from fixture.application import *
from model.contacts import Email
from model.contacts import General
from model.contacts import Secondary
from model.contacts import Telephone


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(login='admin', password='secret')
    app.create_contact(General(), Telephone(), Email(email='email@mfsa.ru', email2='email2@mfsa.ru', email3='email3@mfsa.ru'), Secondary())
    app.logout()