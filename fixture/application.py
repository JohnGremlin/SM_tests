from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(0)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_main_url(self):
        self.driver.get("http://addressbook/")
        self.driver.set_window_size(1536, 720)

    def destroy(self):
        self.driver.quit()
