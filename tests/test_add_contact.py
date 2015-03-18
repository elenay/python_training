__author__ = 'eya'

from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="one", lastname="two", email="one.threetwo@ww.com"))
