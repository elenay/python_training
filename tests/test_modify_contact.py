__author__ = 'eya'
from model.contact import Contact
from random import randrange


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="NoOneWasHere"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    old_contact = old_contacts[index]
    old_contact.firstname = "blah"
    old_contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, old_contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)