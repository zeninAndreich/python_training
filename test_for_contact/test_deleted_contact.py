
def test_deleted_first_contact(app):
    app.session_for_contact.login(username="admin", password="secret")
    app.contact.deleted_first_contact()
    app.session_for_contact.logout()
