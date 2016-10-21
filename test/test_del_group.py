def test_delete_first_group(app2):
    app2.session.login(login="admin", password="secret")
    app2.group.delete_first_group()
    app2.session.logout()