# -*- coding: utf-8 -*-
from model.model_group import *

def test_add_group(app2, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    app2.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

