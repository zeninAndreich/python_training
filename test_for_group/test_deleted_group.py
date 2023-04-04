from model_for_group.group import Group


# Удаление первой группы в списке.

def test_delete_first_groups(app):
    if app.group.count() == 0:
        app.group.create(Group(name="да пусть так вот будет"))
    app.group.delete_first_group()
