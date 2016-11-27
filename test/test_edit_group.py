# -*- coding: utf-8 -*-
from random import randrange
from model.model_group import Group


def test_edit_group_name(app2):
    # если число групп == 0, то делаем новую, чтобы ее можно было модифицировать
    if app2.group.count() == 0:
        app2.group.create(Group(name="Created name"))
    # собираем старый список групп
    old_groups = app2.group.get_group_list()
    # забираем в локальную переменную значение, которое будет присвоено имени группы после модификации
    group = Group(name="new group_name")
    index = randrange(len(old_groups)) # cлучайно генерит число
    # запоминаем id элемента, который будет видоизменен
    group.id = old_groups[index].id
    # меняем название случайной группы списка на то, которое было запомнено
    app2.group.edit_group_by_index(index, group)
    # сравниваем длины списков, должны совпадать (ничего же не удаляли)
    # новый список сразу грузить не будем, дешевле измерить длину нового списка методом count
    assert len(old_groups) == app2.group.count()
    # собираем новый список из групп
    new_groups = app2.group.get_group_list()
    # присваиваем первому элементу старого списка то имя, на которое его меняли
    old_groups[index] = group
    # сравниваем 2 списка старый с запомненным id и именем, замененным на новое и новый
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

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