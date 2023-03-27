from selenium.webdriver.common.by import By
from time import sleep


class SessionHelper_group:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        self.app.open_home_page()
        self.app.driver.find_element(By.NAME, "user").click()
        self.app.driver.find_element(By.NAME, "user").send_keys(username)
        self.app.driver.find_element(By.NAME, "pass").click()
        self.app.driver.find_element(By.NAME, "pass").send_keys(password)
        self.app.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def logout(self):
        self.app.driver.find_element(By.LINK_TEXT, "Logout").click()
        sleep(0.05)

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        return len(self.app.driver.find_elements(By.LINK_TEXT, "Logout")) > 0

    def is_logged_in_as(self, username):
        # return self.app.driver.find_element(By.CSS_SELECTOR, "b").text == "(" + username + ")"
        return self.app.driver.find_element(By.XPATH, "//div[@id=\'top\']/form/b").text == "("+username+")"

    def ensure_login(self, username, password):
        if self.app.driver.is_logged_in():
            if self.app.driver.is_logged_in_as(username):
                return
            else:
                self.app.driver.logout()
        self.app.driver.login(username, password)
