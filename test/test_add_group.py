# -*- coding: utf-8 -*-
from model.model_group import Group


def test_add_group(app2):
    app2.session.login(login="admin", password="secret")
    app2.group.create(Group())
    app2.session.logout()


#def test_add_empty_group(app2):
#    app2.session.login(login="admin", password="secret")
#    app2.group.create(Group(name="", footer="", header=""))
#    app2.session.logout()

