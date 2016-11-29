from random import randrange
from model.model_contact import *

def test_delete_first_contact(app2):
    if app2.contact.count() == 0:
        app2.contact.create(Contact(firstname2="firstname-created", middlename="middlename-created", lastname="lastname-created", nickname="nickname-created", title="title-created",
                                    company="company-created", address="address-created", homephone='home-created', mobilephone='mobilephone-created', workphone='workphone-created', fax='fax-created',
                                    email='email-created@mfsa.ru', email2='email2-created@mfsa.ru', email3='email3-created@mfsa.ru', address2='Another address-created', secondaryphone2='home_secondary-created', notes='Some text-created'))
    old_contacts = app2.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app2.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app2.contact.count()
    new_contacts = app2.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

