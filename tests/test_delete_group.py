__author__ = 'eya'

def test_delete_group(app):
    app.group.delete_first_group()