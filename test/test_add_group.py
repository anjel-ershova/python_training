# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app2):
    app2.session.login(login="admin", password="secret")
    app2.group.create(Group(name="group_name1", footer="group_footer1", header="group_header1"))
    app2.session.logout()

def test_add_empty_group(app2):
    app2.session.login(login="admin", password="secret")
    app2.group.create(Group(name="", header="", footer=""))
    app2.session.logout()

