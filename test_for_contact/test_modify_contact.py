from model_for_contact.contact import Contact


def test_modify_contact_firstname(app):
    app.session_for_contact.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Сергей"))
    app.session_for_contact.logout()


def test_modify_contact_middlename(app):
    app.session_for_contact.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(middlename="Сергеевич"))
    app.session_for_contact.logout()


def test_modify_contact_lastname(app):
    app.session_for_contact.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(lastname="Тестовый"))
    app.session_for_contact.logout()


def test_modify_contact_nickname(app):
    app.session_for_contact.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(nickname="Тестовый589"))
    app.session_for_contact.logout()


# ВНИМАНИЕ!!! Для создания новых тестов по модификации контатов, необходимо раскоментировать
# в fixture_for_contact \contact\fill_contact_form закоментированные элемены вспомогательного метода.
