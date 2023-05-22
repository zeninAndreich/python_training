from model_for_group.group import Group
from random import randrange


# Удаление первой группы в списке.

def test_delete_some_groups(app):
    if app.group.count() == 0:
        app.group.create(Group(name="да пусть так вот будет"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index+1] = []
    assert old_groups == new_groups