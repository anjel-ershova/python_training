from selenium.webdriver.support.ui import Select
from random import randint
from random import choice
from model.model_contact import *


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.navigation.open_contact_creation_page()
        self.fill_contact_form(contact)
        # save_contact
        wd.find_element_by_name("submit").click()
        # return_to_home_page
        self.app.navigation.open_home_page()

    def fill_calendar(self, day, month, year):
        # для дат (число, год) используем randint, как сделать случайный месяц - пока не ясно
        wd = self.app.wd
        wd.find_element_by_name(day).send_keys(randint(1, 30))
        select = Select(wd.find_element_by_name(month))
        select.select_by_visible_text('January')
        wd.find_element_by_name(year).send_keys(randint(1920, 2017))

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # заполнение первого блока - General, используется метод fill_contact_form, переменные имеют заданное дефолтное значение
        self.edit_if_not_none("firstname", contact.firstname)
        self.edit_if_not_none("middlename", contact.middlename)
        self.edit_if_not_none("lastname", contact.lastname)
        self.edit_if_not_none("nickname", contact.nickname)
        wd.find_element_by_name("photo").send_keys("C:\\fun\\learn\\Python\\SoftwareTesting\\занятие1\\окружение.png")
        self.edit_if_not_none("title", contact.title)
        self.edit_if_not_none("company", contact.company)
        self.edit_if_not_none("address", contact.address)
        # заполнение телефона, используется метод fill_contact_form, переменные имеют заданное дефолтное значение
        self.edit_if_not_none("home", contact.home)
        self.edit_if_not_none("mobile", contact.mobile)
        self.edit_if_not_none("work", contact.work)
        self.edit_if_not_none("fax", contact.fax)
        # заполнение email, используется метод fill_contact_form, для иллюстрации значение переменной указано в тесте в явном виде
        # отдельно в классе дефолтное значение не задано
        self.edit_if_not_none("email", contact.email)
        self.edit_if_not_none("email2", contact.email2)
        self.edit_if_not_none("email3", contact.email3)
        # заполнение сайта, используется метод fill_contact_form
        self.edit_if_not_none("homepage", "https://google.ru")
        # заполняем дату рождения и годовщину, используем отдельный метод fill_calendar
        self.fill_calendar(day='bday', month='bmonth', year='byear')
        self.fill_calendar(day='aday', month='amonth', year='ayear')
        # заполнение Secondary, переменные имеют заданное дефолтное значение
        self.edit_if_not_none("address2", contact.address2)
        self.edit_if_not_none("phone2", contact.home)
        self.edit_if_not_none("notes", contact.notes)


    def edit_if_not_none(self, field, text1):
        wd = self.app.wd
        if text1 is not None:
            wd.find_element_by_name(field).click()
            wd.find_element_by_name(field).clear()
            wd.find_element_by_name(field).send_keys(text1)
        else:
            pass

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        self.select_first_contact()
        # click edit icon
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(new_contact_data)
        # submit edition
        wd.find_element_by_name("update").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # метод открытия домашней страницы должен браться из хелпера навигации
        self.app.navigation.open_home_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        contacts_list = []
        wd.find_elements_by_name("entry")
        for element in wd.find_elements_by_name("entry"):
            # нашли все переменные в строке
            all_cells = element.find_elements_by_tag_name("td")
            # забираем содержимое ячеек 2 и 3 в локальные вырезки
            firstname_cell = all_cells[2]
            lastname_cell = all_cells[1]
            id_cell = all_cells[0]
            # теперь получаем именно текст из вырезок
            firstname1 = firstname_cell.text
            lastname1 = lastname_cell.text
            #id = element.find_element_by_name("selected[]").get_attribute("value")
            id = int(id_cell.find_element_by_name("selected[]").get_attribute("value"))
            # в список добавляем полученное ФИ + id
            contacts_list.append(Contact(firstname2=firstname1, lastname=lastname1, id=id))
        return contacts_list

