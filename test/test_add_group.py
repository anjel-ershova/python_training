# -*- coding: utf-8 -*-
from model.model_group import *
import pytest
from data.data_add_group import constant as testdata

# 1 - название параметра, куда передаются тест. данные,
# 2 - откуда тест. данные брать,
# 3 - список с текстовым предлставлением тест. данных
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app2, group):
    old_groups = app2.group.get_group_list()
    app2.group.create(group)
    assert len(old_groups) + 1 == app2.group.count()
    new_groups = app2.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

