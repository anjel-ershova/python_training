from selenium import webdriver
from fixture.session import SessionHelper
from fixture.fixture_group import GroupHelper
from fixture.navigation import NavigationHelper
from fixture.fixture_contact import *

class Application:

    def __init__(self, browser, baseurl):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)
        self.group = GroupHelper(self)
        self.navigation = NavigationHelper(self)
        self.baseurl = baseurl

    # метод, проверяющий, валидна ли фикстура
    def is_valid(self):
        try:
           self.wd.current_url
           return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
