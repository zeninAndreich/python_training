

#Удаление первой группы в списке.

def test_delete_first_groups(app):
    app.session_for_group.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session_for_group.logout()