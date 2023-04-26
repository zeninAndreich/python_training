from model_for_group.group import Group


# Удаление первой группы в списке.

def test_delete_first_groups(app):
    if app.group.count() == 0:
        app.group.create(Group(name="да пусть так вот будет"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
