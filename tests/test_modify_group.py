__author__ = 'eya'
from model.group import Group

def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "testone"))
    app.group.modify_first_group(Group(name="edited name"))
