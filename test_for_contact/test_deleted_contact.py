from model_for_contact.contact import Contact


def test_deleted_first_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create_new_contact(
            Contact(firstname="Максим", middlename="Сергеевич", lastname="Щербаков", nickname="andreich_zenin",
                    poletitle="test_title", company="test_company", address="Ryazan",
                    telephonehome="84913324693", telephonemobile="89105984136", telephonework="89156327896",
                    telephonefax="79102653789", email="sobaka@mail.ru", byear="1996", phone2="Ra",
                    notes="Ryazan"))
    app.contact.deleted_first_contact()
