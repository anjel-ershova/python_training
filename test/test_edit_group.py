# -*- coding: utf-8 -*-
from model.model_group import Group
import random

def test_edit_group_name(app2, db, check_ui):
    # если число групп == 0, то делаем новую, чтобы ее можно было модифицировать
    if len(db.get_group_list()) == 0:
        app2.group.create(Group(name="Created name"))
    # собираем старый список групп
    old_groups = app2.group.get_group_list()
    group = random.choice(old_groups)
#    # было: запоминаем id элемента, который будет видоизменен
#    group.id = old_groups[index].id
    new_group_data = Group(name="Newest group")
    app2.group.edit_group_by_id(group.id, new_group_data)
    new_groups = db.get_group_list()
#    # было: присваиваем первому элементу старого списка то имя, на которое его меняли
#    old_groups[index] = group
    assert len(old_groups) == len(new_groups)
#   подумать, как правильно запоминать id группы, выбранной по id
#   assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app2.group.get_group_list(), key=Group.id_or_max)

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