from selenium.webdriver.support.ui import Select
from random import randint
from random import choice

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def edit_if_not_none(self, field, text1):
        wd = self.app.wd
        if text1 is not None:
            wd.find_element_by_name(field).click()
            wd.find_element_by_name(field).clear()
            wd.find_element_by_name(field).send_keys(text1)
        else:
            pass

    def create(self, general, telephone, email, secondary):
        wd = self.app.wd
        self.app.navigation.open_contact_creation_page()
        self.fill_contact_form(general, telephone, email, secondary)
        # save_contact
        wd.find_element_by_name("submit").click()
        # return_to_home_page
        self.app.navigation.open_home_page()

    def fill_calendar (self, day, month, year):
        # для дат (число, год) используем randint, как сделать случайный месяц - пока не ясно
        wd = self.app.wd
        wd.find_element_by_name(day).send_keys(randint(1, 30))
        select = Select(wd.find_element_by_name(month))
        select.select_by_visible_text('January')
        wd.find_element_by_name(year).send_keys(randint(1920,2017))


    def fill_contact_form(self, general, telephone, email, secondary):
        wd = self.app.wd
        # заполнение первого блока - General, используется метод fill_contact_form, переменные имеют заданное дефолтное значение
        self.edit_if_not_none("firstname", general.firstname)
        self.edit_if_not_none("middlename", general.middlename)
        self.edit_if_not_none("lastname", general.nickname)
        self.edit_if_not_none("nickname", general.lastname)
        wd.find_element_by_name("photo").send_keys("C:\\fun\\learn\\Python\\SoftwareTesting\\занятие1\\окружение.png")
        self.edit_if_not_none("title", general.title)
        self.edit_if_not_none("company", general.company)
        self.edit_if_not_none("address", general.address)
        # заполнение телефона, используется метод fill_contact_form, переменные имеют заданное дефолтное значение
        self.edit_if_not_none("home", telephone.home)
        self.edit_if_not_none("mobile", telephone.mobile)
        self.edit_if_not_none("work", telephone.work)
        self.edit_if_not_none("fax", telephone.fax)
        # заполнение email, используется метод fill_contact_form, для иллюстрации значение переменной указано в тесте в явном виде
        # отдельно в классе дефолтное значение не задано
        self.edit_if_not_none("email", email.email)
        self.edit_if_not_none("email2", email.email2)
        self.edit_if_not_none("email3", email.email3)
        # заполнение сайта, используется метод fill_contact_form
        self.edit_if_not_none("homepage", "https://google.ru")
        # заполняем дату рождения и годовщину, используем отдельный метод fill_calendar
        self.fill_calendar(day='bday', month='bmonth', year='byear')
        self.fill_calendar(day='aday', month='amonth', year='ayear')
        # заполнение Secondary, переменные имеют заданное дефолтное значение
        self.edit_if_not_none("address2", secondary.address2)
        self.edit_if_not_none("phone2", secondary.home)
        self.edit_if_not_none("notes", secondary.notes)

    def edit_first_contact(self, field, text1):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        self.select_first_contact()
        # click edit icon
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.edit_if_not_none(field, text1)
        # submit edition
        wd.find_element_by_name("update").click()

    def open_to_edit(self):
        #потом удалить
        wd = self.app.wd
        self.app.navigation.open_home_page()
        self.select_first_contact()
        # click edit icon
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    def click_to_submit(self):
        #потом удалить
        wd = self.app.wd
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

