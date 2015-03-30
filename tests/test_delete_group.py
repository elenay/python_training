__author__ = 'eya'
from model.group import Group
from random import randrange


def test_delete_random_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="testOne"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups)-1 == app.group.count()
    new_groups = app.group.get_group_list()
    del old_groups[index]
    assert old_groups == new_groups