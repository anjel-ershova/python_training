import re
from random import randrange


def test_phones_on_homepage(app2):
    for_index = app2.contact.get_contact_list()
    index = randrange(len(for_index))  # cлучайно генерит число
    contact_from_home_page = app2.contact.get_contact_list()[index]
    contact_from_edit_page = app2.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_homepage == merge_emails_like_on_homepage(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)

"""
#доделать при случае
def test_phones_on_contact_view_page(app2):
    for_index = app2.contact.get_contact_list()
    index = randrange(len(for_index))  # cлучайно генерит число
    contact_from_view_page = app2.contact.get_contact_info_from_view_page(index)
    contact_from_edit_page = app2.contact.get_contact_info_from_edit_page(index)
    assert contact_from_edit_page.home == contact_from_view_page.home
    assert contact_from_edit_page.work == contact_from_view_page.work
    assert contact_from_edit_page.mobile == contact_from_view_page.mobile
    assert contact_from_edit_page.phone2 == contact_from_view_page.phone2
"""

def clear(s):
    # регулярное выражение re.sub в качестве параметров имеет: ("что вырезать", "на что заменять", где это делать)
    return re.sub("[() -]", "", s)

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                    [contact.home, contact.mobile, contact.work, contact.phone2]))))

def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            (filter(lambda x: x is not None,
                                [contact.email, contact.email2, contact.email3]))))
