from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.driver = app.driver
        self.app = app

    def login(self, username, password):
        self.app.open_main_url()
        self.driver.find_element(By.NAME, "user").click()
        self.driver.find_element(By.NAME, "user").send_keys(username)
        self.driver.find_element(By.NAME, "pass").click()
        self.driver.find_element(By.NAME, "pass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def logout(self):
        # logout
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        return len(self.driver.find_elements(By.LINK_TEXT, "Logout")) > 0

    def is_logged_in_as(self, username):
        return self.driver.find_element(By.XPATH, "//div/div[1]/form/b").text == "("+username+")"
