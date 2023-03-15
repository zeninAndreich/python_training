from model_for_contact.contact import Contact


def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="Сергей"))


def test_modify_contact_middlename(app):
    app.contact.modify_first_contact(Contact(middlename="Сергеевич"))


def test_modify_contact_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="Тестовый"))


def test_modify_contact_nickname(app):
    app.contact.modify_first_contact(Contact(nickname="Тестовый589"))


# ВНИМАНИЕ!!! Для создания новых тестов по модификации контатов, необходимо раскоментировать
# в fixture_for_contact \contact\fill_contact_form закоментированные элемены вспомогательного метода.
