__author__ = 'eya'

from model.contact import Contact

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="NoOneWasHere"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="edited")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert len(old_contacts) == len(new_contacts)
