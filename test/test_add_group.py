# -*- coding: utf-8 -*-
import unittest

import pytest

from fixture.application import *
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(login="admin", password="secret")
    app.create_group(Group(name="group_name1", header="group_header1", footer="group_footer1"))
    app.logout()


def test_add_empty_group(app):
    app.login(login="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

if __name__ == '__main__':
    unittest.main()
