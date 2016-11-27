from model.model_contact import *

def test_delete_first_contact(app2):
    if app2.contact.count() == 0:
        app2.contact.create(Contact(firstname2="firstname-created", middlename="middlename-created", lastname="lastname-created", nickname="nickname-created", title="title-created",
                company="company-created", address="address-created", home='home-created', mobile='mobile-created', work='work-created', fax='fax-created',
                email='email-created@mfsa.ru', email2='email2-created@mfsa.ru', email3='email3-created@mfsa.ru', address2='Another address-created', home2='home_secondary-created', notes='Some text-created'))
    old_contacts = app2.contact.get_contact_list()
    app2.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app2.contact.count()
    new_contacts = app2.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

