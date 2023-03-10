from model_for_group.group import Group


def test_modify_groups_name(app):
    app.session_for_group.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="Тестовая 1000"))
    app.session_for_group.logout()


def test_modify_groups_header(app):
    app.session_for_group.login(username="admin", password="secret")
    app.group.modify_first_group(Group(header="Тест молификация"))
    app.session_for_group.logout()
