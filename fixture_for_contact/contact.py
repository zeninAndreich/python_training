from selenium.webdriver.common.by import By
from time import sleep


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_new_contact(self, contact):
        # create new contact and filling out the form
        self.app.driver.find_element(By.LINK_TEXT, "add new").click()
        self.fill_contact_form(contact)
        self.app.driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()

    def fill_contact_form(self, contact):
        self.type_contact("firstname", contact.firstname)
        self.type_contact("middlename", contact.middlename)
        self.type_contact("lastname", contact.lastname)
        self.type_contact("nickname", contact.nickname)
        # self.type_contact("title", contact.title)
        # self.type_contact("company", contact.company)
        # self.type_contact("address", contact.address)
        # self.type_contact("home", contact.home)
        # self.type_contact("mobile", contact.mobile)
        # self.type_contact("work", contact.work)
        # self.type_contact("fax", contact.fax)
        # self.type_contact("email", contact.email)
        # self.type_contact("bday", contact.bday)
        # self.type_contact("bmonth", contact.bmonth)
        #  self.type_contact("byear", contact.byear)
        #  self.type_contact("address2", contact.address2)
        # self.type_contact("phone2", contact.phone2)
        # self.type_contact("notes", contact.notes)

    def type_contact(self, field_firstname, text):
        if text is not None:
            self.app.driver.find_element(By.NAME, field_firstname).click()
            self.app.driver.find_element(By.NAME, field_firstname).send_keys(text)

    # для корректной работы теста на удаление, делал выборку элемента "удалить" через CSS_SELECTOR
    def deleted_first_contact(self):
        self.app.driver.get("http://localhost/addressbook/")
        self.select_first_contact()
        # удалить выбранный элемент.
        self.app.driver.find_element(By.CSS_SELECTOR, "[value='Delete']").click()
        assert self.app.driver.switch_to.alert.text == "Delete 1 addresses?"
        self.app.driver.switch_to.alert.accept()
        sleep(0.05)

    def select_first_contact(self):
        self.app.driver.find_element(By.NAME, "selected[]").click()

    def modify_first_contact(self, new_contact_data):
        self.app.driver.get("http://localhost/addressbook/")
        self.select_first_contact()
        # Нажать на кнопку,котороя открывые форму модификации.
        self.app.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > .center:nth-child(8) img").click()
        # Заполнить форму
        self.fill_contact_form(new_contact_data)
        # Подтвердить
        self.app.driver.find_element(By.CSS_SELECTOR, "input:nth-child(86)").click()

    def count_contact(self):
        self.app.driver.get("http://localhost/addressbook/")
        return len(self.app.driver.find_elements(By.NAME, "selected[]"))
