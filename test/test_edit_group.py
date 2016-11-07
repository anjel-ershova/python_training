# -*- coding: utf-8 -*-
from model.model_group import Group


def test_edit_group_name(app2):
    app2.group.edit_first_group(Group(name="new group_name"))

def test_edit_group_header(app2):
    app2.group.edit_first_group(Group(header="new group_header1"))

def test_edit_group_footer(app2):
    app2.group.edit_first_group(Group(footer="new group_footer1"))