import re


def test_phones_on_homepage(app2):
    # поверки для конкретного контакта, в [] - индекс == номер контакта
    contact_from_home_page = app2.contact.get_contact_list()[0]
    contact_from_edit_page = app2.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.homephone == clear(contact_from_edit_page.homephone)
    assert contact_from_home_page.workphone == clear(contact_from_edit_page.workphone)
    assert contact_from_home_page.mobilephone == clear(contact_from_edit_page.mobilephone)
    assert contact_from_home_page.secondaryphone == clear(contact_from_edit_page.secondaryphone)

def test_phones_on_contact_view_page(app2):
    # поверки для конкретного контакта, в () - индекс == номер контакта
    contact_from_view_page = app2.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app2.contact.get_contact_info_from_edit_page(0)
    assert contact_from_edit_page.homephone == contact_from_view_page.homephone
    assert contact_from_edit_page.workphone == contact_from_view_page.workphone
    assert contact_from_edit_page.mobilephone == contact_from_view_page.mobilephone
    assert contact_from_edit_page.secondaryphone == contact_from_view_page.secondaryphone

def clear(s):
    # регулярное выражение re.sub в качестве параметров имеет: ("что вырезать", "на что заменять", где это делать)
    return re.sub("[() -]", "", s)