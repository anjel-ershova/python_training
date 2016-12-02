import random
from model.model_contact import *

def test_delete_first_contact(app2, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app2.contact.create(Contact(firstname2="firstname-created", middlename="middlename-created", lastname="lastname-created", nickname="nickname-created", title="title-created",
                                    company="company-created", address="address-created", home='home-created', mobile='mobile-created', work='work-created', fax='fax-created',
                                    email='email-created@mfsa.ru', email2='email2-created@mfsa.ru', email3='email3-created@mfsa.ru', address2='Another address-created', phone2='home_secondary-created', notes='Some text-created'))
    # старый список берем из базы
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app2.contact.delete_contact_by_id(contact.id)
    new_contacts = app2.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app2.group.get_contact_list(), key=Contact.id_or_max)

