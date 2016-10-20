from selenium.webdriver.support.ui import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, general, telephone, email, secondary):
        wd = self.app.wd
        # open_contacts_page
        wd.find_element_by_link_text("add new").click()
        # заполнение первого блока - General, переменные имеют заданное дефолтное значение
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(general.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(general.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(general.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(general.nickname)
        wd.find_element_by_name("photo").send_keys("C:\fun\learn\Python\SoftwareTesting\занятие1\окружение.png")
        # картинка выбирается, но при просмотре созданного контакта не отображается
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(general.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(general.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(general.address)
        # заполнение телефона, переменные имеют заданное дефолтное значение
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(telephone.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(telephone.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(telephone.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(telephone.fax)
        # заполнение email, для иллюстрации значение переменной указано в тесте в явном виде
        # отдельно в классе дефолтное значение не задано
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(email.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(email.email3)
        # заполнение сайта, дополнительные классы не вводим
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("https://google.ru")
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
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(secondary.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(secondary.home)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(secondary.notes)
        # save_contact
        wd.find_element_by_name("submit").click()
        # return_to_home_page
        wd.find_element_by_link_text("home").click()
