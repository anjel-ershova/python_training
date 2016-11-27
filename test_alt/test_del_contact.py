from model.alt_model_contact import *

def test_add_contact(app2):
    if app2.contact.count() == 0:
        app2.contact.create(General(firstname="firstname-created", middlename="middlename-created", lastname="lastname-created", nickname="nickname-created", title="title-created",
                 company="company-created", address="address-created"), Telephone(home='home-created', mobile='mobile-created', work='work-created', fax='fax-created'),
                 Email(email='email-created@mfsa.ru', email2='email2-created@mfsa.ru', email3='email3-created@mfsa.ru'), Secondary(address2='Another address-created', home='home_secondary-created', notes='Some text-created'))
    old_contacts = app2.contact.get_contact_list()
    app2.contact.delete_first_contact()
    new_contacts = app2.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

