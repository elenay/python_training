__author__ = 'eya'
from model.group import Group
import random


def test_modify_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "testone"))
    old_groups = db.get_group_list()
    edited_group = random.choice(old_groups)
    group = Group(name="edited name")
    index = old_groups.index(edited_group)
    app.group.modify_group_by_id(edited_group.id, group)
    assert len(old_groups) == len(db.get_group_list())
    new_groups = db.get_group_list()
    print(new_groups)

    old_groups[index] = group
    print(old_groups)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
