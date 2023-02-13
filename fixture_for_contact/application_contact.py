from selenium import webdriver
from selenium.webdriver.common.by import By

from fixture_for_contact.session_for_contact import SessionHelper_contact


# Отдельный класс,в котором содержатся все вспомогательные методы.

class Application_contact:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.vars = {}
        self.session_for_contact = SessionHelper_contact(self)


    def create_new_contact(self, contact):
        # create new contact and filling out the form
        self.driver.find_element(By.LINK_TEXT, "add new").click()
        self.driver.find_element(By.NAME, "firstname").click()
        self.driver.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        self.driver.find_element(By.NAME, "theform").click()
        self.driver.find_element(By.NAME, "middlename").click()
        self.driver.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        self.driver.find_element(By.NAME, "theform").click()
        self.driver.find_element(By.NAME, "lastname").click()
        self.driver.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        self.driver.find_element(By.NAME, "theform").click()
        self.driver.find_element(By.NAME, "nickname").click()
        self.driver.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        self.driver.find_element(By.NAME, "theform").click()
        self.driver.find_element(By.NAME, "title").click()
        self.driver.find_element(By.NAME, "title").send_keys(contact.poletitle)
        self.driver.find_element(By.NAME, "company").click()
        self.driver.find_element(By.NAME, "company").send_keys(contact.company)
        self.driver.find_element(By.NAME, "address").click()
        self.driver.find_element(By.NAME, "address").send_keys(contact.address)
        self.driver.find_element(By.NAME, "home").click()
        self.driver.find_element(By.NAME, "home").send_keys(contact.telephonehome)
        self.driver.find_element(By.NAME, "mobile").click()
        self.driver.find_element(By.NAME, "mobile").send_keys(contact.telephonemobile)
        self.driver.find_element(By.NAME, "work").click()
        self.driver.find_element(By.NAME, "work").send_keys(contact.telephonework)
        self.driver.find_element(By.NAME, "fax").click()
        self.driver.find_element(By.NAME, "fax").send_keys(contact.telephonefax)
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys(contact.email)
        self.driver.find_element(By.NAME, "bday").click()
        dropdown = self.driver.find_element(By.NAME, "bday")
        dropdown.find_element(By.XPATH, "//option[. = '12']").click()
        self.driver.find_element(By.CSS_SELECTOR, "select:nth-child(61) > option:nth-child(14)").click()
        self.driver.find_element(By.NAME, "bmonth").click()
        dropdown = self.driver.find_element(By.NAME, "bmonth")
        dropdown.find_element(By.XPATH, "//option[. = 'February']").click()
        self.driver.find_element(By.CSS_SELECTOR, "select:nth-child(62) > option:nth-child(3)").click()
        self.driver.find_element(By.NAME, "byear").click()
        self.driver.find_element(By.NAME, "byear").send_keys(contact.byear)
        self.driver.find_element(By.NAME, "theform").click()
        self.driver.find_element(By.NAME, "address2").click()
        self.test = "address_test"
        self.driver.find_element(By.NAME, "address2").send_keys(self.test)
        self.driver.find_element(By.NAME, "phone2").click()
        self.driver.find_element(By.NAME, "phone2").send_keys(contact.phone2)
        self.driver.find_element(By.NAME, "notes").click()
        self.driver.find_element(By.NAME, "notes").send_keys(contact.notes)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()


    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def destroy_contact(self):
        self.driver.quit()