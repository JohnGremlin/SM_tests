# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    # main test method
    old_groups = app.group.get_group_list()
    app.group.create(Group(first_name="Test First Name", middle_name="Test Middle Name", last_name="Test Last Name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    # main test method
    app.group.create(Group(first_name="", middle_name="", last_name=""))