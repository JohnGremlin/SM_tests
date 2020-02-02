from selenium.webdriver.common.by import By
from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.driver = app.driver
        self.app = app

    def create(self, group):
        self.open_groups_page()
        self.driver.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        # submit group creation
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit'").click()
        self.group_cache = None

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.first_name)
        self.change_field_value("group_header", group.middle_name)
        self.change_field_value("group_footer", group.last_name)

    def change_field_value(self, field_name, text):
        if text is not None:
            self.driver.find_element(By.NAME, field_name).click()
            self.driver.find_element(By.NAME, field_name).clear()
            self.driver.find_element(By.NAME, field_name).send_keys(text)

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, group_index):
        self.open_groups_page()
        self.select_group_by_index(group_index)
        # submit deletion
        self.driver.find_element(By.NAME, "delete").click()
        self.group_cache = None

    def select_first_group(self):
        # select first group element
        self.driver.find_element(By.NAME, "selected[]").click()

    def select_group_by_index(self, group_index):
        # select first group element
        self.driver.find_elements(By.NAME, "selected[]")[group_index].click()

    def modify_group_by_index(self, new_group_data, group_index):
        self.open_groups_page()
        self.select_group_by_index(group_index)
        # open modification form
        self.driver.find_element(By.NAME, "edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        self.driver.find_element(By.NAME, "update").click()
        self.group_cache = None

    def modify_first_group(self):
        self.modify_group_by_index(0)

    def open_groups_page(self):
        # open group page
        if not (self.driver.current_url.endswith("/groups.php") and len(self.driver.find_elements(By.NAME, "new")) > 0):
            self.driver.find_element(By.LINK_TEXT, "groups").click()

    def count(self):
        driver = self.app.driver
        self.open_groups_page()
        return len(driver.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            driver = self.app.driver
            self.open_groups_page()
            self.group_cache = []
            for element in driver.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(first_name=text, id=id))
        return list(self.group_cache)
