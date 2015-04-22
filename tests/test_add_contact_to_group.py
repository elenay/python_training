__author__ = 'eya'
from model.contact import Contact


def test_add_contact(app, db, check_ui, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    old_contacts.append(contact)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
