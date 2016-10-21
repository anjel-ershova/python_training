def test_add_contact(app2):
    app2.session.login(login='admin', password='secret')
    app2.contact.delete_first_contact()
    app2.session.logout()
