from model.model_contact import Contact
from model.model_group import Group
import random
from fixture.orm import *


def test_add_contact_to_group(app2, db, orm):
    #проверка на пустой список контактов
    if len(db.get_contact_list()) == 0:
        app2.contact.create(Contact(firstname2="firstname-created_orm", middlename="middlename-created_orm", lastname="lastname-created_orm", nickname="nickname-created", title="title-created",
                                    company="company-created", address="address-created", home='home-created', mobile='mobile-created', work='work-created', fax='fax-created',
                                    email='email-created@mfsa.ru', email2='email2-created@mfsa.ru', email3='email3-created@mfsa.ru', address2='Another address-created', phone2='home_secondary-created', notes='Some text-created'))
    #проверка на пустой список групп
    if len(db.get_group_list()) == 0:
        app2.group.create(Group(name="Created name_orm", footer="Created footer_orm", header="Created header_orm"))
    # открываем страницу home
    app2.navigation.open_home_page()
    # выбираем любой контакт
    all_contacts = app2.contact.get_contact_list()
    contact = random.choice(all_contacts)
    app2.contact.select_contact_by_id(contact.id)
    # выбор произвольной группы из дропдауна
    all_groups = db.get_group_list()
    target_group = random.choice(all_groups)
    # собрать старый список контактов в группах из orm
    old_cont_in_gr_orm = orm.get_contacts_in_group(target_group)
    # добавляем выбранный контакт в выбранную группу
    app2.group.select_some_group_to_add(target_group)
    # собрать новый список контактов в группах из orm
    new_cont_in_gr_orm = orm.get_contacts_in_group(target_group)
    old_cont_in_gr_orm.append(contact)
    assert sorted(old_cont_in_gr_orm, key=Group.id_or_max) == sorted(new_cont_in_gr_orm, key=Group.id_or_max)

    """
     if check_ui:
         assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app2.contact.get_contact_list(), key=Contact.id_or_max)
 #        assert new_contacts == app2.contact.get_contact_list() #раскомментировать, чтобы проверить работоспособность check_ui: если тест упал - работает
 """