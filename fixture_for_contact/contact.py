from selenium.webdriver.common.by import By


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_new_contact(self, contact):
        # create new contact and filling out the form
        self.app.driver.find_element(By.LINK_TEXT, "add new").click()
        self.app.driver.find_element(By.NAME, "firstname").click()
        self.app.driver.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        self.app.driver.find_element(By.NAME, "theform").click()
        self.app.driver.find_element(By.NAME, "middlename").click()
        self.app.driver.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        self.app.driver.find_element(By.NAME, "theform").click()
        self.app.driver.find_element(By.NAME, "lastname").click()
        self.app.driver.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        self.app.driver.find_element(By.NAME, "theform").click()
        self.app.driver.find_element(By.NAME, "nickname").click()
        self.app.driver.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        self.app.driver.find_element(By.NAME, "theform").click()
        self.app.driver.find_element(By.NAME, "title").click()
        self.app.driver.find_element(By.NAME, "title").send_keys(contact.poletitle)
        self.app.driver.find_element(By.NAME, "company").click()
        self.app.driver.find_element(By.NAME, "company").send_keys(contact.company)
        self.app.driver.find_element(By.NAME, "address").click()
        self.app.driver.find_element(By.NAME, "address").send_keys(contact.address)
        self.app.driver.find_element(By.NAME, "home").click()
        self.app.driver.find_element(By.NAME, "home").send_keys(contact.telephonehome)
        self.app.driver.find_element(By.NAME, "mobile").click()
        self.app.driver.find_element(By.NAME, "mobile").send_keys(contact.telephonemobile)
        self.app.driver.find_element(By.NAME, "work").click()
        self.app.driver.find_element(By.NAME, "work").send_keys(contact.telephonework)
        self.app.driver.find_element(By.NAME, "fax").click()
        self.app.driver.find_element(By.NAME, "fax").send_keys(contact.telephonefax)
        self.app.driver.find_element(By.NAME, "email").click()
        self.app.driver.find_element(By.NAME, "email").send_keys(contact.email)
        self.app.driver.find_element(By.NAME, "bday").click()
        dropdown = self.app.driver.find_element(By.NAME, "bday")
        dropdown.find_element(By.XPATH, "//option[. = '12']").click()
        self.app.driver.find_element(By.CSS_SELECTOR, "select:nth-child(61) > option:nth-child(14)").click()
        self.app.driver.find_element(By.NAME, "bmonth").click()
        dropdown = self.app.driver.find_element(By.NAME, "bmonth")
        dropdown.find_element(By.XPATH, "//option[. = 'February']").click()
        self.app.driver.find_element(By.CSS_SELECTOR, "select:nth-child(62) > option:nth-child(3)").click()
        self.app.driver.find_element(By.NAME, "byear").click()
        self.app.driver.find_element(By.NAME, "byear").send_keys(contact.byear)
        self.app.driver.find_element(By.NAME, "theform").click()
        self.app.driver.find_element(By.NAME, "address2").click()
        self.test = "address_test"
        self.app.driver.find_element(By.NAME, "address2").send_keys(self.test)
        self.app.driver.find_element(By.NAME, "phone2").click()
        self.app.driver.find_element(By.NAME, "phone2").send_keys(contact.phone2)
        self.app.driver.find_element(By.NAME, "notes").click()
        self.app.driver.find_element(By.NAME, "notes").send_keys(contact.notes)
        self.app.driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()