from model.model_group import Group

def test_delete_first_group(app2):
    if app2.group.count() == 0:
        app2.group.create(Group(name="Created name", footer="Created footer", header="Created header"))
    old_groups = app2.group.get_group_list()
    app2.group.delete_first_group()
    new_groups = app2.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups