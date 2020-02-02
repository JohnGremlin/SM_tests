from model.group import Group
from random import randrange


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(first_name="test first name"))
    old_groups = app.group.get_group_list()
    group_index = randrange(len(old_groups))
    group = Group(first_name="Modified group name")
    group.id = old_groups[group_index].id
    app.group.modify_group_by_index(group, group_index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[group_index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(middle_name="test group header"))
    old_groups = app.group.get_group_list()
    group_index = randrange(len(old_groups))
    group = Group(middle_name="Modified group header")
    group.id = old_groups[group_index].id
    app.group.modify_group_by_index(group, group_index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[group_index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(last_name="test group header"))
    old_groups = app.group.get_group_list()
    group_index = randrange(len(old_groups))
    group = Group(last_name="Modified group footer")
    group.id = old_groups[group_index].id
    app.group.modify_group_by_index(group, group_index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[group_index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
