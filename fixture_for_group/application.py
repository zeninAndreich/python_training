from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture_for_group.session_for_group import SessionHelper_group
from fixture_for_group.group import GroupHelper


# Отдельный класс в котором содержатся все вспомогательные методы.
class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.vars = {}
        self.session_for_group = SessionHelper_group(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/group.php")

    def destroy(self):
        self.driver.quit()

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False