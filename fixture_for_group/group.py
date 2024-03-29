from selenium.webdriver.common.by import By
from model_for_group.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        self.app.driver.find_element(By.LINK_TEXT, "group page").click()

    def create(self, group):
        self.init_group_page()
        self.fill_group_form(group)
        # submit group creation
        self.app.driver.find_element(By.NAME, "submit").click()
        self.return_to_group_page()
        self.group_cache = None

    def fill_group_form(self, group):
        self.type("group_name", group.name)
        self.type("group_header", group.header)
        self.type("group_footer", group.footer)

    def type(self, field_name, text):
        if text is not None:
            self.app.driver.find_element(By.NAME, field_name).click()
            self.app.driver.find_element(By.NAME, field_name).send_keys(text)

    def init_group_page(self):
        self.app.driver.find_element(By.NAME, "new").click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        self.app.driver.get("http://localhost/addressbook/group.php")
        self.select_group_by_index(index)
        # удалить выбранную группу
        self.app.driver.find_element(By.NAME, "delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def select_ferst_group(self):
        self.app.driver.find_element(By.NAME, "selected[]").click()

    def select_group_by_index(self, index):
        self.app.driver.find_elements(By.NAME, "selected[]")[index].click()



    def modify_first_group(self):
        self.modify_group_by_index(0)


    def modify_group_by_index(self, index, new_group_data):
        self.app.driver.get("http://localhost/addressbook/group.php")
        self.select_group_by_index(index)
        # Нажимаем на кнопку для открытия модификации
        self.app.driver.find_element(By.NAME, "edit").click()
        # Заполнить форму.
        self.fill_group_form(new_group_data)
        # Подтвердить
        self.app.driver.find_element(By.NAME, "update").click()
        self.return_to_group_page()
        self.group_cache = None

    def count(self):
        self.app.driver.get("http://localhost/addressbook/group.php")
        return len(self.app.driver.find_elements(By.NAME, "selected[]"))


    group_cache = None


    def get_group_list(self):
        if self.group_cache is None:
            self.app.driver.get("http://localhost/addressbook/group.php")
            self.group_cache = []
            for element in self.app.driver.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id= id))

        return list(self.group_cache)

