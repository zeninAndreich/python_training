from selenium import webdriver
from selenium.webdriver.common.by import By

from fixture_for_contact.session_for_contact import SessionHelper_contact
from fixture_for_contact.contact import ContactHelper


# Отдельный класс,в котором содержатся все вспомогательные методы.

class Application_contact:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.vars = {}
        self.session_for_contact = SessionHelper_contact(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def destroy_contact(self):
        self.driver.quit()
