from model_for_group.group import Group


def test_modify_groups_name(app):
    old_groups = app.group.get_group_list()
    group = Group(name="Тестовая 1000")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_groups_header(app):
    #old_groups = app.group.get_group_list()
    #app.group.modify_first_group(Group(header="Тест молификация"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
