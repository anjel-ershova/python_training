# -*- coding: utf-8 -*-
from model.model_group import Group


def test_add_group(app2):
    app2.group.create(Group(name="group_name1", footer="group_footer1", header="group_header1"))
    # пока оставлю с логаутом, потом удалю
    app2.session.logout()

def test_add_empty_group(app2):
    app2.group.create(Group(name="", footer="", header=""))

