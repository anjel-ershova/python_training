from timeit import timeit
from model.model_group import Group

def test_group_list(app2, db):
    print(timeit(lambda: app2.group.get_group_list(), number=1))
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
    assert False #sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)