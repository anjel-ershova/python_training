from model.model_group import Group

def test_delete_first_group(app2):
    if app2.group.count() == 0:
        app2.group.create(Group(name="Created name", footer="Created footer", header="Created header"))
    app2.group.delete_first_group()