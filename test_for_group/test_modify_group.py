from model_for_group.group import Group


def test_modify_groups_name(app):
    app.group.modify_first_group(Group(name="Тестовая 1000"))


def test_modify_groups_header(app):
    app.group.modify_first_group(Group(header="Тест молификация"))
