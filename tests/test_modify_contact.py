__author__ = 'eya'

from model.contact import Contact

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="noonewashere"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(firstname="edited"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
