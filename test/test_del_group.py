from model.group import Group
from random import randrange


def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(first_name="test"))
    old_groups = app.group.get_group_list()
    group_index = randrange(len(old_groups))
    app.group.delete_group_by_index(group_index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[group_index:group_index+1] = []
    assert old_groups == new_groups
