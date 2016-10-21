# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_group(app2):
    app2.session.login(login="admin", password="secret")
    app2.group.edit_first_group(Group(name="new group_name", header="new group_header1", footer="new group_footer1"))
    app2.session.logout()
