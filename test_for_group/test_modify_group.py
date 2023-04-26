from model_for_group.group import Group


def test_modify_groups_name(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="Тестовая 1000"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_groups_header(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="Тест молификация"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
