from model.model_contact import Contact
from model.model_group import Group
import random
from fixture.orm import *


def test_delete_contact_to_group(app2, db, orm):
    #проверка на пустой список групп
    if len(orm.get_group_list()) == 0:
        app2.group.create(Group(name="Created name_ORM_D", footer="Created footer_ORM_D", header="Created header_ORM_D"))
    # выбираем любую группу, переходим к ней
    active_groups = orm.get_group_list()
    target_group = random.choice(active_groups)
    app2.group.select_some_group_to_view(target_group)
    # смотрим, сколько контактов в группе
    old_contacts = orm.get_contacts_in_group(target_group)
    # проверка на пустой список контактов
    if len(old_contacts) != 0:
        contact = random.choice(old_contacts)
        app2.contact.select_contact_by_id(contact.id)
        # удаляем выбранный контакт
        app2.contact.delete_selected_contact_in_group_page()
    else:
        app2.contact.create(
            Contact(firstname2="firstname-created_ORM_D", middlename="middlename-created_ORM_D", lastname="lastname-created",
                    nickname="nickname-created", title="title-created",
                    company="company-created", address="address-created", home='home-created', mobile='mobile-created',
                    work='work-created', fax='fax-created',
                    email='email-created@mfsa.ru', email2='email2-created@mfsa.ru', email3='email3-created@mfsa.ru',
                    address2='Another address-created', phone2='home_secondary-created', notes='Some text-created'))
        app2.contact.select_contact_by_index(0)
        # удаляем выбранный контакт
        app2.group.add_selected_contact_to_selected_group_by_id(target_group)
    app2.navigation.go_to_target_group_by_id(target_group.id)
    # собираем новый список контактов этой группы
    new_contacts = orm.get_contacts_in_group(target_group)
    old_contacts.remove(contact)
    # проверка, что список после удаления контакта совпадает с списком ??? каким
    assert sorted(new_contacts, key=Group.id_or_max) == sorted(old_contacts, key=Group.id_or_max)