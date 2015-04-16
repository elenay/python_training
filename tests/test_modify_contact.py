__author__ = 'eya'
from model.contact import Contact
import random


def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="NoOneWasHere"))
    old_contacts = db.get_contact_list()
    edited_contact = random.choice(old_contacts)
    edited_contact.firstname = "edited name"
    app.contact.edit_contact_by_id(edited_contact.id, edited_contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)