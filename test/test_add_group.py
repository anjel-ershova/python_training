# -*- coding: utf-8 -*-
from model.model_group import *
import pytest

testdata = [Group(name="group_name1", footer="group_footer1", header="group_header1", id=None),
        Group(name="", footer="", header="")
]


# 1 - название параметра, куда передаются тест. данные,
# 2 - откуда тест. данные брать,
# 3 - список с текстовым предлставлением тест. данных
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app2, group):
    pass
    #old_groups = app2.group.get_group_list()
    #app2.group.create(group)
    #assert len(old_groups) + 1 == app2.group.count()
    #new_groups = app2.group.get_group_list()
    #old_groups.append(group)
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

