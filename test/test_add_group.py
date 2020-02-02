# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    # main test method
    old_groups = app.group.get_group_list()
    group = Group(first_name="Test First Name", middle_name="Test Middle Name", last_name="Test Last Name")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    # main test method
    old_groups = app.group.get_group_list()
    group = Group(first_name="", middle_name="", last_name="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
