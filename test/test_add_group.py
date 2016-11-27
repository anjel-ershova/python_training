# -*- coding: utf-8 -*-
from model.model_group import *

def test_add_group(app2):
    old_groups = app2.group.get_group_list()
    group = Group(name="group_name1", footer="group_footer1", header="group_header1", id=None)
    app2.group.create(group)
    new_groups = app2.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_add_empty_group(app2):
    old_groups = app2.group.get_group_list()
    group2 = Group(name="", footer="", header="")
    app2.group.create(group2)
    new_groups = app2.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group2)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


