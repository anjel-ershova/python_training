import re


def test_phones_on_homepage(app2):
    # поверки для конкретного контакта, в [] - индекс == номер контакта
    contact_from_home_page = app2.contact.get_contact_list()[0]
    contact_from_edit_page = app2.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.home == clear(contact_from_edit_page.home)
    assert contact_from_home_page.work == clear(contact_from_edit_page.work)
    assert contact_from_home_page.mobile == clear(contact_from_edit_page.mobile)
    assert contact_from_home_page.phone2 == clear(contact_from_edit_page.phone2)

def test_phones_on_contact_view_page(app2):
    # поверки для конкретного контакта, в () - индекс == номер контакта
    contact_from_view_page = app2.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app2.contact.get_contact_info_from_edit_page(0)
    assert contact_from_edit_page.home == contact_from_view_page.home
    assert contact_from_edit_page.work == contact_from_view_page.work
    assert contact_from_edit_page.mobile == contact_from_view_page.mobile
    assert contact_from_edit_page.phone2 == contact_from_view_page.phone2

def clear(s):
    # регулярное выражение re.sub в качестве параметров имеет: ("что вырезать", "на что заменять", где это делать)
    return re.sub("[() -]", "", s)

#def test_all_data_homepage_vs_editpage(app2):
