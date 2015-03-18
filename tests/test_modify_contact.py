__author__ = 'eya'

from model.contact import Contact

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.open_add_contact_page()
        app.contact.create(Contact(firstname="testone"))
    app.contact.edit_first_contact(Contact(firstname="edited-one"))
