# Generated by Selenium IDE
import pytest
from model_for_contact.contact import Contact
from fixture_for_contact.application_contact import Application_contact


@pytest.fixture
def app(request):
    # Создание фикстуры
    fixture = Application_contact()
    # Разрушение фикстуры
    request.addfinalizer(fixture.destroy_contact)
    return fixture


def test_create_new_contact(app):
    app.session_for_contact.login(username="admin", password="secret")
    app.create_new_contact(
        Contact(firstname="Андрей", middlename="Сергеевич", lastname="Зенин", nickname="andreich_zenin",
                poletitle="test_title", company="test_company", address="Ryazan",
                telephonehome="84913324693", telephonemobile="89105984136", telephonework="89156327896",
                telephonefax="79102653789", email="sobaka@mail.ru", byear="1996", phone2="Ra",
                notes="Ryazan"))
    app.session_for_contact.logout()


def test2_create_new_contact(app):
    app.session_for_contact.login(username="admin", password="secret")
    app.create_new_contact(
        Contact(firstname="Антон", middlename="Сергеевич", lastname="Лопата", nickname="anton_lopata",
                poletitle="не понятное поле, заполним так", company="АЛЬФА БАНК", address="Ryazan",
                telephonehome="74113354693", telephonemobile="89505984146", telephonework="79156627896",
                telephonefax="29102353789", email="kot@mail.ru", byear="1995", phone2="Rakkkkkk",
                notes="Ryazan2"))
    app.session_for_contact.logout()
