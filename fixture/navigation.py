class NavigationHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") and len(wd.find_elements_by_xpath("//div/div[4]/form[2]/div[1]/input")) > 0):
            wd.find_element_by_link_text("home").click()

    def open_next_birthdays_page(self):
        wd = self.app.wd
        # на всякий случай
        if not(wd.current_url.endswith("/birthdays.php") and len(wd.find_elements_by_xpath("//div[@id='content']//h1[.='Next birthdays']")) > 0):
            wd.find_element_by_link_text("next birthdays").click()

    def open_contact_creation_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_xpath("//div[@id='content']//h1[.='Edit / add address book entry']")) > 0):
            wd.find_element_by_link_text("add new").click()

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def go_to_target_group_by_id(self, id):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/?group=%s" % id)
