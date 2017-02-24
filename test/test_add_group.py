# -*- coding: utf-8 -*-
from model.model_group import *

def test_add_group(app2, db, data_groups, check_ui):
    group = data_groups
    old_groups = db.get_group_list()
    app2.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app2.group.get_group_list(), key=Group.id_or_max)
#        assert new_groups == app2.group.get_group_list() #раскомментировать, чтобы проверить работоспособность check_ui: если тест упал - работает
