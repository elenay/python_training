__author__ = 'eya'

from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="finn", header="four", footer="tour"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
