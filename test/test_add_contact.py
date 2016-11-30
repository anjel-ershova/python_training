# -*- coding: utf-8 -*-
from model.model_contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    cont_symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10

    return prefix + "".join([random.choice(cont_symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname2="", middlename="", lastname="", nickname="", title="",
                           company="", address="", home="", mobile="", work="", fax="", email="", email2="", email3="",
                           address2="", phone2="", notes="")] + [Contact
                            (firstname2=random_string("firstname", 10),
                             middlename=random_string("middlename", 20),
                             lastname=random_string("lastname", 20),
                             nickname=random_string("nickname", 20),
                             title=random_string("title", 20),
                             company=random_string("company", 20),
                             address=random_string("address", 30),
                             home=random_string("homephone", 20), mobile=random_string("mobilephone", 20), work=random_string("workphone", 20),
                             fax=random_string("fax", 20),
                             email=random_string("email1", 20), email2=random_string("email2", 20), email3=random_string("email3", 20),
                             address2=random_string("Another_address", 20),
                             phone2=random_string("home_secondary", 20),
                             notes=random_string("notes", 50))
for i in range(1)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app2, contact):
    # собираем старый список контактов
    old_contacts = app2.contact.get_contact_list()
    # выполняем создание контакта в соответствии с локальными переменными
    app2.contact.create(contact)
    # сравниваем старый и новый списки по длине, новый == старый +1, длину старого списка берем методом count
    assert len(old_contacts) + 1 == app2.contact.count()
    # собираем новый список контактов (после создания нового)
    new_contacts = app2.contact.get_contact_list()
    #добавляем в старый список данные от нового созданного контакта (из локальных переменных)
    old_contacts.append(contact)
    # сравниваем 2 полученных списка: новый и старый с добавленным контактом
    # для того, чтобы их можно было сравнивать в model_contacts надо добавить 2 метода: __eq__ и id_or_max
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

