# Generated by Selenium IDE

from selenium import webdriver
from selenium.webdriver.common.by import By
from group import Group


class TestTest445588():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_add_groups_new(self):
        self.login(username="admin", password="secret")
        self.create_group(Group(name="Тест по уроку 14 - вынос переменных в класс", header = "test_one", footer="test_two"))
        self.logout()

    def test_add_groups_new_pustaya(self):
        self.login(username="admin", password="secret")
        self.create_group(Group(name="", header="", footer=""))
        self.logout()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_group_page(self):
        self.driver.find_element(By.LINK_TEXT, "group page").click()

    def create_group(self, group):
        self.init_group_page()
        # fill group form
        self.driver.find_element(By.NAME, "group_name").click()
        self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.driver.find_element(By.NAME, "group_header").click()
        self.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.driver.find_element(By.NAME, "group_footer").click()
        self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        self.driver.find_element(By.NAME, "submit").click()
        self.return_to_group_page()

    def init_group_page(self):
        self.driver.find_element(By.NAME, "new").click()

    def login(self, username, password):
        self.open_home_page()
        self.driver.find_element(By.NAME, "user").click()
        self.driver.find_element(By.NAME, "user").send_keys(username)
        self.driver.find_element(By.NAME, "pass").click()
        self.driver.find_element(By.NAME, "pass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/group.php")
