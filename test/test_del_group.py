from random import randrange
from model.model_group import Group

def test_delete_some_group(app2):
    if app2.group.count() == 0:
        app2.group.create(Group(name="Created name", footer="Created footer", header="Created header"))
    old_groups = app2.group.get_group_list()
    index = randrange(len(old_groups))
    app2.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app2.group.count()
    new_groups = app2.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups