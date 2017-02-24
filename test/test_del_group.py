from model.model_group import Group
import random

def test_delete_some_group(app2, db, check_ui):
    if len(db.get_group_list()) == 0:
        app2.group.create(Group(name="Created name", footer="Created footer", header="Created header"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app2.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == app2.group.count()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app2.group.get_group_list(), key=Group.id_or_max)
#        assert new_groups == app2.group.get_group_list() #раскомментировать, чтобы проверить работоспособность check_ui: если тест упал - работает