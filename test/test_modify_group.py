from model.group import Group


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(first_name="Modified group name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(middle_name="Modified group header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_footer(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(last_name="Modified group footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

