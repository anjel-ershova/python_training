# -*- coding: utf-8 -*-
from model.model_group import Group
import random

def test_edit_group_name(app2, db, check_ui):
    # если число групп == 0, то делаем новую, чтобы ее можно было модифицировать
    if len(db.get_group_list()) == 0:
        app2.group.create(Group(name="Created name"))
    # собираем старый список групп из бд
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group_data = Group(id=group.id, name="WOW03", footer=None, header=None)
    app2.group.edit_group_by_id(group.id, new_group_data)
    new_groups = db.get_group_list()
    assert len(old_groups) == app2.group.count()
    new_groups.remove(new_group_data)
    old_groups.remove(group)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
    if check_ui:
        newest_groups = db.get_group_list()
        assert sorted(newest_groups, key=Group.id_or_max) == sorted(app2.group.get_group_list(), key=Group.id_or_max)

"""
def test_edit_group_header(app2):
    if app2.group.count() == 0:
        app2.group.create(Group(header="Created header"))
    old_groups = app2.group.get_group_list()
    app2.group.edit_first_group(Group(header="new group_header1"))
    new_groups = app2.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_edit_group_footer(app2):
    if app2.group.count() == 0:
        app2.group.create(Group(footer="Created footer" ))
    old_groups = app2.group.get_group_list()
    app2.group.edit_first_group(Group(footer="new group_footer1"))
    new_groups = app2.group.get_group_list()
    assert len(old_groups) == len(new_groups)
"""