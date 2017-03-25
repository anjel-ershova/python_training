from model.model_contact import Contact
from model.model_group import Group
import random
from fixture.orm import *


def test_delete_contact_to_group(app2, db):
    #проверка на пустой список групп
    if len(db.get_group_list()) == 0:
        app2.group.create(Group(name="Created name", footer="Created footer", header="Created header"))

    # открываем страницу home
    app2.navigation.open_home_page()
    # выбираем любую группу, переходим к ней
    active_groups = db.get_group_list()
    target_group = random.choice(active_groups)
    app2.group.select_some_group_to_view(target_group)
    old_contacts = app2.contact.get_contact_list()
    # проверка на пустой список контактов
    if len(old_contacts) == 0:
        app2.contact.create(
            Contact(firstname2="firstname-created", middlename="middlename-created", lastname="lastname-created",
                    nickname="nickname-created", title="title-created",
                    company="company-created", address="address-created", home='home-created', mobile='mobile-created',
                    work='work-created', fax='fax-created',
                    email='email-created@mfsa.ru', email2='email2-created@mfsa.ru', email3='email3-created@mfsa.ru',
                    address2='Another address-created', phone2='home_secondary-created', notes='Some text-created'))
        app2.contact.select_contact_by_index(0)
        app2.group.select_some_group_to_add(target_group)
    # перейти к странице конкретной группы
    app2.navigation.go_to_target_group_by_id(target_group.id)
    # выбираем любой контакт из конкретной группы
    contact = random.choice(old_contacts)
    app2.contact.select_contact_by_id(contact.id)
    # если нет контакта, добавляем его

    # удаляем контакт
    app2.contact.delete_contact_by_id(contact.id)
    # проверка, что список после удаления контакта совпадает с списком ??? каким
    pass