from selenium.webdriver.support.ui import Select

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
        # заполняем дату рождения и годовщину
        select = Select(wd.find_element_by_name("bday"))
        select.select_by_visible_text('9')
        select = Select(wd.find_element_by_name("bmonth"))
        select.select_by_visible_text('March')
        wd.find_element_by_name("byear").send_keys("9999")
        select = Select(wd.find_element_by_name("aday"))
        select.select_by_visible_text('1')
        select = Select(wd.find_element_by_name("amonth"))
        select.select_by_visible_text('November')
        wd.find_element_by_name("ayear").send_keys("8888")
        # заполнение Secondary, переменные имеют заданное дефолтное значение
        self.edit_if_not_none("address2", secondary.address2)
        self.edit_if_not_none("phone2", secondary.home)
        self.edit_if_not_none("notes", secondary.notes)

    def edit_first_contact(self, new_group_data):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        self.select_first_contact()
        # click edit icon
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.edit_if_not_none(new_group_data,)
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