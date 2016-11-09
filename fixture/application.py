from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.fixture_contact import ContactHelper
from fixture.fixture_group import GroupHelper
from fixture.navigation import NavigationHelper


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)
        self.group = GroupHelper(self)
        self.navigation = NavigationHelper(self)

    def is_valid(self):
        try:
           self.wd.current_url
           return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
