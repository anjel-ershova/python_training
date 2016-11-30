# -*- coding: utf-8 -*-
from model.model_group import *

def test_add_group(app2, data_groups):
    group = data_groups
    old_groups = app2.group.get_group_list()
    app2.group.create(group)
    assert len(old_groups) + 1 == app2.group.count()
    new_groups = app2.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

