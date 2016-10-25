class GroupHelper:
    def __init__(self, app):
        self.app = app

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_if_not_empty(self, field, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field).click()
            wd.find_element_by_name(field).clear()
            wd.find_element_by_name(field).send_keys(text)

    def fill_group_form(self, group):
        wd = self.app.wd
        self.edit_if_not_empty("group_name", group.name)
        self.edit_if_not_empty("group_header", group.header)
        self.edit_if_not_empty("group_footer", group.footer)

    def create(self, group):
        wd = self.app.wd
        # open_groups_page
        wd.find_element_by_link_text("groups").click()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def edit_first_group(self, new_group_data):
        wd = self.app.wd
        # open group page
        wd.find_element_by_link_text("groups").click()
        self.select_first_group()
        # click edit button
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # submit edition
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        # open_groups_page
        wd.find_element_by_link_text("groups").click()
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()